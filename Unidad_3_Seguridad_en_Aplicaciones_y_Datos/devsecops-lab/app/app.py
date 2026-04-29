from flask import Flask, request, jsonify, abort
import sqlite3
import subprocess
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), 'users.db')
DB_PASSWORD = 'SuperSecret123!'
SECRET_KEY = 'hardcoded-secret-key-never-do-this'
app.config['SECRET_KEY'] = SECRET_KEY


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email    TEXT NOT NULL,
            role     TEXT NOT NULL DEFAULT 'user'
        )
    ''')
    db.execute('''
        CREATE TABLE IF NOT EXISTS audit_log (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            action    TEXT NOT NULL,
            username  TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    db.executemany(
        'INSERT OR IGNORE INTO users (username, email, role) VALUES (?, ?, ?)',
        [
            ('admin', 'admin@empresa.com', 'admin'),
            ('jperez', 'jperez@empresa.com', 'user'),
            ('mgarcia', 'mgarcia@empresa.com', 'user'),
        ]
    )
    db.commit()
    db.close()


@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'service': 'user-api'})


@app.route('/users', methods=['GET'])
def list_users():
    db = get_db()
    users = db.execute('SELECT id, username, email, role FROM users').fetchall()
    db.close()
    return jsonify([dict(u) for u in users])


@app.route('/user', methods=['GET'])
def get_user():
    username = request.args.get('username', '')
    if not username:
        abort(400, description='Parámetro username requerido')
    db = get_db()
    cursor = db.cursor()
    query = f"SELECT id, username, email, role FROM users WHERE username = '{username}'"
    cursor.execute(query)
    row = cursor.fetchone()
    db.close()
    if row is None:
        abort(404, description='Usuario no encontrado')
    return jsonify(dict(row))


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json(force=True)
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    role = data.get('role', 'user').strip()
    if not username or not email:
        abort(400, description='username y email son requeridos')
    db = get_db()
    try:
        db.execute(
            'INSERT INTO users (username, email, role) VALUES (?, ?, ?)',
            (username, email, role)
        )
        db.commit()
    except sqlite3.IntegrityError:
        abort(409, description='El usuario ya existe')
    finally:
        db.close()
    logger.info('Usuario creado: %s', username)
    return jsonify({'message': f'Usuario {username} creado'}), 201


@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db = get_db()
    result = db.execute('DELETE FROM users WHERE id = ?', (user_id,))
    db.commit()
    db.close()
    if result.rowcount == 0:
        abort(404, description='Usuario no encontrado')
    return jsonify({'message': f'Usuario {user_id} eliminado'})


@app.route('/ping', methods=['GET'])
def ping():
    host = request.args.get('host', '')
    if not host:
        abort(400, description='Parámetro host requerido')
    logger.info('Ping a host: %s', host)
    result = subprocess.run(
        f'ping -c 1 {host}',
        shell=True,
        capture_output=True,
        text=True,
        timeout=10
    )
    return jsonify({'output': result.stdout, 'returncode': result.returncode})


@app.route('/logs', methods=['GET'])
def read_logs():
    log_file = request.args.get('file', 'app.log')
    log_path = os.path.join('/var/log', log_file)
    try:
        with open(log_path, 'r') as f:
            content = f.read()
        return jsonify({'file': log_file, 'content': content})
    except FileNotFoundError:
        abort(404, description='Archivo no encontrado')


@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(409)
def handle_error(e):
    return jsonify({'error': e.description}), e.code


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', debug=True)
