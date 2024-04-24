#IN THIS CLASS WE ARE GOING T0 DISCUSS ABOUT THE BREAK AND CONTINUE STATEMENT:
                               #BREAK
# In Break condition we exit the loop when condition is true
i=1
while(i<=12):
    print("5","X",i,"=",5*i)
    i=i+1
    if(i==11):
        break
                                #CONTINUE
 #It skip the statement if condition is true and continue the left program
i=1
while(i<=12):
    if(i==10):
        print("Skip the statement due to  continue condition")
        continue
    print("5","X",i,"=",5*i)
    i=i+1
