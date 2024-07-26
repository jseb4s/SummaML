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
1. Pronóstico de Demanda
Abrir y ejecutar el notebook models.ipynb en la carpeta notebooks/. Allí se encuentra todo el proceso de cargue de datos para los modelos de pronóstico y clasificación. Las salidas de este notebook son:
- Archivo con las métricas de clasificación.
- Archivo con los resultados
Esto generará el archivo con los pronósticos en results/prediction_results.csv.
3. Clasificación
Abrir y ejecutar el notebook clasificacion.ipynb en la carpeta notebooks/.
Esto generará el archivo del modelo entrenado en models/modelo_entrenado.pkl y las métricas en results/métricas_modelo.txt.

4. Servicio API
Para ejecutar el servicio API:
python scripts/main.py

Para probar API:
python scripts/test_api.py

Teoría
Las respuestas teóricas se encuentran en el archivo teoria_.pdf.

Instrucciones Adicionales
Notebooks
sarima.ipynb: Contiene el código y análisis para el modelo SARIMA utilizado en el pronóstico de la demanda.
clasificacion.ipynb: Incluye el código para el modelo de clasificación, junto con el análisis de datos y las métricas del modelo.
Scripts
main.py: Script principal para ejecutar el servicio API que consume el modelo de clasificación.
test_api.py: Script para probar el API, enviando solicitudes POST y mostrando las respuestas.
Archivos de Datos
to_predict.csv: Archivo CSV con los datos a ser pronosticados.
Resultados
demanda_pronosticada.csv: Archivo con los pronósticos generados por el modelo SARIMA.
métricas_modelo.txt: Archivo de texto con las métricas del modelo de clasificación.
resultados_servicio.json: Resultados generados por el servicio API.
