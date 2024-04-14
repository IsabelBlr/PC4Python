def guardar_precio_bitcoin(precio, fecha, archivo="bitcoin_prices.txt"):
    with open(archivo, "a") as f:
        f.write(f"{fecha}: {precio}\n")

def main():
    # Ejemplo de datos de precio y fecha
    precios = [
        {"fecha": "2024-04-13", "precio": 60000},
        {"fecha": "2024-04-12", "precio": 59000},
        {"fecha": "2024-04-11", "precio": 58000},
        # Agrega más datos de precio y fecha según lo necesites
    ]

    for dato in precios:
        guardar_precio_bitcoin(dato["precio"], dato["fecha"])

    print("Datos de precio de Bitcoin guardados en bitcoin_prices.txt")

if __name__ == "__main__":
    main()