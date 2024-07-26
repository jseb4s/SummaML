# Proyecto de Pronóstico y Clasificación de Demanda

## Descripción
Este repositorio contiene el código y los archivos necesarios para realizar el pronóstico de la demanda de Cementos Argos y un modelo de clasificación expuesto a través de un API. El proyecto está dividido en varias partes que incluyen la creación de modelos predictivos, la exposición de un servicio API y la generación de resultados.

/project-root
├── data/
│ ├── to_predict.csv
│ └── ... (otros archivos de datos, si los hay)

├── models/
│ └── modelo_entrenado.pkl

├── notebooks/
│ ├── sarima.ipynb
│ └── clasificacion.ipynb

├── scripts/
│ ├── main.py
│ └── test_api.py

├── results/
│ ├── resultados_servicio.json
│ ├── métricas_modelo.txt
│ └── demanda_pronosticada.csv

├── requirements.txt

├── README.md

└── teoria_.pdf

## Requisitos

- Python 3.8+
- Instalar las dependencias:
  ```bash
  pip install -r requirements.txt

## Uso
### 1. Pronóstico de Demanda y Clasificación
Abrir y ejecutar el notebook models.ipynb en la carpeta notebooks/. Allí se encuentra todo el proceso de cargue de datos para los modelos de pronóstico y clasificación. Las salidas de este notebook son:
- Archivo con las métricas de clasificación: results/classification_metrics.txt.
- Archivo con los resultados de clasificación: results/prediction_results.csv.
- Modelo de clasificación: models/classification_model.pkl
- Preprocesamiento modelo de clasificiación: models/preprocessor.pkl


### 2. Servicio API
Para ejecutar el servicio API:
python scripts/main.py

### 3. Probar API:
python scripts/test_api.py

### 4. Teoría
Las respuestas teóricas se encuentran en el archivo teoria_.pdf.

Instrucciones Adicionales
Notebooks
models.ipynb: Contiene el código y análisis para el modelo SARIMA utilizado en el pronóstico de la demanda. Además, incluye el código para el modelo de clasificación.

Scripts
main.py: Script principal para ejecutar el servicio API que consume el modelo de clasificación.
test_api.py: Script para probar el API, enviando solicitudes POST y mostrando las respuestas.

Archivos de Datos
to_predict.csv: Archivo CSV con los datos a ser pronosticados.
dataset_demand_acumulate.csv: Archivo CSV que contiene la información de la demanda entre el 2017-01 hasta el 2022-04 (año-mes).
dataset_alpha_betha.csv: Archivo CSV que contiene la información de todas las variables involucradas para realizar la clasificación 
de si un registro es Alpha o Betha, este cuenta con más de 7000 registros.


Resultados
demanda_pronosticada.csv: Archivo con los pronósticos generados por el modelo SARIMA.
métricas_modelo.txt: Archivo de texto con las métricas del modelo de clasificación.

