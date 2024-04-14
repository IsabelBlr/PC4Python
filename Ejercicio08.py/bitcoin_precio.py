import requests
import sqlite3
from datetime import date

def obtener_precio_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'USD': data['bpi']['USD']['rate_float'],
            'GBP': data['bpi']['GBP']['rate_float'],
            'EUR': data['bpi']['EUR']['rate_float']
        }
    else:
        print("Error al obtener el precio del bitcoin.")
        return None

def obtener_tipo_cambio_PEN():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT venta FROM sunat_info WHERE fecha = ?", (date.today().strftime("%Y-%m-%d"),))
    tipo_cambio = cursor.fetchone()[0]
    
    conn.close()
    
    return tipo_cambio

def crear_tabla_bitcoin():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bitcoin (
        fecha TEXT PRIMARY KEY,
        USD REAL,
        GBP REAL,
        EUR REAL,
        PEN REAL
    );
    """)
    
    conn.commit()
    conn.close()

def insertar_datos_bitcoin():
    precio_bitcoin = obtener_precio_bitcoin()
    tipo_cambio_PEN = obtener_tipo_cambio_PEN()
    
    if precio_bitcoin and tipo_cambio_PEN:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        
        fecha = date.today().strftime("%Y-%m-%d")
        USD = precio_bitcoin['USD']
        GBP = precio_bitcoin['GBP']
        EUR = precio_bitcoin['EUR']
        PEN = USD * tipo_cambio_PEN
        
        cursor.execute("INSERT INTO bitcoin (fecha, USD, GBP, EUR, PEN) VALUES (?, ?, ?, ?, ?)", (fecha, USD, GBP, EUR, PEN))
        
        conn.commit()
        conn.close()

def calcular_precio_10_bitcoins():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT PEN, EUR FROM bitcoin ORDER BY fecha DESC LIMIT 1")
    resultados = cursor.fetchone()
    
    precio_10_bitcoins_PEN = resultados[0] * 10
    precio_10_bitcoins_EUR = resultados[1] * 10
    
    conn.close()
    
    return precio_10_bitcoins_PEN, precio_10_bitcoins_EUR

def main():
    crear_tabla_bitcoin()
    insertar_datos_bitcoin()
    
    precio_10_bitcoins_PEN, precio_10_bitcoins_EUR = calcular_precio_10_bitcoins()
    
    print(f"Precio de comprar 10 bitcoins en PEN: {precio_10_bitcoins_PEN}")
    print(f"Precio de comprar 10 bitcoins en EUR: {precio_10_bitcoins_EUR}")

if __name__ == "__main__":
    main()