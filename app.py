import os
from flask import Flask, request, jsonify, render_template
from database import init_db, ReferencePoint, SessionLocal
from localization_engine import LocalizationEngine
import json

# Modificar la inicialización de Flask para definir la carpeta raíz explícitamente
# Esto ayuda a Flask a encontrar las carpetas 'templates' y 'static' sin importar el sistema operativo
app = Flask(__name__, root_path=os.path.dirname(os.path.abspath(__file__)))

engine = LocalizationEngine()

# Inicializa la base de datos si no existe
init_db()

@app.route('/')
def home():
    # Devuelve el dashboard (index.html) ubicado en la carpeta 'templates'
    return render_template('index.html')

@app.route('/api/calibrate', methods=['POST'])
def calibrate():
    """
    Endpoint para añadir nuevos puntos de referencia durante la fase de calibración.
    Espera datos JSON: {'x': float, 'y': float, 'rssi_data': {'AP_A': -dBm, ...}}
    """
    data = request.json
    if not data or 'x' not in data or 'y' not in data or 'rssi_data' not in data:
        return jsonify({"status": "error", "message": "Datos incompletos"}), 400

    db = SessionLocal()
    new_point = ReferencePoint(
        x=data['x'],
        y=data['y'],
        rssi_data=json.dumps(data['rssi_data'])
    )
    db.add(new_point)
    db.commit()
    db.close()
    return jsonify({"status": "success", "message": "Punto de referencia añadido"}), 201

@app.route('/api/train', methods=['POST'])
def train():
    """
    Endpoint para entrenar el modelo KNN una vez terminada la calibración.
    """
    db = SessionLocal()
    points = db.query(ReferencePoint).all()
    db.close()

    if not points:
        return jsonify({"status": "error", "message": "No hay puntos de referencia para entrenar"}), 400
    
    engine.train_model(points)
    return jsonify({"status": "success", "message": "Modelo entrenado correctamente"}), 200

@app.route('/api/locate', methods=['POST'])
def locate():
    """
    Endpoint principal para predecir la ubicación en tiempo real.
    Espera datos JSON: {'rssi_data': {'AP_A': -dBm, ...}}
    """
    data = request.json
    if not data or 'rssi_data' not in data:
        return jsonify({"status": "error", "message": "Datos incompletos"}), 400

    x, y, status = engine.predict_location(data['rssi_data'])
    if status == "Modelo no entrenado":
        return jsonify({"status": "error", "message": status}), 400

    return jsonify({"status": "success", "x": x, "y": y, "message": "Ubicación predicha"}), 200

if __name__ == '__main__':
    # Ejecutar la aplicación Flask en modo de depuración
    app.run(debug=True)

