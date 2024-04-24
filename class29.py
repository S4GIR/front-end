#IN THIS CLASS WE ARE GOING TO DISCUSS ABOUT THE FINALLY KEYWORD
#FINALLY:- Any satatement which is written finally keyword always executed.
                    
                    #EXAMPLE
def fun1():
    try:
        a=[1,3,5,7,9]
        i=int(input("Enter the index: "))
        print(a[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("I am always executed ")

x=fun1()
print(x)
  #Note:- In above program the print function written in finally always 
  #ecexute even if programm get any error or not