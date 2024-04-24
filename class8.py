# #In this class we are going to study about the string 
# #NOTE :- STRING ARE IMMUTABLE IT CANT BE CANGABLE IT CREATES THE NEW STRING 
# a="Sagir"
# print(len(a))
# print(a.upper())   #It dose not change the string it creates the new string in All capital
# print(a.lower())   #It dose not change the string it creates the new string in All Small.
# b="Saaagir!!!!!!"
# print(b.rstrip("!"))  #rstrip hide the symbol or character just kie !!!!
#                            #rstip does not hide the word before example:-!!!!saaagir
#                            #NEW KEYWORD replace()
# c="!!!!!Sagirr!!!!!!Sagirr"
# print(a.replace("sagirr","Noor"))
capitaal="im sorry babu i cant !!!"
# print(capitaal.capitalize())  #IT capitalize the sentence
# print(c.count("Sagirr"))   #IT cout the number of same word repitative 
# print(capitaal.endswith("!!!"))              #Its give the True or False value for ending line 
print(capitaal.startswith("im"))
#Output is True
exam=["hii",50,"sagir"]
print(capitaal.rstrip("!"))
print(capitaal.center(66))#It move the word after 66 index
#print(exam.split())    FACING PROBLEM IN THIS QUESTION 
countcap=capitaal.count("m")
print(countcap)
print(capitaal.find("c"))
print(capitaal.find("a"))
print(capitaal.find("b"))
str1="hii,my name is Sagir and today i want to introduce myself.So please keep silient :"
capstr1=str1.capitalize()
print(capstr1)
print(str1.upper())
print(str1.index("my"))
exam2= "NO im not in your level so please keep away from me start 1223"
exam3="SoHowAreYouMyFriend"
print(exam2.isalnum())  #It gives the false value becouse of backspace
print(exam3.isalnum())
print(exam2.isalpha())
print(exam3.isalpha())
print(exam2.islower())
exam4="Hii My name is \nSagir"
print(exam4.isprintable())#It give the false value because \n is not printable 
print(exam2.isspace())
exam5="My Childhood Dream"
print(exam5.istitle())
