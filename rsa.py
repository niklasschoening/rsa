import random

def getPrime(x,y):      
    isPrime = False
    if x<2: x=2

    while not isPrime:
        pPrime=random.randrange(x,y)                #random Zahl in range wird generiert
        isPrime=True
        for i in range(2,pPrime):                   
            if pPrime % i == 0: isPrime = False     #wird nach Teilern durchsucht
        
    return pPrime

def getPrime2(x,y):
    isPrime = False
    if x<2: x=2

    while not isPrime:
        pPrime=random.randrange(x,y)                #random Zahl in range wird generiert
        if pow(2,(pPrime-1))%pPrime==1:             #Fermats kleiner Satz wird angewendet
            isPrime=True
        
    return pPrime

print(getPrime2(0,1000))