# CIS115
# Ch7: Lists & Tuples

# ------- Problem #0 -------
avg_temps_p_nc = [54, 64, 74, 81, 88, 90, 88, 82, 73, 56]
months = ["Jan", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Dec"]

# Step 1: Find the number of temperatures in avg_temps_p_nc
print(len(avg_temps_p_nc))

# Step 2: Find the month with the temperature 88
i = avg_temps_p_nc.index(88)
print(i)
print(months[i])

#index method will only output the very first index, you recursivly slice your list

# ------- Problem #1 -------
# Step 1: Input the year of the collected temperatures
year_temp = int(input("Enter year"))


# Step 2: Append the year to the end of the list using the .append(element) method

avg_temps_p_nc.append(year_temp)
print(avg_temps_p_nc)

#can only append one thing at a time
#list can be added together using (+) plus

# ------- Problem #2 -------
# Step 1: Input an average temperature for February
feb_temp = int(input("Please enter temp\n"))


# Step 2: Insert the Feb temperature in the list
# at the appropriate index using the .insert(index, element) method
# and print the list
avg_temps_p_nc.insert(1,feb_temp)
print(avg_temps_p_nc)


# Step 3: Repeat for November

nov = int(input("Enter temp\n"))
avg_temps_p_nc.insert(10,nov)


# ------- Problem #3 -------
# Step 1: Find the min temperature using min()
print(min(avg_temps_p_nc))


# Step 2: Find the max temperature using max()
print(max(avg_temps_p_nc))



# ------- Problem #4 -------
# Step 1: Create a copy of avg_temps_p_nc
avg_temps_copy = []  # empty list
#we can concatonate this list with the original list
avg_temps_copy += avg_temps_p_nc 

avg_temps_copy = avg_temps_p_nc.copy()

print(avg_temps_copy)
print(avg_temps_p_nc)
# Step 2: Sort the copied list in ascending order using the .sort() method
avg_temps_copy.sort()
print(avg_temps_copy)


# ------- Problem #5 -------
# Step 1: Remove the temperature 88 from avg_temps_p_nc
# using the .remove(element) method
avg_temps_p_nc.remove(88)
#if we were to remove a string we need to make sure its in the same format "88" if it was string

print(avg_temps_p_nc)

# ------- Problem #6 -------
# Step 1: Reverse the order of the copied list to be in descending order
# using the .reverse() method
avg_temps_copy.reverse()

print(avg_temps_copy)

# ------- Problem #7 -------
# Step 1: Delete the last element in avg_temps_p_nc using the del statement

del avg_temps_p_nc[-1]
#deleting last element
#best for deleting index value
#can also be done with remove
#avg_temps_p_nc.remove(avg_temps_p_nc[-1])





# CHALLENGE PROBLEMS
# ------- Problem #1: List Builder --------
# Create a list of data points from input using a while loop.
# 1. Accept an item from input to add to a list (e.g. grades, scores, prices)
# 2. Create an empty list
# 3. While no undesired input is entered, continue appending items to
# your list and accepting from input new items to add 
# 4. Print the final list

shopping_list = []

ans = input("Would you like to make a groccery list? (Type yes to continue)\n")

while ans == "yes":
    grocceries = input("Enter shoppping item\n")

    shopping_list.append(grocceries)
    
    ans = input("Would you like to add another item\n")
else:
    print(shopping_list)




# ------- Problem #2: Larger Than --------
# Create a list of numbers using the range() function. Write a program to output
# all numbers in the list that are larger than the average number in the list.
# Repeat for the max number in the list.
length = int(input("Enter length of list\n"))

list_range = list(range(1,length+1))
print(list_range)

avg = sum(list_range) // len(list_range)
#delete items larger than avg
del list_range[0:avg]
print(list_range,"All #'s larger than avg")

#repeat: print all # greater than max
del list_range[0:max(list_range)-1]

print(list_range,"All #s greater than max")

# ------- Problem #3: List Fixer --------
# Given the bug_list list below, replace all occurrences of
# "Sanhdills" with the correct spelling, "Sandhills".
bug_list = ["Montgomery", "Richmond", "Sanhdills", "Rockingham", "Sanhdills", "Richmond", "Sanhdills", "Sanhdills", "Sanhdills", "Montgomery"]

for i in range(len(bug_list)):

    if bug_list[i] == "Sanhdills":
        bug_list[i] = "Sandhills"

print(bug_list)


# ------- Problem #4: Lo Shu Magic Square (2x2) --------
# Build a list of two lists (2-dimensional list) to represent a 3 x 3 grid. See example below.
# The grid must contain the numbers 1 through 4 exactly.
# Check that the sum of the rows, columns, and diagonals of the grid
# add up to the same number.
#nested list add one more
#ask user what number for 9 input
#you check sum of the rows column and diagnal
list1 = []
list2 = []
list3 = []
grid = [list1, list2, list3]

answer = input("Would you like to play\n")

while answer == "yes":
    ans1 = int(input("Enter #(1-9)\n"))
    list1.append(ans1)
    ans2 = int(input("Enter #(1-9)\n"))
    list1.append(ans2)
    ans3 = int(input("Enter #(1-9)\n"))
    list1.append(ans3)
    ans4 = int(input("Enter #(1-9)\n"))
    list2.append(ans4)
    ans5 = int(input("Enter #(1-9)\n"))
    list2.append(ans5)
    ans6 = int(input("Enter #(1-9)\n"))
    list2.append(ans6)
    ans7 = int(input("Enter #(1-9)\n"))
    list3.append(ans7)
    ans8 = int(input("Enter #(1-9)\n"))
    list3.append(ans8)
    ans9 = int(input("Enter #(1-9)\n"))
    list3.append(ans9)
    break
print(list1)
print(list2)
print(list3)

#check sum of the rows
for i in range(len(grid)):
    if sum(list1) and sum(list2) and sum(list3) == 15:
        print("you win!")
else:
    print("You lose")

##list practice
#Challnge 11/03 CIS 115
#using lists to create sets of information
#there is also a unique function
# "set(grades) will give you the same


grades = [90,75,87,93,95,100,75,65]

unique = []

duplicate = []
for g in grades:
#check if g is in unique
    if g not in unique:
        unique.append(g)
    else:
        duplicate.append(g)
print(unique)
print(duplicate)


# ------- Problem #5: Wordman -------
# Input a word from the user. Build a list with the letters of the word (hint: use list()).
# Output the length of the word. Allow the user to guess 5 letters and
# output whether the letter is in the list. Allow the user 5 guesses at the word.
# If the user guesses correctly, output "Winner". Otherwise, output "You lose".



    






# ------- Problem #6: Blackjack --------
# Store names of player and dealer in variables.
# Ask how many rounds player would like to play and repeat game for specified number of rounds.
# Store cards in a list.
# Using the random.choice() function from the random module (imported below), 
# choose (aka deal) two cards to player and dealer from list of cards
# and keep track of both cards dealt.
# Create counter for player and dealer: counter1, counter2
# Increment counters by value of cards dealt for dealer and player.
# Print counts for player and dealer.
# While player wants to hit, deal a card to player.
# While dealer has less than 17, deal a card to dealer.
# Increment counters by value of cards dealt for player and dealer.
# Print counts for player and dealer.
# Use if-else statements to compare dealer with player and output "The winner is ...".



