def FizzBuzz(start, finish):
    n = finish - start + 1
    outlist = []
    
    for i in range(1, n + 1):
        x = start + i - 1
        if x % 15 == 0:
            outlist.append('fizzbuzz')
        elif x % 5 == 0:
            outlist.append('buzz')
        elif x % 3 == 0:
            outlist.append('fizz')
        else:
            outlist.append(x)
    return(outlist)