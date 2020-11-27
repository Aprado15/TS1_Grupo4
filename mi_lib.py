<<<<<<< Updated upstream
=======
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

>>>>>>> Stashed changes
