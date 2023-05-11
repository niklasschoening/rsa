import random

end = 1000

def BreakPrime(x):
    Ax = []
    b1 = True
    b2 = True
    while b1:
        a = 2
        b2 = True
        while b2:
            if (x % a) == 0:
                Ax.append(a)
                x = x/a
                if x == 1: 
                    b1 = False
                    break
                b2 = False
            a += 1
    return Ax

def IsPrime(x, isE, An):

    if not isE:
        isPrime=True
        for i in range(2,int(x)):                   
            if x % i == 0: isPrime = False     #mögliche Primzahl wird nach Teilern durchsucht
    else:
        isPrime=True
        for i in range(2,x):                   
            if x % i == 0 and not (An.__contains__(x)): isPrime = False
        
    return isPrime

def GetPrime(x,y, isE, An):
    isPrime = False
    if x<2: x=2

    while not isPrime:
        pPrime=random.randrange(x,y)                #random Zahl in range wird generiert
        if pow(2,(pPrime-1))%pPrime==1:             #Fermats kleiner Satz wird angewendet
            isPrime=IsPrime(pPrime, isE, An)
        
    return pPrime

def GetD(e, m):
    emodm = e%m
    em = e/m
    e2 = e
    m2 = m
    Aem = [em]

    y=0
    while emodm != 0:
        e2 = m2
        m2 = emodm
        emodm = e2 % m2
        em = e2/m2
        Aem.append(em)
        y += 1
    print(Aem)
    a = 0
    b = 1
    while y>0:
        b = a-(Aem[y]*b)
        print(b)
        y -= 1


p = GetPrime(0,end,False,None)
print(f'p: {p}')
q = GetPrime(0,end,False,None)
print(f'q: {q}')
n = p*q
print(f'n = p*q = {p}{q} = {n}')
m = (p-1)*(q-1)
print(f'm: {m}')
An = BreakPrime(m)
print(An)
e = GetPrime(0,m,True,An)
print(f'e: {e}')
GetD(e, m)