# #IN CLASS WE ARE GOING TO DISCUSS ABOUT THE EXCEPTION HANDLING
# #Exception Handling:--when a unwanted or unexpected error occurs during runtime or we
# #if handled those error then this called Execption handling

# #We can handled these error by simply using try or except keywords

# #NOTE:-- If we use try keyword then if our program have any error it 
# #jump the error or run the program after error
 

#             #Example
# #In below program it is going to work very smoothly but if we enter the input is integer 
# #but we input a string then it get confused how to multiply the table of string 
# #for example if i input sagir then it shows error but compile time it does not show any
# #error 
# #NOTE:-- In below program we also have to print a different print  statement due to string
# #error we also not able to print a different print statement so if wew use here exception
# #handling the we are able to print those statement which have not any error
             
#              #EXAMPLE WITHOUT ANY TRY AND EXCEPT (EXCEPTION HANLDING)

a=input("Enter a number ")
print(f"The multipliction table  of {a} is:")
for i in range(1,11):
    print(f"{int(a)}X {i}={int(a)*i}")
print("Wow it is working")

            EXAMPLE WITH TRY AND EXCEPT (EXCEPTION HANDLIND)

a=input("Enter a number ")
print(f"The multipliction table  of {a} is:")
try:
    for i in range(1,11):
       print(f"{int(a)}X {i}={int(a)*i}")
except:
    print("Invalid input")
    print("Exception handling is working")

print("Here is the end of program")


                  #EXAMPLE 2 OF EXECPTION HANDLING

try:
    num=int(input("Enter a integer: "))
    a=[3,6]
    print(a[num])
except ValueError:
    print("Number entered is not a integer ")

except IndexError:
    print("Index Error ")