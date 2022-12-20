# CIS115
# Ch4: For Loops

# ------- Problem #0 -------
for num in [0, 1, 2, 3, 4, 5]:
    print(num)


# ------- Problem #1 -------
my_list = ["Ace", "King", "Queen"]

# Step 1: Write a for loop to loop through my_list
for card in my_list:
    
    # Step 2: Print each item
    print(card)




# ------- Problem #2 -------
# Step 1: Create your_list
big_five = ["openness", "conscientousness", "extraversion", "agreeableness", "neroticism"]

# Step 2: Write a for loop to loop through your_list
for trait in big_five:


# Step 3: Print each item
    print(trait)



# ------- Problem #3 -------
for number in range(6):
    print(number)




# ------- Problem #4 -------
# Step 1: Ask user for a number of loops
loops = int(input("Please input number of loops"))

# Step #2: Write a for loop to loop through the range of numbers input
for loop in range(loops):

    # Step 3: Print each number in the range
    print(loop)

#might not have a list - if you use a range

# ------- Problem #5 -------
# Step 1: Ask user for a number of loops
num_loops = int(input("Please input number of loops"))

# Step #2: Write a for loop to loop through every other number in the
# range of numbers input, starting with 1 
for num in range(1,num_loops,2):

    # Step 3: Print the square of each number (raise to the power of 2)
    print(num**2)


## range(start,stop, count)


start = int(input("Enter start number\n"))
stop = int(input("Enter end number\n"))


for num in range(start,stop+1,1):
    print(num)

total = 0
total_tests = int(input("Enter total number of tests\n"))

for num in range(0,total_tests,1):
    test_scores = int(input("Enter test scores\n"))
    total = total + test_scores

average = total // total_tests
print(average)


##tuition = 8000
##interest = .03
##years = int(input("Enter years")
##for num in range(0,years)
##    total = college_tuition * interest
    

#we ad an extra +1 to include what the user input

# CHALLENGE PROBLEMS

# Problem #1: Output the numbers 1 through 10


for number in range(1,11):
    print(number)



# Problem #2: Output all odd numbers from 1 to 10,
# then output all even numbers from 1 to 10

for number in range(1,11,2):
    print(number)
    
for num in range(2,11,2):
    print(num)



# Problem #3: You are asked to calculate the miles per hour (MPH)
# of a European car with a speedometer in kilometers per hour (KPH).
# Using the formula,MPH = KPH * 0.6214, calculate the MPH for
# speeds from 60 KPH to 130 KPH in increments of 10.
# Output the speed in MPH and KPH.

start_speed = 60
end_speed = 131
increment = 10
conversion = 0.6214


for KPH in range(60,131,10):
    MPH = KPH * 0.6214
    print(MPH)


# Problem #4: Input a starting number and input a stopping number that is
# less than the starting number. Loop through this range of numbers and
# make sure to output the numbers from highest to lowest.
start = int(input("please enter starting number"))
stop = int(input("please enter a stop number less than start"))

for num in range(start,stop,-1):
    print(num)




# Problem #5: Write a loop that asks the user to enter a number.
# The loop should iterate 10 times and 
# keep a running total of the numbers entered.
sum = 0

for num in range(0,10):
    number = int(input("Enter number"))
    sum += number
    print(sum, num+1)


# Problem #6: Write a loop that calculates the total of the following series of numbers:
# 1/30 + 2/29 + 3/28 + ... + 30/1
full = 0

for num in range(1,31,1):
        print(num,"/",31-num)
        total = num / (31-num)
        print(total,"after dividing")
        full = full + total
        print(full,"Total")

#loop lab
'''

#in class code
tuition = 8000
increase = 0.03
years =int(input("Enter years\n"))
for i in range(0,years):
    tuition *= (1 + increase)

    print("Year", i+1 , "- projected tuition: $", tuition)

# you run through the list in the for loop but also run through the numbers in list



#my code

total = 0
total_tests = int(input("Enter total number of tests\n"))

for num in range(total_tests):
    test_scores = int(input("Enter test scores\n"))
    total += test_scores

average = total // total_tests
print(average)

Exampe of nested loop  - clock - hours - minutes - seconds

'''
#outer loop 3 times - inner loop [a, b, c,]
list_ = ["a","b","c"]
for num in range(3):
    for letter in list_:
        print(num), print(letter)

#snake - game - in  python -by ganesh -kavhar

speed = int(input("Please enter speed\n"))

hours = int(input("Please enter time\n"))

for num in range(0,hours):
    
   
    distance = speed * hours
    print(distance,"Miles Traveled")


