#IN THIS CLASS WE ARE GOING TO DISCUSS ABOUT THE WHILE LOOOOOP
          #IN while loop first we have to initialize then we have to give the condition
 #NOTE:---- In python we have only for loop or while loop we dont have the  do while loop
                         #EXAMPLE1
i=0
while i<=7: #here loop start
    print(i)  #It print the value of i
    i=i+1   #increament the value of i
print("Loop is Done")
                          #EXAMPLE2

i=int(input("Enter the number:")) #to take the input and to initialize i
while(i>8): #start loop
    i=int(input("Enter the number:"))  #Take input
    print("The number you type is :",i) #Print the value

                        #EXAMPLE3(Decreament loop)

i=int(input("Enter the number :"))
while(i>=0):
    print(i)
    i=i-1

                         #EXAMPLE4(WHILE LOOP WITH ELSE STATEMENT)

x=int(input("Enter the numnber:"))
while(x>=0):
    print(x)
    x=x-2
else:
    print("Done with the loop:")