def main ():
    
    
    repetir = True
    while repetir:
        A = set()
        B = set()
        n = int(input("Ingrese cuntos elementos tiene el conjunto A\n"))
        for i in range(n):
            n1 = float(input(f"Ingrese el numero {i+1} del conjunto A: "))
            A.add(n1)

        n = int(input("Ingrese cuntos elementos tiene el conjunto B\n"))
        for i in range(n):
            n1 = float(input(f"Ingrese el numero {i+1} del conjunto B: "))
            B.add(n1)
        print(A)
        print(B)


        menu = """
        Ingrese la operacion a realizar

        1. Union A u B
        2. Interseccion A n B
        3. diferencia A - B
        4. diferencia B - A
        5. diferencia simetrica 
    
        """
        n = int(input(menu))
        

        while n>5 or n<0:
            n = int(input("Ingrese una opcion valida\n" + menu))
            
        

        if n == 1:
            # union
            print(f"conjunto A u B = {A | B}")
            print(f"\nsu cardinalidad es de {len(A | B)}\n")
                
        if n == 2:
            # interseccion
            print(f"conjunto A n B = {A & B}")
            print(f"\nsu cardinalidad es de {len(A & B)}\n")
        if n == 3:
            # diferencia A - B
            print(f"diferencia A - B = {A - B}")
            print(f"\nsu cardinalidad es de {len(A - B)}\n")
            
        if n == 4:
            # diferencia B - A
            print(f"diferencia  B - A = {B - A}")
            print(f"\nsu cardinalidad es de {len(B - A)}\n")
        if n == 5:
            # diferencia simetrica
            print(f"diferencia simetrica A - B = {A ^ B}")
            print(f"\nsu cardinalidad es de {len(A ^ B)}\n")
        menu = """
        ¿Desea repetir el programa?
        1. Si
        2. No
        """
        r = int(input(menu))
        if r == 1:
            pass
        else:
            repetir = False



if __name__ == "__main__":
    main()