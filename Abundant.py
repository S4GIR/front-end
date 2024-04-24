a=int(input("Enter the number to check it is a abundant number or not : \n"))
n=1
fact=0
while n<a:
    if a/n==0:
        fact=fact+n
    else:
        n=n+1
if fact>a:
    print("yes")
else:
    print("Not")
print(fact)

