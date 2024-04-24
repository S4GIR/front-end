a=int(input("Enter a number you want to reverse"))
mod=0
prod=0
while a>0:
 mod=a%10
 prod=prod*10+mod
 a=a//10
print(prod)
