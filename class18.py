          #IN THIS CLASS WE ARE GOING TO STUDY ABOUT THE TUPLE
#Tuple is also similar to list but the difference is tuple is immutable
#Tuple is written in simple bracket ()
                   #EXAMPLE
t=(2,4,6,3)
print(type(t),t)
a=(1)
print(type(a))  #Here it show integer type because single element is confused the
                #compiler to give the difference between integer and tuple
                #In this case we use comma(,) to differntiate the tuple
b=(1,)
print(type(b))    
tuple=(3,5,22,"Sagir","is","good","boy")
print(tuple)
print(tuple[0])
print(tuple[1])
print(tuple[2])
print(tuple[3])
print(tuple[4])
print(tuple[5])
print(tuple[6])
print(len(tuple))
print(tuple[1:7:2])
print(tuple[-4])
if "Sagir" in tuple:
    print("Yes it is in the tuple ")
else:
    print("NO it is not in tuple")
if "bhai" in tuple:
    print("Yes it is in the tuple ")
else:
    print("NO it is not in tuple")
tuple2=tuple[2:5]  #Here it does not change the value it creates the new tuple because 
                   # we know tuple is immutable  
print(tuple2)