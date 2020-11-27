def esPrimo(num):
    if num == 1 or num ==0:
        return False
    elif num == 2:
        return True
    elif num >2:
        for i in range(2, num):
            if num % i == 0:
                return False
            elif num % i !=0 and i==num-1:
                return True 

def factorial (*fac):
    for x in fac:
        fact=1
        for y in range(1,x+1):
            fact=fact*y
        print fact

def esCapicua(cap):
#Intervalo inferior
a=10
#Intervalo superior 
b=100
#Contador para la cantidad de capicuas
c=0
print("Los capicuas encontrados son los siguientes:")
for i in range(a,b+1):
    num_s=str(i)
    num_list=list(num_s)
    if num_list==num_list[::-1]:
        cap=''.join(num_list)
        c+=1
        print(cap)
        
print("Total de Capicuas:",c)


def esRaiz(x): 
    math.sqrt(x)
print(x)