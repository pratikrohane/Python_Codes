#Factorial of given Number

def factorial(num):
    if num < 0:
        return 0
    elif num == 0 or num == 1:
        return 1 
    else:
        return(num * factorial(num-1))
    
num = int(input())

print("Factorial of", num, ":", factorial(num))