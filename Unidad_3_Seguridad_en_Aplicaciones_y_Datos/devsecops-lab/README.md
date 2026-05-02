# Lab DevSecOps
## Arquitectura de Sistemas de Seguridad | CUGDL — UDG

---

## Instrucciones del laboratorio

1. Hacer **fork** de este repositorio en tu cuenta de GitHub

2. **Habilitar GitHub Actions en tu fork** — paso obligatorio que GitHub no hace automáticamente:
   - Ve a la pestaña **Actions** de tu fork
   - Haz clic en **"I understand my workflows, go ahead and enable them"**
   - Sin este paso el pipeline nunca se ejecutará, sin importar qué commits hagas

3. Clonar el fork y navegar a `Unidad_3_Seguridad_en_Aplicaciones_y_Datos/devsecops-lab/`

4. Levantar la aplicación (ver sección **Cómo correr la app**) y explorar los endpoints

5. Revisar `app/app.py` e identificar las vulnerabilidades presentes en el código

6. Completar el pipeline de seguridad — el archivo está en la **raíz del repositorio**:
   `.github/workflows/security.yml`
   > GitHub Actions solo detecta workflows en `/.github/workflows/` de la raíz del repo,
   > no en subcarpetas. Las rutas dentro del YAML ya apuntan a la carpeta correcta del lab.

7. Activar Dependabot en **Settings → Security → Dependabot**

8. Hacer commit del workflow y verificar en la pestaña **Actions**:
   - Puedes disparar el pipeline manualmente con el botón **"Run workflow"** sin necesidad de hacer push
   - SAST aparecerá en rojo si Semgrep detecta vulnerabilidades — eso es correcto y esperado
   - Los tests corren independientemente del resultado de SAST

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
lc_arquitectura_de_sistemas_de_seguridad/   ← raíz del repositorio
├── .github/
│   └── workflows/
│       └── security.yml    <- pipeline de seguridad (completar en el lab)
│
└── Unidad_3_Seguridad_en_Aplicaciones_y_Datos/
    └── devsecops-lab/
        ├── Dockerfile
        ├── README.md
        ├── app/
        │   ├── app.py              <- API Flask (analizar antes del pipeline)
        │   └── requirements.txt    <- dependencias del proyecto
        └── tests/
            └── test_app.py         <- tests básicos con pytest
```

> El `security.yml` está en la raíz porque GitHub Actions solo detecta
> workflows en `/.github/workflows/` del repositorio principal.

---

## Pistas para el análisis

Antes de correr el pipeline, revisa `app/app.py` manualmente.
Hay al menos **5 problemas de seguridad** distribuidos en el código.
Las siguientes pistas te orientan sin darte la respuesta — úsalas solo si te quedas atascado.

<details>
<summary>Pista 1 — Configuración inicial</summary>

Revisa las primeras líneas del archivo, antes de cualquier definición de ruta.
¿Encuentras valores sensibles escritos directamente en el código fuente?

Reflexiona: ¿qué implicaría que este repositorio fuera público en GitHub?
¿Cómo debería manejarse ese tipo de información en una aplicación real?

Referencia: OWASP Top 10 A02:2021 — Cryptographic Failures.

</details>

<details>
<summary>Pista 2 — Búsqueda de usuarios</summary>

Observa cómo se construye la consulta a la base de datos en el endpoint `/user`.
¿El valor que ingresa el usuario se valida o se inserta directamente en la consulta?

Prueba buscar un usuario usando este valor exacto como nombre:
```
' OR '1'='1
```
¿Qué devuelve la API? ¿Debería devolver eso?

Referencia: OWASP Top 10 A03:2021 — Injection.

</details>

<details>
<summary>Pista 3 — Diagnóstico de red</summary>

Mira cómo se procesa el parámetro `host` antes de ejecutar el comando del sistema operativo.
¿Se sanitiza de alguna forma antes de usarlo?

Desde el panel de Diagnóstico de Red, prueba este valor como host:
```
8.8.8.8; whoami
```
¿Qué aparece en la salida? ¿El servidor debería permitir eso?

Referencia: OWASP Top 10 A03:2021 — Injection (OS Command Injection).

</details>

<details>
<summary>Pista 4 — Visor de logs</summary>

El endpoint `/logs` recibe un nombre de archivo y lo lee del servidor.
¿Se verifica de alguna forma qué archivos están permitidos leer?

Prueba pasar este valor como nombre de archivo:
```
../../etc/passwd
```
¿Qué responde el servidor?

Referencia: Path Traversal / Directory Traversal — CWE-22.

</details>

<details>
<summary>Pista 5 — Arranque del servidor</summary>

Busca la última línea del archivo donde se inicia la aplicación Flask.
Hay dos parámetros que, combinados, representan un riesgo incluso en desarrollo.

Mira lo que imprime la terminal cuando arrancas la app.
¿Qué información sensible aparece en los logs del servidor?
¿Qué podría hacer alguien en tu misma red con esa información?

Referencia: CWE-94 / Flask debug mode exposure.

</details>

---

## Preguntas de entrega

Una vez analizado el código y ejecutado el pipeline, responde en tu reporte:

1. Lista cada vulnerabilidad encontrada: nombre, línea aproximada en el código y categoria OWASP/CWE.
2. ¿Qué herramienta del pipeline detectó cada una? ¿Alguna no fue detectada automáticamente?
3. Para cada vulnerabilidad, propone el cambio mínimo de código que la corregiría.
4. Revisa `requirements.txt`: ¿qué reportó pip-audit? ¿Qué versiones son seguras?
5. ¿Qué configuró Dependabot y qué ventaja ofrece frente a una auditoría manual?

---

## Advertencia

Este código contiene vulnerabilidades con fines educativos.
**NO usar en producción. NO ejecutar en redes no controladas.**
