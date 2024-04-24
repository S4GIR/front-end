              #IN THIS CLASS WE ARE GOING TO DISCUSS ABOUT METHOD OF TUPLE
#As we know tuple is immutable so if we want to change the value of tuple then first we 
#have to first copy the element in list then we can change the list then again we have to
#make it tuple
frnd=('Sagir','arif','abuzar','jishan','anuj','samar','sharik','abhisek','arpit')
print(frnd)
temp=list(frnd)
temp.append("Bhai Bhai")
#print(temp)
temp.pop(7)
#print(temp)
temp[1]="Arif"
#print(temp)
frnd=tuple(temp)
print(frnd)
                        #EXAMPLE TO SHOW THE MERGING OF TUPLE
frnd1=("sagir","arif")
frnd2=("irfan","farhan")
frnds=frnd1+frnd2
print(frnds)
                        #EXAMPLE TO THE COUNT METHOD IN TUPLE BY CREATING NEW TUPLE
tup=(1,2,3,4,3,5,3,6,3,7,3)
count=tup.count(3)
print("Count of 3 in tuple tup =",count)

                        #EXAMPLE TO THE INDEX METHOD IN TUPLE BY CREATING NEW TUPLE
res=tup.index(3)   #It shows the index of 3
print(res)
res2=tup.index(3,3,8) #It show the index of 3 but in given ratio 3:8
print(res2)       

                         #EXAMPLE TO THE lenght METHOD IN TUPLE BY CREATING NEW TUPLE
lenght=len(tup)
print(lenght)