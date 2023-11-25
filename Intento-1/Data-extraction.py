# Practica 1: Extraccion de datos
# Rodrigo Antonio Martinez Macias 1896222

import kaggle

# Reemplaza 'nombre-de-tu-dataset' con el nombre del dataset de Kaggle que deseas descargar
dataset_name = 'szamil/who-suicide-statistics'

# Descarga el archivo ZIP del dataset
kaggle.api.dataset_download_files(dataset_name, path='./', unzip=False)

import zipfile

# Reemplaza 'nombre-del-archivo.zip' con el nombre del archivo ZIP descargado
archivo_zip = 'who-suicide-statistics.zip'

# Descomprime el archivo ZIP
with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
    zip_ref.extractall('./')  # Extrae los archivos en el directorio actual
