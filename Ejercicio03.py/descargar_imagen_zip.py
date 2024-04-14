import requests
import zipfile
import os

def descargar_imagen(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print("Error al descargar la imagen.")
        return None

def guardar_imagen_como_zip(imagen_bytes, nombre_archivo):
    with zipfile.ZipFile(nombre_archivo, 'w') as archivo_zip:
        archivo_zip.writestr("imagen.jpg", imagen_bytes)

def descomprimir_zip(archivo_zip, directorio_destino):
    with zipfile.ZipFile(archivo_zip, 'r') as archivo_zip:
        archivo_zip.extractall(directorio_destino)

def main():
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    imagen_bytes = descargar_imagen(url)
    
    if imagen_bytes:
        guardar_imagen_como_zip(imagen_bytes, "imagen.zip")
        print("Imagen guardada como imagen.zip.")
        
        descomprimir_zip("imagen.zip", "./")
        print("Archivo ZIP descomprimido.")

if __name__ == "__main__":
    main()