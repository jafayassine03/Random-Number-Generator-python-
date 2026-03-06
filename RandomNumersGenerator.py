import random
print(" YOU WILL PUT THE MIN NUMBER AND MAX NUMBER AND THE COPMUTER WILL PICK A RANDOM NUMBER BETWEEN THE MIN AND MAX NUMBER YOU ENTERED ")
a = int(input("Enter the min number: "))
b = int(input("Enter the max number: "))
if b<=a :
    print(" the max number must be bigger the the min")
else :
    print(random.randint(a,b))
