# CIS115
# Ch4: While Loops


# ------- Problem #1 -------
# Step 1: Ask user for input (Yes or No)
decision = input("Enter Yes or No")

# Step 2: While input is "Yes", output "keep looping". Otherwise, end program.

while decision == "Yes":
    print("Keep looping")
    decision = input("Enter Yes or No")



# ------- Problem #2 -------
# Step 1: Assign 40 to a variable named x
x = 40

# Step 2: While x is greater than 0, output x and output each multiple of 5 until 0

while x > 0:
    print(x)
    x = x - 5



#these two ae the exact same to add one
##sum = sum + 1
##sum += 1



# ------- Problem #3 -------
# Step 1: Input a word

word = input("Enter a word")
# Step #2: While the word is not equal to "JACKPOT", output "You lose!"
# and prompt the user for another guess. If guessed correctly, output "You win!".

while word != "JACKPOT":
    print("You lose!\n")
    word = input("Guess again\n")
else:
    print("You Win!")





# ------- Problem #4: -------
# Step 1: Input a user's age (hint: convert to an integer)
age = int(input("Please enter age\n"))

# Step 2: While the user is less than 18, output "Not eligible to vote."
# Prompt the user for the next age. When 18 or older, output "Voter!".


while age < 18:
    print("Not eligible to vote")
    age = int(input("Please enter another age\n"))
else:
    print("Eligable to vote")








# ------- Problem #5 -------
# Input a series of positive numbers. While the numbers are not negative, continue inputting numbers.
# As each new number is input, add the number to a total. Output the total at the end of the program.
Total = 0
number = float(input("Please enter positve numbers"))

while number > 0:
    Total += number
## total = total + num
    number = float(input("Please enter positve numbers"))

else:
    print(Total)
    
## what if we wanted to input negative numbers
## use print (Total)
##while num < 0:
##    total = total + num
##    num = int(input())
##print(total)






# CHALLENGE PROBLEMS

# Problem #1: Input a number. While the number is an even number,
# output the number and continue inputting a number.


number = int(input("Enter number\n"))
Even_or_odd = number%2


while Even_or_odd == 0:
    print("Even",number)
    number = int(input("Enter number\n"))
    Even_or_odd = number%2
else:
    print("Odd",number)



# Problem #2: Input the price of a grocery item. While the price is greater than 0,
# add the price to the total and continue inputting prices of grocery items. Output the total grocery bill.
price_total = 0
price = float(input("Enter price of grocery item"))

while price > 0:
    price_total += price
    price = float(input("Enter price of grocery item"))
else:
    print(price_total)





# Problem #3: Input the length of a field goal kicked. While the length is greater than 0,
# calculate the points awarded for each field goal and add it to the total. Output the total points.
# (hint: use the rules for the Fantasy Football problem from the Sept. 15 lecture)

total = 0

length = int(input("Enter length of field goal kicked\n"))

        
while length > 0:
    if length > 0 and length <= 39:
        points = 3
    elif length >= 40 and length <= 49:
        points = 4
    elif length >= 50:
        points = 5
    total += points
    length = int(input("Enter next length of field goal kicked\n"))
else:
    print (total,"Field goal points!")

# Problem #4: Input a monthly budget amount. Input monthly expense amounts.
# While expense amounts are greater than 0, add them to a total.
# Then compare the total to the monhly budget and ouput
# whether the user is over or under budget.
budget = int(input("Enter budget total\n"))

total_exp = 0
expenses = int(input("Enter expenses"))
while expenses > 0:
    #add total before getting expenses
    total_exp = expenses +total_exp
    expenses = int(input("Enter expenses"))
    
if budget > total_exp:
    print("Under budget")
elif budget>= total_exp:
    print("Over Budget")
print("$",total_exp,"Monthly Expenses","$",budget,"Budget Total")

#while loop to enter sales
keep_going = "y"
while keep_going == "y":
        sales = float(input("Enter total sales"))
        comm_rate = float(input("Enter comm_Rate"))
        commission = sales * comm_rate
        print(commission)
        keep_going = input("type y to continue")
else:
        print("End")

