console.log("Script.js cargado. El dashboard está vivo.");

// Función de ejemplo para llamar a la API de entrenamiento
function trainModel() {
    console.log("Intentando entrenar el modelo...");
    fetch('/api/train', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        alert("Respuesta del servidor: " + data.message);
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
        alert("Ocurrió un error al intentar entrenar el modelo.");
    });
}

// En un sistema real, aquí iría la lógica para:
// 1. Obtener la ubicación actual de los tags periódicamente.
// 2. Actualizar la posición de los puntos en el div 'warehouse-map'.
