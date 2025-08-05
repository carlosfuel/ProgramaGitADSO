class TablaMultiplicar:
    def __init__(self,numero):
        self.numero = numero
        
    def imprimir_tabla(self):
        print
        for i in range(1, 11):
            resultado = self.numero * i
            print(f"{self.numero} x {i} = {resultado}")

def main():
    try:
        numero = int(input("**--ingrese un número para mostrar su tabla de multiplicar: "))
        tabla = TablaMultiplicar(numero)
        tabla.imprimir_tabla()
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()