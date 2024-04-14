def contar_lineas_codigo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            
            # Filtrar las líneas en blanco y los comentarios
            lineas_filtradas = [linea.strip() for linea in lineas if linea.strip() and not linea.strip().startswith('#')]
            
            return len(lineas_filtradas)
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no se encontró.")
        return None

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")

    if ruta_archivo.endswith('.py'):
        num_lineas = contar_lineas_codigo(ruta_archivo)
        
        if num_lineas is not None:
            print(f"Archivo: {ruta_archivo}, número de líneas de código: {num_lineas}")
    else:
        print("El archivo ingresado no es un archivo .py.")

if __name__ == "__main__":
    main()