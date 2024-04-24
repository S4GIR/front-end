# # #IN THIS CLASS WE ARE GOING TO DISCUSS ABOUT THE FUNCTION
# #    #Funtion is used to when we have to use the things for manytime then we make a funtion
# # #   to reduce the line of code and we can easliy use the funtion unlimited time by simply
# # #   calling the function name

# #    #NOTE:-----   We have to make the funtion always at the top of the of program
# #                        #EXAMPLE1(Example of mean)
# # print("program to find the Average:")
# # def gmean(a,b):
# #     mean=(a+b)/2
# #     print(mean)
# # a=int(input("Enter the first number:"))
# # b=int(input("Enter the second number:"))
# # gmean(a,b)
# # gmean(a,b)
# # if(a>b):
# #     print("First number is greater")
# # else:
# #     print("Second number is greater")

#                     #EXAMPLE2(USES OF PASS )
# def isLesserThan(a,b):
#     pass           #In python we use the keyword pass to run a program if any function is 
#                #left without making the body of the funtion ///  Pass:- pass the function
#                #without any error. 



#                             #EXAMPLE3(Example to find greater value)

# def isGreater(a,b):
#     if(a>b):
#         print("First number is greater")
#     else:
#         print("Second number is greater")
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# isGreater(a,b)
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# isGreater(a,b)
# n=int(input("Enter the number of repetition:"))
# while(n>=0):
#     c=int(input("Enter the first number:"))
#     d=int(input("Enter the second number:"))
#     isGreater(a,b)
#     n=n-1
                 
                  #EXAMPLE4(varible lenght argument)
#numbers=int(input("Enter the number to check its average"))
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is:",sum/len(numbers))

average(5,25,36,85,20,25)
average(5,25,1,)
average(355,255,655)

