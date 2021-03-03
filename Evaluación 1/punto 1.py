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
        A.append(i+10)

#B
    B.append(0)
    B.append(2)
    B.append(4)
    B.append(6)
    B.append(12)
    B.append(24)
    B.append(48)

#C

    for i in range(46):
        if(i%4==2):
            C.append(i)

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
ImprimirConjunto(DiferenciaSim(Diferencia(A,C),Interseccion(B,D)))
print("Segunda operación")
ImprimirConjunto(Diferencia(DiferenciaSim(Interseccion(B,D),C),Union(A,D)))
print("Tercera operación")
ImprimirConjunto(Union(Interseccion(Interseccion(A,B),C),Union(Diferencia(A,C),Diferencia(B,D))))
