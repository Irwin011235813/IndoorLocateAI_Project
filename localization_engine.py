import pandas as pd
import json
from sklearn.neighbors import KNeighborsClassifier
import joblib
import os

# Nombre del archivo donde guardaremos nuestro modelo entrenado
MODEL_PATH = 'knn_model.joblib'

class LocalizationEngine:
    def __init__(self):
        self.model = None
        self.is_trained = False
        # Intentar cargar un modelo existente al iniciar
        if os.path.exists(MODEL_PATH):
            self.model = joblib.load(MODEL_PATH)
            self.is_trained = True

    def train_model(self, reference_points_data):
        """
        Entrena el modelo KNN con los datos de calibración.
        """
        # Convertir los datos de la base de datos a un DataFrame de pandas
        data = []
        for point in reference_points_data:
            rssi_dict = json.loads(point.rssi_data)
            row = {'x': point.x, 'y': point.y}
            row.update(rssi_dict)
            data.append(row)
        
        df = pd.DataFrame(data)
        
        # Necesitamos rellenar los valores NaN (donde no se vio un AP) con un valor bajo, ej. -100 dBm
        df = df.fillna(-100)

        # Definir las características (RSSI values) y las etiquetas (location 'labels')
        # Para KNN necesitamos un ID único para cada punto de referencia como etiqueta
        # Y luego mapear ese ID de nuevo a las coordenadas X, Y reales.
        # Simplificación: usaremos las coordenadas como las etiquetas de salida por ahora, 
        # aunque KNN es un clasificador o regresor, no devuelve X,Y directamente.
        
        # Vamos a usar K-Nearest Neighbors Classifier, así que necesitamos IDs únicos para cada punto
        df['label'] = df['x'].astype(str) + ',' + df['y'].astype(str)
        
        features = df.drop(['x', 'y', 'label'], axis=1)
        labels = df['label']
        
        # Inicializar el clasificador KNN (K=3 es un buen punto de inicio)
        self.model = KNeighborsClassifier(n_neighbors=3)
        self.model.fit(features, labels)
        self.is_trained = True
        
        # Guardar el modelo entrenado en un archivo
        joblib.dump(self.model, MODEL_PATH)
        print(f"Modelo KNN entrenado y guardado en {MODEL_PATH}")


    def predict_location(self, current_rssi_data):
        """
        Predice la ubicación (X, Y) basándose en los datos RSSI actuales.
        """
        if not self.is_trained:
            return None, "Modelo no entrenado"

        # Preparar los datos de entrada en el formato correcto para pandas
        # Asegurarse de que las columnas coinciden con las usadas durante el entrenamiento
        input_data = pd.DataFrame([current_rssi_data])
        
        # Rellenar NaN con -100, igual que en el entrenamiento
        input_data = input_data.fillna(-100)
        
        # Predecir la etiqueta (que es nuestro string 'X,Y')
        predicted_label = self.model.predict(input_data)
        
        # Convertir la etiqueta de nuevo a coordenadas X, Y
        x_str, y_str = predicted_label.split(',')
        return float(x_str), float(y_str), "Ubicación predicha"
