import math
def main():
    #e^-x
    value = float(input("Ingrese x de e^-x\n"))

    #variables
    error_esperado = ((0.5 * math.pow(10, -7)) * 100)
    contador = 0
    error_aproximado = 100
    k = 0
    x = 0
    y = 0

    while True:
        if error_esperado < error_aproximado:
            y = x

            #Calulo de x con la serie de Maclaurin

            x = x + (math.pow(-1, k) * (math.pow(value, k))/(math.factorial(k)))
            contador += 1
            k += 1

            #calculo del error

            error_aproximado = abs((x-y)/x) * 100
            print("-" * 20)
            print(f"La iteracion actual es: {contador}")
            print(f"El valor de la iteracion #{contador} es: {x}")
            print(f"Su error aproximado es: {error_aproximado}")
            print("-" * 20)
            print("\n\n")
        #llegue a las cifras significativas necesarias
        else:
            #Imprimo el final y termino el ciclo infinito
            print("-" * 20)
            print(f"La iteracion final es: {contador}")
            print(f"El valor de la iteracion #{contador} es: {x}")
            print(f"Su error aproximado es: {error_aproximado}")
            print("-" * 20)
            print("\n\n")
            break




if __name__ == '__main__':
    main()