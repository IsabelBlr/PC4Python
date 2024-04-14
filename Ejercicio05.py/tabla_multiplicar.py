def guardar_tabla_multiplicar(n):
    with open(f"tabla-{n}.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n * i}\n")

def mostrar_tabla_multiplicar(n):
    try:
        with open(f"tabla-{n}.txt", "r") as f:
            print(f"Tabla de multiplicar del {n}:")
            print(f.read())
    except FileNotFoundError:
        print(f"El archivo tabla-{n}.txt no existe.")

def mostrar_linea_tabla(n, m):
    try:
        with open(f"tabla-{n}.txt", "r") as f:
            lineas = f.readlines()
            if m <= len(lineas):
                print(lineas[m - 1])
            else:
                print(f"La línea {m} no existe en el archivo tabla-{n}.txt.")
    except FileNotFoundError:
        print(f"El archivo tabla-{n}.txt no existe.")

def main():
    while True:
        print("Menú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                guardar_tabla_multiplicar(n)
            else:
                print("Número fuera de rango. Intente de nuevo.")
        
        elif opcion == "2":
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                mostrar_tabla_multiplicar(n)
            else:
                print("Número fuera de rango. Intente de nuevo.")

        elif opcion == "3":
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            m = int(input("Ingrese un número entero para la línea a mostrar: "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                mostrar_linea_tabla(n, m)
            else:
                print("Número fuera de rango. Intente de nuevo.")

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()