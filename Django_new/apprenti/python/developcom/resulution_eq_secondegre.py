def resoleq2deg(a,b,c) : 
    disc = (b * b) - (4 * (a * c))
    print(disc)
    if disc < 0 : 
        return -1 
    if disc == 0 :
        return - ( b / (2 * a))



if __name__ == '__main__' : 

    print(resoleq2deg(1,2,1))
