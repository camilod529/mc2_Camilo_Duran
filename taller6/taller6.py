import math 

def main():
    angulo = float(input("Ingrese un angulo en grados: "))
    angulo = math.radians(angulo)

    #Definir error esperado
    error_esperado = ((0.5 * math.pow(10,-8)) * 100)
    contador = 0
    error_aproximado = 100
    k = 0
    x = 0 
    y = 0

    #definir el ciclo infinito
    while True:
        if(error_esperado<error_aproximado):
            y = x
            #Calculo con la definicion de serie de Maclaurin
            x = x + (math.pow(-1,k) * math.pow(angulo, 2 * k))/(math.factorial(2 * k))
            contador += 1
            k += 1
            
            #Calulo del error

            error_aproximado = abs((x-y)/x) * 100
            print("-" * 20)
            print(f"La iteracion actual es: {contador}")
            print(f"El valor de la iteracion #{contador} es: {x}")
            print(f"Su error aproximado es: {error_aproximado}")
            print("-" * 20)
            print("\n\n")
        else:
            print("-" * 20)
            print(f"La iteracion final es: {contador}")
            print(f"El valor de la iteracion #{contador} es: {x}")
            print(f"Su error aproximado es: {error_aproximado}")
            print("-" * 20)
            print("\n\n")
            break

if __name__ == '__main__':
    main()