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
    #Conjuntos
    A = set()
    B = set()
    C = set()
    D = set()

    A = {1, 2, 4, 8, 15, 31, 46}

    #Conjunto B
    for i in range(6, 26):
        B.add(i)

    #Conjunto C
    for i in range(-5, 31):
        if i%3 == 0:
            C.add(i)
    
    #Conjunto D
    for i in range(6,50):
        if numero_primo(i):
            D.add(i)

    #Mostrar conjuntos
    print(f"Conjunto A {A}")
    print(f"Conjunto B {B}")
    print(f"Conjunto C {C}")
    print(f"Conjunto D {D}")

    print("-" * 80 + "\n")

    #Respuestas

    #(BnC)u(A^D)
    print(f"(BnC)u(A diferencia simetrica D): {union(interseccion(B, C),diferencia_simetrica(A, D))}")
    print("-" * 80 + "\n")

    #(B^C)^(Au(B-C))
    print(f"(B diferencia simetrica C)diferencia simetrica(Au(B-C)): {diferencia_simetrica(diferencia_simetrica(B, C), union(A, diferencia(B, C)))}")
    print("-" * 80 + "\n")
    #((C-B)^(AnD))n(AuBuC)
    print(f"((C-B)diferencia simetrica(AnD))n(AuBuC): {interseccion(diferencia_simetrica(diferencia(C,B), interseccion(A,D)),union(A,union(B,C)))}")
    print("-" * 80 + "\n")

if __name__ == '__main__':
    main()