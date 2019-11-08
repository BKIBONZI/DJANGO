def tabMultiplicationN(valeur) :
    n = 1
    while (n <= 10) :
        print(n," X ", valeur," = ", n *  valeur)
        n += 1

if __name__ == '__main__' :
    y = input("Quelle table de multiplication desirez-vous ?")
    tabMultiplicationN(int(y))
