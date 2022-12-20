# CIS115
# Ch3: Decision Structures and Boolean Logic


# ------- Problem #1: if statement -------
# Step 1: Input whether it is cold outside or not (Yes or No)
cold = input("Is it cold?(yes or no)\n")
  

# Step 2: If it is cold, output "Wear a coat". Otherwise, do nothing.
if cold == "yes":
  print("Wear a coat")





# ------- Problem #2: Relational Operators -------
x = 1
y = 5
z = 2

print(x > y)
print(z <= y)





# ------- Problem #3: Equality/Inequality Operators -------
a = 2
b = 4
c = 4

print(a == b)
print(b == c)
print(a != b)
print(a != c)




# ------- Problem #4: if-else statement -------
# Step 1: Input a user's age (hint: convert to an integer)

age = input("Enter Age: ")
age2 = int(age)


# Step 2: If user is less than 18, output "Not eligible to vote."
# Otherwise, output "Voter!"
if age2 < 18:
    print("Not eleigble to vote.")
else:
    print("Voter!")





# ------- Problem #5: string comparisons -------
# Step 1: Input a word.
# Step #2: If the word is equal to "JACKPOT", output "You win!". Otherwise, output "You lose."
word = input("Type your word: ")

if word == "Jackpot":
    print("You win!")
else:
    print("You lose.")







# CHALLENGE PROBLEMS

# Problem #1: Input a user's age and their friend's age. Output which person is oldest (hint: use relational operators).
age = int(input("Please enter age: "))
friend_age = int(input("Please enter friends age: "))
if age > friend_age:
  print("You are older than your friend")
else:
  print("Your friend is older than you")




# Problem #2: Input two words and store in two separate variables.
# If both words are the same, output "Match!". Otherwise, output "Different".
word_one = input("Enter a word: " )
word_two = input("Enter another word: ")

if word_one == word_two:
  print("Match!")
else:
  print("Different")






# Problem #3: Input a user's amount of hours worked this week. Input the expected hours worked.
# Determine if the user worked enough hours and output an appropriate message.
# Calculate the total amount earned if the user is paid $15/hour. Output the total earned.

hours_worked = int(input("How many hours did you work?: "))
expected_hours = int(input("Enter expected hours worked"))

if hours_worked >= 40:
  print("You have worked enough!")


earned = hours_worked * 15
print("You earned $",earned)



# Problem #4: Input three numbers. Write a program that will evaluate which number is the
# maximum number using relational operators (<, >, <=, >=).

number1 = int(input("Please enter number 1\n"))
number2 = int(input("Please enter number 2\n"))
number3 = int(input("Please enter number 3\n"))

if (number1 > number2) and (number2> number3):
    print("Maximum number", number1)
elif (number2 > number1) and (number2> number3):
    print ("Maximum number", number2)
elif (number3 > number1) and (number3> number2):
    print ("Maximum number", number3)
elif (number1 == number2) and (number2 == number3):
    print("Equal")
else:
    print("Error")
