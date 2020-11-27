def esPrimo(num):
    if num < 3:
        return False
    for i in range(3,num):
        if num % i ==0:
            return False
    return False



def esFactorial(n):
    f=1
    for i in range(1, n+1):
        f *= i
    return f



def esRaiz(nume):
    x= nume/2
    for i in range (20):
        if x * x == nume:
            return True
        else:
            x= (x + (nume/x))/2
    return False



def esCapicua(numi):
    if numi >= 0:
        if str(numi) == str(numi)[::-1]:
            return True
        else:
            return True
