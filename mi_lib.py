def esPrimo(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i ==0:
            return False
    return True

def evaluarPrimo(numero):
    contador=0
    resultado=True
    for i in range (1,numero+1):
        if (numero%i==0):
            contador+=1
        if (contador>2):
            resultado= False
            break
    return resultado

def esFactorial(n):
    f=1
    for i in range(1, n+1):
        f *= i
    return f

def esFactoriales(nani):
    f=1
    for i in range(nani):
        f *= nani-i
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
            return False
