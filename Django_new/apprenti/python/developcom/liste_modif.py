nombre = [1,2,3,4,5]


if __name__ == '__main__' :
    print(nombre)
    i = 0
    while i < len(nombre)  :
        print(nombre[i], end=' ')
        i += 1
    print()
    print(nombre[2:4])

    nombre[2:2] = [0]
    print(nombre)

    
