#IN THIS CLASS WE ARE GOING TO DISCUSS ABOUT FSTRING
#fstring is also a type of string used for variable 

              #Example wwithout fstring
letter="Hey my name is {} and i am from {}"
name="Sagir"
country="India"
print(letter.format(name,country))   #This is called format used for variable
   
             #Example with fstring

print(f"Hey my name is {name} and i am from {country}")  #This is the example of fstring
#It take name and country from above string.


              #Example 2

price=490000.25254
txt=f"for only {price:.2f} dollar" #Here we use .2f because here we want to show the 
print(txt)                         #only after decimal is 2 digit means only (490000.25)

              #Example 3

print(f"Hey my name is {{name}} and i am from {{country}}") 
   #By using double curli bracket it show exactly what is written in bracket