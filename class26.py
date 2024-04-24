#IN THIS CLASS WE ARE GOING TO DISCUSS ABOUT THE DICTIONARY METHOD

      #1) update 
#In this method one dictionary update is add the all element of another dictionary
emp1={111:56,234:89,123:76,677:98,243:87}
emp2={233:76,101:75,786:99}
print(emp1)
print(emp2)

emp1.update(emp2)
print(emp1)
     #clear
#In this method it delete the all element from the dictionary


#emp1.clear()
#print(emp1)

     #3) emtpy
#It also delete all element from dictionry
empty={}
print(empty)

     #4) pop
#In this method it remove one element from the given dictionary

emp1.pop(111)
print(emp1)

     #5) popitem
#In this method it remove only element but from the last position only

emp1.popitem()
print(emp1)

    #6) del
#In this method it delete the whole dictionary and show error

#del emp1
#print(emp1)

del emp1[234]
print(emp1)