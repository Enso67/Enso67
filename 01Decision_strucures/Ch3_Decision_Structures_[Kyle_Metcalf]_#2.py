# CIS115
# Ch3: Decision Structures and Boolean Logic


# ------- Problem #1: Nested if-else statements -------
# Step 1: Input a person's age and input if they have a driver's license (Yes or No)

age = int(input("What is your age?\n"))

# Step 2: If person's age >= 16
if age >= 16:

    # Step 3: If person has a driver's license, output "Eligible to drive"

    license = input("Do you have a license? (Yes or No)\n")
    if license == "Yes":
          print("Eligible to drive")
    # Step 4: Otherwise, output "No license"
    else:
        print("No license")

# Step 5: Otherwise, output "Too young"

else:
    print("Too young")







# ------- Problem #2: if-elif-else statement -------
# Write a program that accepts a grade (integer) as input and determines the corresponding letter grade
# using if-elif-else branching, equality operators, and relational operators.

# Step 1: Input a student's grade
grade = int(input("Enter grade\n"))

# Step 2: If student's grade is in the range of an 'A', output 'A'

if grade >= 90:
    print("A")

# Step 3: Elif student's grade is in the range of a 'B', output 'B'
elif grade >= 80:
    print("B")


# Step 4: Elif student's grade is in the range of a 'C', output 'C'
elif grade >= 70:
    print("C")


# Step 5: Elif student's grade is in the range of a 'D', output 'D'

elif grade >=60:
    print("D")

# Step 6: Else output "Did not pass"
else:
    print("Did not pass")







# ------- Problem #3: Logical Operators -------
# Write an if-else statement that displays 'Speed is normal' if the speed variable is 
# within the range of 24 to 56. If the speed variable’s value is outside this range, display 
# 'Speed is abnormal'.

# Step 1: Input a speed
speed = int(input("Enter Speed: "))

# Step 2: If speed is within range of 24 to 56, output "Speed is normal"

if speed >= 24 and speed <= 56:
            print("Speed is normal")
            

# Step 3: Otherwise output "Speed is abnormal"

else:
    print("Speed is abnormal")







# CHALLENGE PROBLEMS

# Problem #1: Automotive Services
# Given the following services and corresponding price,
# oil change -- $35
# tire rotation -- $19
# car wash -- $7
# Write a program that accepts from input a request of an automobile service
# and returns the corresponding price. If a user requests a service not listed
# above, output an error message.

service = input("Please enter service: ")

if service == "oil change":
    print("Oil Change $35")
elif service == "tire rotation":
    print("Tire rotation $19")
elif service == "car wash":
    print("Car wash $7")
else:
    print("Not a service we provide")






# Problem #2: Golf Scores
# Golf scores have special names that vary with each hole and are based on the actual number of strokes taken compared to par.
# "Eagle": number of strokes is two less than par
# "Birdie": number of strokes is one less than par
# "Par": number of strokes equals par
# "Bogey": number of strokes is one more than par
# Write a program that accepts two integers from input that represent 1) par and 2) the number of strokes taken.
# Print the appropriate score name. If par is not 3, 4, or 5, print "Error".



par = int(input("Enter Par: "))
strokes = int(input("Enter Strokes: "))

if strokes == par - 2:
    print("Eagle")
elif strokes == par -1:
    print("Birdie")
elif strokes == par:
    print("Par")
elif strokes == par + 1:
    print("Bogey")
elif strokes == par + 2:
    print("Double Bogey")
elif strokes == par + 3:
    print("Tripple Bogey")

if par < 3 or par > 7:
    print("Error")





# Problem #3: Primary Colors
# The colors red, blue, and yellow are known as the primary colors because they cannot 
# be made by mixing other colors. When you mix two primary colors, you get a secondary 
# color, as shown here:
# When you mix red and blue, you get purple.
# When you mix red and yellow, you get orange.
# When you mix blue and yellow, you get green.
# Design a program that prompts the user to enter the names of two primary colors to mix. If 
# the user enters anything other than “red,” “blue,” or “yellow,” the program should display 
# an error message. Otherwise, the program should display the name of the secondary color 
# that results.


primary_one = input("Please enter color one (red, blue or yellow): ")
primary_two = input("Please enter color two (red, blue or yellow): ")

if ((primary_one == "red" or primary_one == "blue") and (primary_two == "red" or primary_two == "blue")):
    print("Purple")
    
elif ((primary_one == "red" or primary_one == "yellow") and (primary_two == "red" or primary_two == "yellow")):
    print("Orange")
elif ((primary_one == "blue" or primary_one == "yellow") and (primary_two == "blue" or primary_two == "yellow")):
    print("Green")
else:
    print("Error")


# Problem #4: Blackjack
# Store names of player and dealer in variables
# Ask how many rounds player would like to play
# Deal two cards to player and dealer and keep track of both cards dealt using input()
# Create counter for player and dealer: counter1, counter2
# Increment counters by value of cards dealt for dealer and player
# Print counts for player and dealer
# Check if player wants to hit or stand and if hit, deal a card to player
# Repeat once more
# Check if dealer has less than 17 and if so, deal a card to dealer
# Repeat once more 
# Increment counters by value of cards dealt for dealer and player
# Print counts for player and dealer
# Use if-else statements to compare dealer with player and output "The winner is ..."

import random

deck_of_cards = ["King of Hearts", "Queen of Hearts", "Jack of Hearts", "10 of Hearts", "9 of Hearts", "8 of Hearts", "7 of Hearts", "6 of Hearts", "5 of Hearts", "4 of Hearts", "3 of Hearts", "2 of Hearts", "Ace of Hearts", "King of Spades", "Queen of Spades", "Jack of Spades", "10 of Spades", "9 of Spades", "8 of Spades", "7 of Spades", "6 of Spades", "5 of Spades", "4 of Spades", "3 of Spades", "2 of Spades", "Ace of Spades", "King of Clubs", "Queen of Clubs", "Jack of Clubs", "10 of Clubs", "9 of Clubs", "8 of Clubs", "7 of Clubs", "6 of Clubs", "5 of Clubs", "4 of Clubs", "3 of Clubs", "2 of Clubs", "Ace of Clubs", "King of Diamonds", "Queen of Diamonds", "Jack of Diamonds", "10 of Diamonds", "9 of Diamonds", "8 of Diamonds", "7 of Diamonds", "6 of Diamonds", "5 of Diamonds", "4 of Diamonds", "3 of Diamonds", "2 of Diamonds", "Ace of Diamonds"]

random_card = random.choice(deck_of_cards)
print(random_card)

'''
random_card = input("Enter card\n")
counter = 0

if random_card == "King of Hearts" or random_card == "Queen of Hearts" or random_card == "Jack of Hearts" or random_card == "10 of Hearts" or random_card == "King of Spades" or random_card == "Queen of Spades" or random_card == "Jack of Spades" or random_card == "10 of Spades" or random_card == "King of Spades" or random_card == "Queen of Spades" or random_card == "Jack of Spades" or random_card == "10 of Spades" or random_card == "King of Clubs" or random_card == "Queen of Clubs" or random_card == "Jack of Clubs" or random_card == "10 of Clubs":
    counter += 10
elif random_card == "9 of Hearts" or random_card == "9 of Spades" or random_card == "9 of Clubs" or "9 of Diamonds":
    counter += 9
elif random_card == "8 of Hearts" or random_card == "8 of Spades"or random_card == "8 of Clubs"or "8 of Diamonds":
    counter += 8
elif random_card == "7 of Hearts" or random_card == "7 of Spades" or random_card == "7 of Clubs" or random_card == "7 of Diamonds":
    counter += 7
elif random_card == "6 of Hearts" or random_card == "6 of Spades" or random_card == "6 of Clubs" or random_card == "6 of Diamonds":
    counter += 6
elif random_card == "5 of Hearts" or random_card == "5 of Spades" or random_card == "5 of Clubs" or random_card == "5 of Diamonds":
    counter += 5
elif random_card == "4 of Hearts" or random_card == "4 of Spades" or random_card == "4 of Clubs" or random_card == "4 of Diamonds":
    counter += 4
elif random_card == "3 of Hearts" or random_card == "3 of Spades" or random_card == "3 of Clubs" or random_card == "3 of Diamonds":
    counter += 3
elif random_card == "2 of Hearts" or random_card == "2 of Spades" or random_card == "2 of Clubs" or random_card == "2 of Diamonds":
    counter += 2
elif random_card == "Ace of Hearts" or random_card == "Ace of Spades" or random_card == "Ace of Clubs" or random_card == "Ace of Diamonds":
    counter += 1

print(counter)




name_one = input("Enter player : ")
name_two = input("Dealer name: ")

round_total = int(input("How many rounds would you like to play?\n")
                



hit = input("Would you like to hit? y or n")
while hit == "yes":

'''


