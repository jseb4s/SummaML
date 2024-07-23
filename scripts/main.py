from flask import Flask, request, jsonify
import joblib
import os
import pandas as pd

models_path = os.path.join('.', 'models')

app = Flask(__name__)

# Cargar el modelo y el preprocesador
model = joblib.load(os.path.join(models_path, "classification_model.pkl"))
preprocessor = joblib.load(os.path.join(models_path, "preprocessor.pkl"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    
    # Preprocesar los datos de entrada
    X_preprocessed = preprocessor.transform(df)
    
    # Realizar la predicción
    prediction = model.predict(X_preprocessed)
    prediction_proba = model.predict_proba(X_preprocessed)[:, 1]
    
    result = {
        'prediction': int(prediction[0]),
        'probability': prediction_proba[0]
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)