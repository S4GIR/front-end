# IN THIS LECTURE WE ARE GOING TO STUDY ABOUT MATCH CASE
x=int(input("Enter the number: "))
match x:  
  case 0:
    print("  X is zero ")#Print it if you enter the no 0
  case 1:
    print("X is one")#print the no if you enter the no 1
  case 2:
    print("X is two")#Print the no if you enter the no 2

  case 3:
    print("X is three")#Print the no if you enter the no 3

  case 4:
    print("X is four")#Print the no if you enter the no 4
  
  case _:
    print("not possible")#Print the no if you enter the no rather than 01234
  
  
