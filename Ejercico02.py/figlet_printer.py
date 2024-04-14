import random
from pyfiglet import Figlet

def obtener_fuente():
    figlet = Figlet()
    fuentes_disponibles = figlet.getFonts()
    
    fuente = input(f"Por favor, ingrese el nombre de una fuente ({', '.join(fuentes_disponibles)}): ")
    
    if not fuente:
        fuente = random.choice(fuentes_disponibles)
    
    if fuente not in fuentes_disponibles:
        print("La fuente ingresada no es válida.")
        return obtener_fuente()
    
    return fuente

def main():
    fuente = obtener_fuente()
    texto = input("Por favor, ingrese el texto a imprimir: ")
    
    figlet = Figlet(font=fuente)
    texto_formateado = figlet.renderText(texto)
    
    print(texto_formateado)

if __name__ == "__main__":
    main()