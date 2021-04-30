import sys

def main():
    n = 4
    A = [[0 for columns in range(n+1)] for rows in range(n)]
    X = [0 for i in range(n)]
    A = [[2, 1, 4, -4, -1], [5, 5, 3, -2, 3], [2, 2, -1, 0, 9], [0, 5, -2, 1, 11]]

    # #llenar matriz 
    # for i in range(n):
    #     for j in range(n+1):
    #         print(f"Ingrese el valor de A[{i}][{j}]")
    #         A[i][j] = float(input())


    aux1 = 0
    #Calculando gauss-jordan
    for i in range(n):
        if A[i][i] == 0:
            aux0 = A[aux1 + 1]
            A[aux1 + 1] = A[aux1]
            A[i] = aux0
        
        for j in range(n):
            if i != j:
                aux = A[j][i]/A[i][i]

                for k in range(n+1):
                    A[j][k] = A[j][k] - aux * A[i][k]
        aux1 += 1

    for i in range(n):
        X[i] = A[i][n]/A[i][i]

    #Imprimir resultados
    print("\n\nLa respuesta es: \n")
    for i in range(n):
        print(f"X{i+1} = {X[i]}")


    


if __name__ == '__main__':
    main()