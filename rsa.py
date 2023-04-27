import random

def IsPrime(x):

    isPrime=True
    for i in range(2,x):                   
        if x % i == 0: isPrime = False     #mögliche Primzahl wird nach Teilern durchsucht
        
    return isPrime

def GetPrime(x,y):
    isPrime = False
    if x<2: x=2

    while not isPrime:
        pPrime=random.randrange(x,y)                #random Zahl in range wird generiert
        if pow(2,(pPrime-1))%pPrime==1:             #Fermats kleiner Satz wird angewendet
            isPrime=IsPrime(pPrime)
        
    return pPrime

print(GetPrime(0,1000))