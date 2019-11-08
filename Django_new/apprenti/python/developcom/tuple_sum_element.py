def sum(values) :
    i = 0
    s = 0
    while i < len(values) :
      s = s + values[i] 
      i +=  1
    return s

if __name__ == '__main__' :
   print(sum((1,2,3)))

