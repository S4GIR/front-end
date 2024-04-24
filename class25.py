#IN THIS CLASS WE ARE GOING TO DISCUSS ABOUT THE DICTIONARY 
#DICTIONARY:-It is the ordered collection of different type of varible stored 
#in curli bracket separated with comma 
#Note:----- It dictionary we have 2 value 1) Key 2) Value 
#Both keys and values is written in semicolon(:)
#We can excess the value by writting keys name of all the keys by writting keys() method
#Note :--------- dict collect item in ordered wise only after 3.7 
#version before its is unordered
dict={"name":"sagir","age":18,"height":5.11}
print(dict) #It will print all the set same to same 
print(type(dict))
print(dict.keys())
print(dict.values())
for key in dict.keys():
    print(dict[key])
print(dict["name"])
print(dict["age"])
print(dict["height"])
for key in dict.keys():
    print(f"The vlaue corresponding to the key {key} is {dict[key]}")
print(dict.items())
for key, value in dict.items():
        print(f"The vlaue corresponding to the key {key} is {value}")
