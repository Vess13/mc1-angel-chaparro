def Union(A,B):
    C=[]
    for a in A:
        C.append(a)
    for b in B:
        C.append(b)
    return C
    
def Interseccion(A,B):
    C=[]
    for a in A:
        for b in B:
            if(a==b):
                C.append(a)
    return C

def Diferencia(A,B):
    C=[]
    flag=False
    for a in A:
        for b in B:
            if(a==b):
                flag=True
        if(flag==False):
            C.append(a)
        flag=False
    return C

def DiferenciaSim(A,B):
    return Union(Diferencia(A,B),Diferencia(B,A))

def ImprimirConjunto(A):
    B=[]
    for a in A:
        if a not in B:
            print(a)
            B.append(a)

if __name__=="__main__":
    A=[]
    B=[]
    loop=True

    for i in range(5):
        A.append(int(input("digite un numero para el conjuto A")))
    for i in range(5):
        B.append(int(input("digite un numero para el conjuto B")))
    while(loop==True):
        print(A)
        print(B)
        print(" - Que desea hacer - ")
        print("1. Union")
        print("2. Interseccion")
        print("3. Diferencia")
        print("4. Diferencia Simetrica")
        print("0. Salir")
        x=int(input("Indique el numero"))
        if(x==1):
            print("conjunto resultante")
            ImprimirConjunto(Union(A,B))
        if(x==2):
            print("conjunto resultante")
            ImprimirConjunto(Interseccion(A,B))
        if(x==3):
            print("conjunto resultante")
            ImprimirConjunto(Diferencia(A,B))
        if(x==4):
            print("conjunto resultante")
            ImprimirConjunto(DiferenciaSim(A,B))
        if(x==0):
            loop=False

