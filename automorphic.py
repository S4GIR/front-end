a=int(input("Enter the number to check it is automorphic or not "))
n=a*a
last1=0
last2=0
while n>0:
    last1=a%10
    last2=n%10
    if last1==last2:
     a=a//10
     n=n//10
     print("Automorphic")
    else:
        print("Not Automorphic")
    break

