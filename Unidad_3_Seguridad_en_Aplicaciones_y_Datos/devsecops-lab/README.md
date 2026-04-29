# Lab DevSecOps — Semana 9
## Arquitectura de Sistemas de Seguridad | CUGDL — UDG

---

## Instrucciones del laboratorio

1. Hacer **fork** de este repositorio en tu cuenta de GitHub
2. Navegar a `Unidad_3_Seguridad_en_Aplicaciones_y_Datos/devsecops-lab/`
3. Levantar la aplicación (ver sección **Cómo correr la app**) y explorar los endpoints
4. Revisar `app/app.py` e identificar las vulnerabilidades presentes en el código
5. Completar `.github/workflows/security.yml` con el pipeline de seguridad
6. Activar Dependabot en **Settings → Security → Dependabot**
7. Hacer commit del workflow, ir a la pestaña **Actions** y analizar los resultados

---

## Cómo correr la app

### Opción A — Docker (recomendada, no requiere instalar Python)

**Requisito:** tener [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado.

```bash
# Desde la carpeta devsecops-lab/
docker build -t user-api .
docker run -p 5000:5000 user-api
```

La API queda disponible en `http://localhost:5000`.

Para detener el contenedor: `Ctrl+C` y luego `docker ps` + `docker stop <id>`.

---

### Opción B — Python local

**Requisito:** Python 3.10 o superior. Verificar con `python --version`.

```bash
# 1. Crear entorno virtual (recomendado)
python -m venv venv

# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate

# 2. Instalar dependencias
pip install -r app/requirements.txt

# 3. Correr la aplicación
python app/app.py
```

La API queda disponible en `http://localhost:5000`.

---

## Endpoints disponibles

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/health` | Estado del servicio |
| GET | `/users` | Lista todos los usuarios |
| GET | `/user?username=<name>` | Busca un usuario por nombre |
| POST | `/user` | Crea un usuario (JSON: username, email, role) |
| DELETE | `/user/<id>` | Elimina un usuario por ID |
| GET | `/ping?host=<host>` | Ejecuta ping a un host |
| GET | `/logs?file=<archivo>` | Lee un archivo de log del sistema |

### Ejemplos con curl

```bash
# Listar usuarios
curl http://localhost:5000/users

# Buscar usuario
curl "http://localhost:5000/user?username=admin"

# Crear usuario
curl -X POST http://localhost:5000/user \
     -H "Content-Type: application/json" \
     -d '{"username": "nuevo", "email": "nuevo@empresa.com"}'

# Ping
curl "http://localhost:5000/ping?host=8.8.8.8"
```

---

## Estructura del laboratorio

```
devsecops-lab/
├── Dockerfile
├── README.md
├── app/
│   ├── app.py              ← API Flask (analizar antes del pipeline)
│   └── requirements.txt    ← dependencias del proyecto
├── tests/
│   └── test_app.py         ← tests básicos con pytest
└── .github/
    └── workflows/
        └── security.yml    ← pipeline de seguridad (completar en el lab)
```

---

## ⚠ Advertencia

Este código contiene vulnerabilidades con fines educativos.
**NO usar en producción. NO ejecutar en redes no controladas.**
