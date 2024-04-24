#IN THIS EXERCISE WE ARE GOING TO MAKE KON BANEGA CRORE
sum=0
print("Welcome to kon banega crorepati")
print("1)Who is the prime minister of india")
l1=["Sagir","Amit","modi chor","Rahul"]
print(l1)
a=input()
if a=="modi chor":
    print("yes")
    sum=sum+1000
    print("2) What is the national bird of India")
    l2=["cat","peacock","crow","hen"]
    print(l2)
    b=input()
    if b=="peacock":
        print("yes")
        sum=sum+9000
        print("3)National animal pf India")
        l3=["deer","lion","tiger","bear"]
        print(l3)
        c=input()
        if c=="tiger":
            sum=sum+90000
            print("Hurray! You won the game and win prize money of ",sum)
        else:
            print("You loose and win the prize money of only",sum)
    else:
        print("You loose and win the prize money of",sum)
else:
    print("You loose the game")