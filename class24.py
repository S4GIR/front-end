#IN THIS CLASS WE ARE GOING TO DISCUSS ABOUT THE SET METHODS
#Sets method means how to manipulate the sets

    #1)Union and update in set
    #As we know union means merging of two sets and deleting the duplicate value

#Example of union
#union means merging the different sets without duplication
set1={2,3,4,5,6,1}
set2={1,2,7,8,9,5}
print(set1.union(set2))  #It merge the two set and remove duplicate value

#Example of update

set1.update(set2)  #Here it update the value of set1 with set2 means put all
                   #value which is not in the set1 from set2
print(set1,set2)

                    #2)Intersection in sets

#intersection means taking only comman part
  
print(set1.intersection(set2))


   #3) symmetric_differnce 
#Differnce means a union b minus(-)a intersection b
chess=(set1.symmetric_difference(set2))
print (chess)

   #4) differnce

less=(set1.difference(set2))
print(less)
    
    #5)  isdisjoint
#isdijoint check whether the two different set having atleast one 
#similar object if yes print True else print false

print(set1.isdisjoint(set2))

    #6) issuperset
#It means is a set having all the element from another set called superset

cities1={"Tokyo","Berlin","Nirobi","Denver","Moscow","Helenski"}
cities2={"Tokyo","Denver","Berlin"}
print(cities1.issuperset(cities2))

    #7)  issubset
# It means a set is called subset if having all the element same from another set

print(cities2.issubset(cities1))


     #8)  add
#Add method is used to add element in previous sets

cities1.add("Professor")
print(cities1)


     #9) remove
# It delete the element from the set if the element is not found it shows error
cities1.remove("Moscow")
print(cities1)
     # BUT if we use discard then it does not show any error
    #EXAMPLE OF BOTH REMOVE AND DISCARD
#cities1.remove("Moscow2")  It show an error and will not run and stop the program imediatley 
#print(cities1)
cities1.discard("Moscow2")    #It does not show any error but it pass the run
print(cities1)                #without any error

   
      #10) POP method 
#It delete the element randonly

cities1=cities1.pop()
print(cities1)

      #11) del method
#It is used to delete the entire sets and show an error 

#del cities1
#print(cities1)


      #12) clear method
#It is used to delete the all element without any error

#cities1=cities1.clear()
#print(cities1)

     # Check if item exists
info={"Calra",20,False,5.9}
if "Calra" in info:
    print("Yes")
else:
    print("No")
