   #IN THIS CLASS WE ARE GOING TO DISCUSS ABOUT THE LIST METHOD
l=[1,3,5,8,33,55,66,33,22]
print(l)
l.append(6)  #Append is the method which is used to add the element in last of list
# with the given value
print(l)
l.sort()     #Sort is the method used to sort the element in ascending order
print(l)
l.sort(reverse=True)  #By using reverse=True in sort method we sort in descending order
print(l)
l.reverse()   #Reverse is the method used to reverse the original list
print(l)
print(l.index(33))  #It gives the index of given element
print(l.count(33))  #Count is the method used to count the element in list


m=l
m[0]=2
print(l)  #Here we are printing the list l
#Here it change the value of previous list  by the value 2
   #if we dont want change our previous list we only want to change the new list then we 
   #have to used copy method
                         #COPY METHOD
m=l.copy()
m[0]=5
print(l)
print(m)
l.insert(1,566)  #Insert is the method used to insert the element in the list
                #Here 1 is the index where we want to insert and 566 is the new element
print(l)
a=[2,4,5,6,8,9,1]
print(a)
b=[23,43,65,45,35,87]
a.extend(b)   #Extend method open the list a & put it in the last of b list
print(a)
c=a+b   #It merge the two differet list in new single list
print(c) 

