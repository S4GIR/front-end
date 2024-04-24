#IN THIS CLASS WE ARE GOING TO DISCUSS ABOUT LIST
#LIST=List is the order collection of more than one variable.These are separated by comma(,) 
#and always writen in square bracket[] 
#List is mutable 
                #EXAMPLE
list=[5,"sagir","age",34,"colour","black"] 
print(type(list))
print(len(list))
print(list)
print(list[1:4])   #It use the limit from index1 to index2
print(list[0])
print(list[1])
print(list[2])
print(list[-1])
if 5 in list:     #This keyword is used to the  find the element in list or not
    print("yes")
else:
    print("no")
if "agir" in "sagir":    #it will also work in string
    print("Yes")
else:
    print("No")
print(list[1:6:2])   #In this line use the jump condition by index of 2 
   

                         #LIST COMREHENSION
        
lst=[i for i in range(40)]  
print(lst)            #Print the value from 0 to 39 
lst2=[i+i for i in range(10)]
print(lst2)           #print the value from 0 to 10 but by adding its value double
lst2=[i*i for i in range(10) if i%2==0]
print(lst2)
