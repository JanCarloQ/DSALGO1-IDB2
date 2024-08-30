'''
# this is a comment
x = 1
y = 2.0
z = x * y
print ("1 times 2.0 =",z,"\nThis is a test for my python program")
print("This is another line")
userInput = input("how old are you?")
print(userInput, "years old")
userInput2 = input("Enter a number: ")
sum = int(userInput) + int(userInput2)
print("the sum is ",sum)
'''


'''
import math
print("How much is your money?")
Money= float(input())
Wiis = 100
print("you could only afford",int(math.floor(Money)/Wiis), "Nintendo Wii's")
print("you will need an additional", Wiis - (int(Money) % int(Wiis)),"to buy another Wii's")
'''
'''
factorial = 1
userInput = int(input("Enter your number: "))
for i in range(1, userInput+1):
    factorial = factorial*i
print("The factorial of",userInput,"is",factorial)
'''
ArrayList = []
userInput = int(input("Enter your number: "))
for i in range(1, userInput+1):
    if userInput % i == 0:
        ArrayList.append(i)
        print(i)
print("the factors of", i,"are:",ArrayList)



