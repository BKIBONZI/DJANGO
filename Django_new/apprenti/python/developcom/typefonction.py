def add(a,b) : 
    return (a + b)

def multiplier(a,b) :
    return (a * b) 

def table(base, start=1, length=10, symbol="*", op=multiplier) :
    n = start 
    while n < start + length : 
        print(n, symbol, base,"=", op(n,base))
        n += 1

if __name__ == '__main__' : 
    table(4,length=2)
    table(4,length=5, symbol="+", op=add)

