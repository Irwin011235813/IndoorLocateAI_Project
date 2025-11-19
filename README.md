# IndoorLocateAI Project: Sistema de Localización en Interiores con Wi-Fi y IA

## 📌 Descripción

**IndoorLocateAI** es un sistema conceptual tipo *Proof of Concept (PoC)* diseñado para resolver el desafío de la localización en interiores, donde el GPS pierde efectividad.
Utiliza la técnica de **Wi-Fi Fingerprinting** —aprovechando la intensidad de señal Wi-Fi (RSSI)— combinada con algoritmos de **Machine Learning (K-Nearest Neighbors / KNN)** para estimar coordenadas **X,Y** de activos móviles en entornos industriales, como almacenes.

El sistema incluye:

* Un backend robusto desarrollado con **Flask**
* Una interfaz web básica para supervisión
* Scripts de simulación para generar datos sin hardware físico

---

## 🚀 Características

* **Localización por Huella Digital RF**
  Utiliza la intensidad de las señales Wi-Fi ya existentes como base para estimar ubicación.

* **Algoritmo de IA (KNN)**
  Modelo de clasificación basado en `scikit-learn` capaz de predecir ubicación en tiempo real.

* **Backend Escalable (Flask)**
  Arquitectura modular con persistencia de datos mediante **SQLAlchemy** (*SQLite en desarrollo*).

* **Dashboard Web de Monitoreo**
  Permite visualizar posiciones y supervisar el sistema desde cualquier navegador.

* **Simulación de Dispositivos IoT**
  Script incluido que genera datos para pruebas sin necesidad de sensores reales.

---

## 🧠 Tecnologías Utilizadas

### Backend

* Python 3.x
* Flask
* SQLAlchemy (SQLite)
* Scikit-learn
* Pandas
* Requests

### Frontend

* HTML5
* CSS3
* JavaScript

### Otros

* Git & GitHub

---

## 📁 Estructura del Proyecto (Ejemplo)

```
IndoorLocateAI_Project/
│
├── app/               # Código del backend con Flask
├── models/            # Modelos y lógica ML
├── static/            # CSS, JS, assets u otros
├── templates/         # Archivos HTML (Frontend)
├── data/              # Dataset de entrenamiento / huellas digitales
├── scripts/           # Scripts de simulación
└── README.md
```

---

## ⚙️ Instalación y Configuración

### 🧰 Prerrequisitos

Asegúrate de tener instalado:

* Python 3.x
* Git

---

### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/Irwin011235813/IndoorLocateAI_Project.git
cd IndoorLocateAI_Project
```

### 2️⃣ Crear Entorno Virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

### 3️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar el Servidor

```bash
python app.py
```

Luego abrir en el navegador:

```
http://127.0.0.1:5000
```

---

## 📊 Simulación

El proyecto incluye un script que genera datos simulados de RSSI, permitiendo probar el sistema sin hardware físico.

Ejemplo:

```bash
python scripts/simulate_tags.py
```

---

## 🛠 Próximas Mejoras

* Mejor visualización del dashboard.
* Soporte para edificios con múltiples pisos.
* Integración con motores de optimización de hiperparámetros.
* Migración a PostgreSQL o MySQL para producción.

---

## 🤝 Contribuciones

Pull Requests, mejoras y reportes de issues son bienvenidos.

---

## 📄 Licencia

Este proyecto se distribuye bajo licencia **MIT** (modificar si aplica).
