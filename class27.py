#IN THIS CLASS WE ARE GOING TO DISCUSS ABOUT ELSE WITH FOR LOOP
       #EXAMPLE
for i in range(11):
    print(i)
else:
    print("Sorry now i cant print because loop is over ")    #Here it will print 
    #the else condition print also

#NOTE:------- Q) can we use else statement with for or while loop 
            #Ans) YES
                     #else with if and else also
#EXAMPLE 
for i in range(10):
    print(i)
    if i==5:
        break
else:
    print("Sorry i cant print")#NOTE:-#Here it is not going to print the else statement
    #beacause else satement only work if loop is completely end but it is not completly 
    #end here it break between the loop
      

      #Example with while also work same

i=0
while(i<11):
    print(i)
    i=i+1
else:
    print("Sorry i cant print")

    #Example 2
i=0
while(i<11):
    print(i)
    i=i+1
    if i==4:
        break
else:
   print("Sorry i cant print")