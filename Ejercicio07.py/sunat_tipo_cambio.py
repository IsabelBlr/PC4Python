import requests
import sqlite3

def obtener_tipo_cambio_2023():
    url = "https://apis.net.pe/api/tipo-cambio/2023"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al obtener el tipo de cambio.")
        return None

def crear_tabla():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sunat_info (
        fecha TEXT PRIMARY KEY,
        compra REAL,
        venta REAL
    );
    """)
    
    conn.commit()
    conn.close()

def insertar_datos(datos):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    for dato in datos:
        fecha = dato['fecha']
        compra = dato['compra']
        venta = dato['venta']
        
        cursor.execute("INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)", (fecha, compra, venta))
    
    conn.commit()
    conn.close()

def mostrar_contenido():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM sunat_info")
    filas = cursor.fetchall()
    
    for fila in filas:
        print(f"Fecha: {fila[0]}, Compra: {fila[1]}, Venta: {fila[2]}")
    
    conn.close()

def main():
    datos = obtener_tipo_cambio_2023()
    
    if datos:
        crear_tabla()
        insertar_datos(datos)
        print("Datos almacenados en la base de datos 'base.db' en la tabla 'sunat_info'.")
        print("Contenido de la tabla:")
        mostrar_contenido()

if __name__ == "__main__":
    main()