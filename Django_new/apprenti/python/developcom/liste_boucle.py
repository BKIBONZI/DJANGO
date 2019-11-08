numbers = [1,2,3,4,5]
address = ["Rue de la Loi", 16, 1000, "Bruxelles", "Belgique"]

if __name__ == '__main__' :
    i = 0
    while i < len(numbers) :
        print(numbers[i])
        i += 1

    j = -1 
    while j >= - (len(numbers)) :
        print(numbers[j])
        j -= 1

    print(address)

    k = 0
    while  k < len(address) -1 :
        print(address[k], end=' ')
        k += 1

    print(address[k])

    address[4] = "Paris"

    print(address)

    # supression d'un élement de la liste   
    del(address[4])

    print(address)
    
    # extration d'une partie de la liste
    print(address[1:4])

    print(address[4])
