def t_found(liste, valeur) :
    i = 0
    trouve = False
    while i < len(liste) : 
        if liste[i] == valeur :
            trouve = True
            return trouve, i
        i +=1
        
    return trouve

if __name__ == '__main__' : 

    print(t_found((1,2,3,4,5,6), 0))
