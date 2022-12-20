'''
#while loop lets user enter num, num x 10, loop iterates as long as input < 100
total = 0
mult = 10
num = int(input("Enter number"))
while num < 100:
    total = num * mult
    print(total)
    num = int(input("Enter number"))

else:
    print("Enter number less than 100")


#ask user for two numbers

num1 = int(input("Please enter num 1"))
num2 = int(input("Please enter num 2"))

# add numbers and display sum
total = num1 + num2
print("$",total)

#ask user if theyd like to perform again

ans = input("Would you like add again?")
#loop
while ans == "yes":
    num1 = int(input("Please enter num 1"))
    num2 = int(input("Please enter num 2"))

    # add numbers and display sum
    total = num1 + num2
    print("$",total)
    ans = input("Would you like add again?")
# terminate
else:
    print("End")

#print 0, 10 - 1000 include 1001 to get to 1000
for num in range(0,1001,10):
    print(num)
'''
#keep a running total

sum = 0

for num in range (0,10):
    number = int(input("Enter number"))
    sum +=  number
    print(sum)
