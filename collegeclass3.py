# # #Finidng power of anynumber using function
# # def Hello():
# #  print("Hello!Goodnorning")
# # Hello()


#     #EXAMPLE OF FINDING A POWER OF ANY GIVEN NUMBERR
# result=1
# a=int(input("Enter the number :"))
# n=int(input("Enter the length"))
# for a in range(a,n):
#   result=result*a
# print(result)
                        
                        #EXAMPLE OF FACTORIAL
n=int(input("Enter the number"))
def fact(n):
    if n==1: 
     return 1
    else:
        return(n*fact(n-1)) 
print(fact(n))

