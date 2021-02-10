#numeros primos
def numero_primo(n):
    cont=0
    for i in range(1, n+1):
        if i == 1 or i == n:
            continue
        if n % i == 0:
            cont+=1
    if cont>0:
        return False
    else:
        if(n == 1):
            return False
        else:
            return True

#union
def union(A, B):
    return (A | B)

#inteseccion
def interseccion(A, B):
    return (A & B)

#diferencia
def diferencia(A, B):
    return (A - B)

#diferencia simetrica
def diferencia_simetrica(A, B):
    return (A ^ B)


def main():
    A = set()
    B = set()
    C = set()
    D = set()

    #conjunto A
    for i in range(6,25):
        A.add(i)

    #conjunto B
    for i in range (1, 31):
        if(i % 2 == 1):
            B.add(i)

    #conjunto C
    C = {0, 3, 6, 9, 11, 15, 18, 20}

    #conjunto D
    for i in range(1,40):
        if(numero_primo(i)):
            D.add(i)

    print(f"Conjunto A {A}")
    print(f"Conjunto B {B}")
    print(f"Conjunto C {C}")
    print(f"Conjunto D {D}")

    print("-" * 80 + "\n")

    #(A^B)nC

    print(f"(A diferencia simetrica B) n C: {interseccion(diferencia_simetrica(A,B),C)}")
    print("-" * 80 + "\n")

    #(A-C)uB
    print(f"(A diferencia C) u B: {union(diferencia(A, C), B)}")
    print("-" * 80 + "\n")

    #A^(CUD)
    print(f"A diferencia simetrica (C u D): {diferencia_simetrica(A, union(C, D))}")
    print("-" * 80 + "\n")

    #(C-A)^(BnD)
    print(f"(C diferencia A) diferencia simetrica (B n D): {diferencia_simetrica(diferencia(C,A),interseccion(B, D))}")
    print("-" * 80 + "\n")


if __name__ == "__main__":


    main()