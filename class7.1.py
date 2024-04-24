
print("According to current time in your system. We are greeting you!!!!!!")
import time 
now =time.strftime("%H:%M:%S")
print(now)
now =int(time.strftime("%H"))
if now<12:
    print(" A VERY WARM!!!GOOD MORNING")
elif now>=12:
    print(" A VERY WARM!!!GOOD AFTERNOON")
elif now>=16:
    print("A VERY WARM!!!GOOD EVENING")
elif now>=16 and now<24:
    print("GOOD NIGHT AND HAVE A 'SWEET' DREAM!!!!!")