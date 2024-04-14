import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        return float(data['bpi']['USD']['rate'].replace(',', ''))
    except requests.RequestException:
        print("Error al conectar con la API de CoinDesk.")
        return None 

def main():
    # Solicitar al usuario la cantidad de bitcoins que posee
    while True:
        try:
            cantidad_bitcoins = float(input("Por favor, introduzca la cantidad de bitcoins que posee: "))
            break
        except ValueError:
            print("Por favor, introduzca un número válido.")

    # Obtener el precio actual de Bitcoin en USD
    precio_bitcoin = obtener_precio_bitcoin()

    if precio_bitcoin is not None:
        # Calcular el costo en USD de la cantidad de bitcoins del usuario
        costo_en_usd = cantidad_bitcoins * precio_bitcoin

        # Mostrar el costo actual de los bitcoins en USD con cuatro decimales y separador de miles
        print(f"El costo actual de {cantidad_bitcoins} bitcoins es: ${costo_en_usd:,.4f}")

if __name__ == "__main__":
    main()
