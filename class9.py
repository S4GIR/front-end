# #In this class we are going to discuss about the condition Operator Which is used in python
# Example 
#    >(greater than),<(Smaller than),==(Equal to),!=(Not equal to),
#    >=(Greater than or equal to),<=(Smaller than or equal to)

                    #USES OF IF ELSE,ELSE,ELIF,NESTED IF ELSE
             #1)USES OF IF-ELSE
    #PROGRAM TO FINDING THE NO IS ODD OR EVEN
a=int(input("Enter the number to check if it is a even or odd number :"))
print("You entered the number is:",a)
if(a%2==0):
     print("It is a Even number:")
else:
    print("It is a odd number :")
print("Task Completed")


                      #2)USES OF ELIF
        #PROGRAM OF FINDING THE AGE
b=int(input("Enter the age :"))
print("Your age is : ",b)
if(b>=60):
    print("You are in old age group")
elif(b>=18):
    print("You are Youngster age group")
else:
    print("You are in child age group")
print("Task Completed:")
         

         #3)USES OF NESTED IF ELSE
     #Program to find the voter and gender
c=int(input("Enter the age :"))
d=input("Enter the gender :")
print("Your age is:",c)
if(c>=50):
    if(d=="girl"):
        print("You are a old lady ,You can vote :THANK YOU!")
    elif(d=="male"):
        print("You are a old man , You can vote :THANK YOU!")
    else:
        print("You are a old and your gender is Others, you can vote :THANK YOU!")
elif(c>=18):
    if(d=="girl"):
        print("You are the young lady , You can vote :THANK YOU!")
    elif(d=="male"):
        print("You are the young man,You can vote :THANK YOU!")
    else:
        print("You are a old and your gender is Others, you can vote :THANK YOU!")
else:
    if(d=="girl"):
        print("You are a child girl,You can't vote :THANK YOU!")
    elif(d=="male"):
        print("You are a child boy,you can't vote :THANK YOU!")
    else:
        print("You are a old and your gender is Others, you can't vote :THANK YOU!")
print("Task Completed")
