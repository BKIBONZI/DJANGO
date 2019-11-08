def pow(a, n) :
    if n == 1 :
        return a
    if n % 2 == 0 :
        return pow(a * a , n / 2)

    return a * pow (a * a, (n - 1) / 2 )

if __name__ == '__main__' :
    print(pow(4,3))
