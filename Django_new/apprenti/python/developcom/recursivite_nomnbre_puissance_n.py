def nombre_puissance_n(a,n) :
    if n == 1 :
        return a
    else :
        return a * nombre_puissance_n(a, n - 1)

if __name__ == '__main__' :
    print(nombre_puissance_n(4,3))
