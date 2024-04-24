#EXERCISE FOR STRING IN THIS CALSS WE STUDY ABOUT THE STRING
#In python we can a write a string under a double quotes or single quotes
                          #Example
# name1="Sagir"
# name2='Sagir'
# print("My name is :"+name1)
# print("My name is :"+name2)
eat='I want to eat all types of fruits,"ecept melon'  # HERE WE USING
# SINGLE QUOTES FOR STRING AND DOUBLE FOR HIGHLIGHTING
# REPITITION OF SAME TPYES OF QUOTES IS NOT ALLOWED
print("fruit "+eat)
name= "my name is sagir ,"i am not bad guy""
print(name)         #HERE IT THROW ERROR DUE TO USES OF SAME TYPE OF QUOTES

           #STRING ALAWYS FIND IN SINGE LINE IF THE LINE EXCEED MORE THAN ONE LINE IT GET 
             #DIFFICULTIES SO FOR THAN ONE LINES WE USE QUOTES 3 TIMES
                                 #EXAMPLE
 poem='''How I wonder what you are.
 Up above the world so high.
 Like a diamond in the sky.
 Twinkle twinkle little star.
 How I wonder what you are.

 Twinkle twinkle little star.
 How I wonder what you are.
 Up above the world so high.
 Like a diamond in the sky.
 Twinkle twinkle little star.
 How I wonder what you are.'''
print("Your poem is "+poem)

#----------------------------------------------------------------------------------------------------------------------------------------------
#INDEX OF CHARACTER USING INDEX

                               #EXAMPLE
name="Sagir"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
         #INDEX FOR MULTIPLE LINE USING (FOR LOOP)
                                #EXAMPLE

poem="""djhddh.djf ededkedn edkehded .
djdhehjededdjed edjed edjd edjd xxjskkk.
jshdhd"""
for character in poem:
    print(character)