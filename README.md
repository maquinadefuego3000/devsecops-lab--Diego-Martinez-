# Arquitectura de Sistemas de Seguridad
**Licenciatura en Ciberseguridad — CUGDL, Universidad de Guadalajara**

> Repositorio oficial de la materia. Aquí encontrarás guías de estudio,
> laboratorios, presentaciones y recursos para cada unidad del curso.

---

##  Docente
**Carlos Pulido Rosas**
- [carlos.pulido.rosas@gmail.com](mailto:carlos.pulido.rosas@gmail.com)
- Dudas sobre el contenido del repositorio: abrir un [Issue](../../issues).

---

##  Objetivo de la materia

Desarrollar la capacidad de diseñar, evaluar e implementar arquitecturas de
sistemas de seguridad robustas, aplicando principios como defensa en
profundidad, mínimo privilegio y Zero Trust, en entornos corporativos,
cloud e híbridos — con énfasis en la práctica a través de laboratorios
semanales y ejercicios de Red y Blue Team.

---

## Contenido del repositorio

| Carpeta | Descripción |
|---------|-------------|
| `Administracion/` | Plan de estudios oficial de la materia |
| `Templates/` | Plantillas base para guías de estudio y laboratorio |
| `Unidad_1_Fundamentos/` | Fundamentos de Arquitectura de Seguridad |
| `Unidad_2_Diseño_de_Redes/` | Diseño de Redes Seguras |
| `Unidad_3_Seguridad_en_Aplicaciones_y_Datos/` | Seguridad en Aplicaciones y Datos |
| `Unidad_4_Resiliencia_y_Operaciones/` | Resiliencia y Operaciones Seguras |
| `Red_Blue_Team/` | Escenarios y rúbricas para ejercicios ofensivos y defensivos |
| `.github/workflows/` | Pipeline CI/CD de seguridad — Lab DevSecOps (Semana 9) |

---

## Unidades del curso

### Unidad 1 — Fundamentos de Arquitectura de Seguridad `4 semanas`
- Introducción a la arquitectura de sistemas seguros
- Principios de diseño: defensa en profundidad, mínimo privilegio, segmentación
- Modelos de seguridad: Zero Trust, CIA Triad
- Normativas y estándares: ISO 27001, NIST CSF, CIS Controls
- Ciclo de vida de la arquitectura de seguridad

### Unidad 2 — Diseño de Redes Seguras `4 semanas`
- Arquitectura de red segura: DMZ, VLANs, segmentación lógica y física
- Tecnologías de protección perimetral: firewalls (NGFW), IDS/IPS
- Secure Network Protocols: VPNs (IPsec, SSL/TLS), tunneling
- Arquitectura para entornos híbridos y cloud (AWS, Azure, GCP)
- Monitorización y gestión de tráfico de red (NetFlow, SIEM)

### Unidad 3 — Seguridad en Aplicaciones y Datos `4 semanas`
- Diseño seguro de aplicaciones (DevSecOps)
- Arquitecturas de autenticación y autorización: IAM, MFA, OAuth, SAML
- Protección de datos: cifrado (en reposo, tránsito, uso), tokenización
- Arquitecturas para bases de datos seguras
- APIs seguras y gestión de vulnerabilidades web (OWASP Top 10)

### Unidad 4 — Resiliencia y Operaciones Seguras `4 semanas`
- Arquitecturas tolerantes a fallos y de alta disponibilidad
- Planes de continuidad del negocio (BCP) y recuperación ante desastres (DRP)
- Automatización de la seguridad: SOAR, orchestration
- Arquitecturas para respaldo y recuperación de datos
- Seguridad en entornos IoT, edge computing y entornos críticos

---

## Entorno de laboratorio

El **60% del curso** se desarrolla en laboratorio. Todos los labs se
realizan en una máquina virtual de **Kali Linux 2025.4** sobre
**Oracle VirtualBox 7**.

Consulta la guía de preparación del entorno antes de la primera sesión:
`Unidad_1_Fundamentos/Guias_de_Laboratorio/U1_S1_Lab_VirtualBox_Kali.docx`

Las imágenes OVA **no se incluyen en este repositorio** por su tamaño.
Descárgalas directamente desde los sitios oficiales:

- 🔗 [Oracle VirtualBox 7](https://www.virtualbox.org/wiki/Downloads)
- 🔗 [Kali Linux — Virtual Machines](https://www.kali.org/get-kali/#kali-virtual-machines)

### Software utilizado en el curso

| Herramienta | Uso | Disponibilidad |
|-------------|-----|----------------|
| Oracle VirtualBox 7 | Hipervisor | Gratuito |
| Kali Linux 2024.4 | Entorno de laboratorio | Gratuito |
| Wireshark | Análisis de tráfico de red | Preinstalado en Kali |
| Nmap | Reconocimiento y escaneo | Preinstalado en Kali |
| Metasploit Framework | Ejercicios Red Team | Preinstalado en Kali |

---

## Nomenclatura de archivos

Todos los archivos siguen el formato `U#_S#_Tipo_Tema.extension`:

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `U#` | Número de unidad | `U1` |
| `S#` | Número de semana | `S2` |
| `Tipo` | Tipo de archivo | `Lab`, `Estudio`, `Presentacion` |
| `Tema` | Nombre corto del tema | `Nmap_Reconocimiento` |

Ejemplo completo: `U1_S2_Lab_Nmap_Reconocimiento.docx`

---

## Evaluación

| Evidencia | Porcentaje |
|-----------|------------|
| Asistencia y participación | 10% |
| Tareas semanales | 15% |
| Prácticas de laboratorio | 25% |
| Exámenes por unidad (U1, U2, U3, U4) | 30% |
| Proyecto final | 20% |
| **Total** | **100%** |

---

## Políticas del curso

**Entregas**
- Las prácticas de laboratorio se entregan en un plazo de **24 horas**
  después de la sesión.
- Entregas tardías (hasta 72h): calificación máxima de **7/10**.
- No se aceptan entregas después de las 72 horas.

**Asistencia**
- La asistencia mínima requerida para tener derecho a evaluación final
  es del **80%**.

**Laboratorio**
- Cada alumno es responsable de mantener su VM operativa durante el semestre.
- Antes de cada ejercicio de Red/Blue Team se debe tomar un snapshot
  de la VM para poder restaurarla si es necesario.
- Está prohibido usar las herramientas del curso fuera del entorno
  de laboratorio controlado. El uso indebido tiene consecuencias
  académicas y posiblemente legales.

**Integridad académica**
- Los laboratorios y tareas son individuales salvo que se indique
  explícitamente lo contrario.
- El uso de IA para generar respuestas de reflexión sin análisis
  propio no está permitido.

---

## ¿Cómo usar este repositorio?

1. Haz **Fork** de este repositorio a tu cuenta personal en GitHub.
2. Clona tu fork en tu equipo:
```bash
   git clone https://github.com/tu_usuario/lc_arquitectura_de_sistemas_de_seguridad.git
```
3. Configura el repo original como `upstream` para recibir actualizaciones:
```bash
   git remote add upstream https://github.com/carpuro/lc_arquitectura_de_sistemas_de_seguridad.git
```
4. Antes de cada sesión, sincroniza los cambios:
```bash
   git pull upstream main
```

---

## ⚠️ Aviso legal

Este repositorio es de uso exclusivo para estudiantes inscritos en la
materia durante el semestre activo. El contenido es propiedad del docente
y de la Universidad de Guadalajara. No está permitida su distribución,
reproducción o uso fuera del contexto del curso sin autorización expresa.

---

Última actualización: mayo 2026