def isDivisor(d,n) :
    return n % d == 0 


def isPrime(n) :
    d = 1
    nbDivisors = 0
    while d <= n :
        if isDivisor(d,n) :
            nbDivisors += 1
        d += 1
        
    return nbDivisors == 2

if __name__ == '__main__' :
    v = input('Entrez le nombre :')
    print(isPrime(int(v)))
