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
    C=[]
    D=[]
#A
    for i in range(20):
        if(i!=0):
            A.append(i+5)

#B
    for i in range(31):
        if(i!=0):
            if (i%2==1):
                B.append(i)
    print(B)
#C
C.append(0)
C.append(3)
C.append(6)
C.append(9)
C.append(11)
C.append(15)
C.append(18)
C.append(20)
#D
D.append(2)
D.append(3)
D.append(5)
D.append(7)
D.append(11)
D.append(13)
D.append(17)
D.append(19)
D.append(23)
D.append(29)
D.append(31)
D.append(37)
#Las operaciones
print("Primer operación")
ImprimirConjunto(Interseccion(C,DiferenciaSim(A,B)))
print("Segunda operación")
ImprimirConjunto(Union(Diferencia(A,C),B))
print("Tercera operación")
ImprimirConjunto(DiferenciaSim(A,Union(C,D)))
print("Cuarta operación")
ImprimirConjunto(DiferenciaSim(Diferencia(C,A),Interseccion(B,D)))