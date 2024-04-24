#IN THIS QUESTION WE 

a=int(input("Enter a number"))
r=0
sum=0
while a>0:
    r=a%10
    sum=sum+r
    a=a//10
print(sum)