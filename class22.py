#IN THIS CLASS WE ARE GOING TO DISCUSS ABOUT THE RECURSION
#Recursion is the process of defining something in term of itself
                  #OR
#Recursion means calling fuction in itself 

                #Example of Factorial 

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1) #Here factorial function calling itself 
a=int(input("Enter the number you want to see the factorial:"))
print(factorial(a))

                 #Example of fibonacci series

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
b=int(input("Enter the number to see the fibonacci series: "))
print(fibonacci(b))