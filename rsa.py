import random

end = 1000

def BreakPrime(x):
    goes = True
    y = x
    Ax = []

    while goes:
        if (y % 2) == 0:      #if even
            Ax.append(2)
            y = y/2
        else:
            a = y
            while goes:
                a -= 1
                if (y % a) == 0:
                    Ax.append(y/a)
                    Ax.append(a)
                    goes = False
            goes = False
    return Ax

def IsPrime(x, isE, An):

    if not isE:
        isPrime=True
        for i in range(2,x):                   
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

p = GetPrime(0,end,False,None)
print(f'p: {p}')
q = GetPrime(0,end,False,None)
print(f'q: {q}')
n = p*q
print(f'n = p*q = {p}{q} = {n}')
An = BreakPrime(n)
print(An)
m = (p-1)*(q-1)
print(f'm: {m}')
e = GetPrime(0,m,True,An)
print(f'e: {e}')