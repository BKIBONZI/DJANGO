def recursivitenpNombre(n) :
    if n == 0 :
        return 0
    else :
        return recursivitenpNombre(n - 1) + n 

if __name__ == '__main__' :
    print(recursivitenpNombre(4))
