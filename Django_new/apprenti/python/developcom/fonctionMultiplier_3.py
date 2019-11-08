def Multiplier_3(valeur, debut, fin) :
    n = debut
    while (n <= fin):
        print(n, " X ", valeur," = ", n * valeur)
        n += 1 

if __name__ == '__main__' :
    Multiplier_3(5,7,9)
