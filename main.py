# main.py
import Operaciones

def ejecutar_calculadora():
    print("--- Calculadora Modular ---")
    
    try:
        # 1. Solicitar números
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        # 2. Solicitar operación
        print("\nOperaciones disponibles:")
        print("1. Suma\n2. Resta\n3. Multiplicación\n4. División")
        opcion = input("Elige una opción (1-4): ")

        # 3. Procesar y mostrar resultado
        if opcion == '1':
            resultado = Operaciones.sumar(num1, num2)
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif opcion == '2':
            resultado = Operaciones.restar(num1, num2)
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif opcion == '3':
            resultado = Operaciones.multiplicar(num1, num2)
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif opcion == '4':
            resultado = Operaciones.dividir(num1, num2)
            print(f"Resultado: {resultado}")
        else:
            print("Opción no válida.")
            
    except ValueError:
        print("Error: Por favor, ingresa solo números válidos.")

if __name__ == "__main__":
    ejecutar_calculadora()