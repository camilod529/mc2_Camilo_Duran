def main():

    n = int(input("Ingrese el tamaño de la matriz "))
    A = [[0 for columns in range(2*n)] for rows in range(n)]
    
    
    #llenar matriz 
    for i in range(n):
        for j in range(n):
            print(f"Ingrese el valor de A[{i}][{j}]")
            A[i][j] = float(input())


    #Usando los ceros creados por fuera de la matriz n*n para crear la matriz identidad
    for i in range(n):        
        for j in range(n):
            if i == j:
                A[i][j+n] = 1

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

                for k in range(2*n):
                    A[j][k] = A[j][k] - aux * A[i][k]
        aux1 += 1
    #calcula en la matriz identidad la matriz inversa
    for i in range(n):
        aux2 = A[i][i]
        for j in range(2*n):
            A[i][j] = A[i][j]/aux2

    print("\n\nLa respuesta es: \n")
    for i in range(n):
        for j in range(n, 2*n):
            print(A[i][j], end="\t")
        print()
        

if __name__ == '__main__':
    main()
