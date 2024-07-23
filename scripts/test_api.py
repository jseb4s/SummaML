import requests

# URL de la API
url = 'http://127.0.0.1:5000/predict'

# Datos de entrada
data = {
    "SeniorCity": 1,
    "Partner": "Yes",
    "Dependents": "No",
    "Service1": "Yes",
    "Service2": "No",
    "Security": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "Charges": 190.85,
    "Demand": 1570.45
}

# Enviar solicitud POST
response = requests.post(url, json=data)

# Verificar el estado de la respuesta HTTP
if response.status_code == 200:
    try:
        # Intentar convertir la respuesta a JSON
        response_json = response.json()
        print(response_json)
    except ValueError:
        print("Error al decodificar la respuesta JSON")
else:
    print(f"Error en la solicitud HTTP: {response.status_code}")
    print(response.text)
