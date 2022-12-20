# CIS115
# Ch7: Lists & Tuples
#Kyle Metcalf CIS-115 10/27
#lists can be changed - they are mutable

# ------- Problem #0 -------
for num in [0, 1, 2, 3, 4, 5]:
    print(num)


# ------- Problem #1 -------
first_programmer = 'Ada Lovelace'
num_languages = 700
year_digital_computer = 1833
first_laptop_price = 2000

# Step 1: Let's create a list, named my_list, with the variables above.
# Lovelace was the first computer programmer; there are over 700 programming languages; 1833 was the first year the digital computer was invented by Charles Babbage; price of first laptop built in 1981 by Adam Osborne (named “Osborne 1”)
my_list = [first_programmer, num_languages, year_digital_computer, first_laptop_price]


# Step 2: Write a for loop to loop through my_list and print each item
for x in my_list:
    print(x)

#outputs the 'Ada Lovelace'
print(my_list)


# ------- Problem #2 -------
# Step 1: Create a list of the range of numbers from 0 to 5
# Hint: use the list() function 
num = list(range(6))
print(num)


# * can be used as a repition operator, to indicate how many time value should be repeated
numbers = [1,2,3]*2    
print(numbers [0]* 5)
print(numbers)

my_list = ["a","b","c"]
#           0   1   2
#           -3  -2  -1
print(my_list[0])
print(my_list[-1])


# ------- Problem #3 -------
# Step 1: Create a list with five 1s

number_list = [1]*5
print(number_list)


#write a for loop to print profit for each day
days = ['Mon','Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
profit = ['1500','500','625','900','875','1100', '375']

##index = 0
##for day in days:
##    print(days, profit[index])
##    index = index + 1

for index in range(len(days)):
    print(days[index], profit[index])

    
#print(list(range(len(profits)))) prints an indexed list    
##your_list. index("Value" we want to search for") no quotes around number

your_list = [2022,"SCC", 3.141715]




your_list[0] = "Eudaimonia"
print(your_list)

# ------- Problem #4 -------
avg_temps_pinehurst_nc = [54, 57, 64, 74, 81, 88, 90, 88, 82, 73, 64, 56]  

# Step 1: Output the first element, third element, and last element of the avg_temps_pinehurst_nc list

print(avg_temps_pinehurst_nc[0],avg_temps_pinehurst_nc[2],avg_temps_pinehurst_nc[-1])



# ------- Problem #5 -------
# Step 1: Create your_list with any elements you choose
greek_gods = ["Zues", "Hades", "Posiden","Artemis","Ares"]

# Step 2: Print the length of your_list and the index of one element in your_list

print(len(greek_gods))
# Step 3: Change the first element in your_list to your name
greek_gods[0] = "Kyle"

# Step 4: Concatenate your_list with my_list and output the resulting list

philos = ["Plato", "Socrates", "Aristotle"]

new_list = philos + greek_gods
print(new_list)


# ------- Problem #6 -------
# Step 1: Input a temperature

temp = int(input("Please enter temperature"))

# Step 2: Check if temperature is in the avg_temps_pinehurst_nc list
avg_temps_pinehurst_nc = [54, 57, 64, 74, 81, 88, 90, 88, 82, 73, 64, 56]  

if temp in avg_temps_pinehurst_nc:
    print(temp)
#theres also a "not in"


# Challenge: How might we check if there are temperatures less than the input temperature?

for i in avg_temps_pinehurst_nc:
    if i <= temp:
        print(i)
    else: print("Too Hot\n")


#normalization of data, find max value, divide everything in list by max value , the scale will go from 0  - 1
# the other sequence are tuples , strings are also sequences
#strings arent mutable like listss ex .append , print(mylist[0] == "e")


# ------- Problem #7 -------
# Step 1: Slice the avg_temps_pinehurst_nc list to
# output the temperatures for the months of spring (March - May)

avg_temps_pinehurst_nc = [54, 57, 64, 74, 81, 88, 90, 88, 82, 73, 64, 56]  

print(avg_temps_pinehurst_nc[2:5:])


# CHALLENGE PROBLEMS

# Problem #1: Design a program that asks the user to enter a store’s sales for each day of the week.
# The amounts should be stored in a list. Use a loop to calculate the total sales for the week and 
# display the result.

profits = []

again = 'y'

while again == 'y':

    sale = int(input("Enter sales\n"))
    profits.append(sale)
    print('Do you want to add another sale?')
     
    again = input('y = yes, anything else = no: ')
    print()
    
total_profits = sum(profits)

print('Total profit',total_profits)


    

# Problem #2: Create a list of names. Write code that determines 
# whether your name is in the names list. If it is, display the message 'Hello [your name]'. 
# Otherwise, display the message 'No [your name]'.
looking_for_name = input("Enter name you're looking for\n")

list_of_names = ["John","Jerard","Sarah","Sammy","Zoastra","Hermes","Thoth","Kyle"]

if looking_for_name in list_of_names:
    print(looking_for_name, "is in the list")



# Problem #3: Create list1 to store a list of integers. Write a statement
# to create a second list containing the squares of the elements of list1.
# used  py -3 -m pip install numpy

import numpy 
 
integers = [7 ,6 ,4 ,9 , 3]
print(integers)
print(numpy.array(integers)**2)

# Problem #4: Natural Language Toolkit (NLTK) Text Files
# Import nltk module (https://www.nltk.org/book/ch01.html)

import nltk 

# Download Gutenberg corpus (http://www.gutenberg.org/)
nltk.download('gutenberg')  

# Print list of all texts available from Gutenberg corpus
print('Texts: ', nltk.corpus.gutenberg.fileids())

# Select a text file from the list of 'Texts' above, and assign to the filename variable below as a string
filename = 'carroll-alice.txt'

text = nltk.corpus.gutenberg.words(filename)


# create a list of the words in your chosen file
book_1 = list(text)
# print the length of text_list
print(len(book_1))

# slice the text_list and print the first 50 elements

print(book_1[:51:])

# Problem #5: Sort Your List
integers = [7 ,6 ,4 ,9 , 3]
print(integers)
integers.sort()
print(integers)
# 1. Store 3 numbers in a tuple
first_tuple = (9,4,1)
# 2. Create a list and add each number to your list
tuple_converted_to_list = list(first_tuple)
print(tuple_converted_to_list)
# 3. Try to sort the list in ascending order as efficiently as possible
tuple_converted_to_list.sort()
print(tuple_converted_to_list)

#A good example of using a tuple would be latitude and longitude
#this would be a list you would not like to change

# Problem #6
# Given the following services and corresponding price, store this information in an appropriate container. 
# oil change -- $35
# tire rotation -- $19
# car wash -- $7
# Write a program that accepts from input a request of an automobile service
# and returns the corresponding price and service requested.
# If a user requests a service not listed above, output an error message.

service_list =["Oil change $35","Tire rotation $19","Car Wash $7"]

service = input("Please enter service: ")

if service == "oil change":
    print(service_list[0])
elif service == "tire rotation":
    print(service_list[1])
elif service == "car wash":
    print(service_list[2])
else:
    print("Not a service we provide")



# Problem #7
# Input 5 user's names and their age. Store each name and age in a user_list
# that is stored inside of a group_list. Input a name to search on and search
# through the group_list to determine if the name is in the group_list.
# Challenge: Is the user eligible to vote?
ages = 5

names_list=[]
ages_list=[]
for i in range(ages):
    user_name = input("Enter name\n")
    names_list.append(user_name)
    user_age = int(input("Enter age\n"))
    ages_list.append(user_age)
name_search = input("Look up a name\n")
if name_search in names_list:
                   print(name_search,"is in the list")
elif name_search not in names_list:
                   print(name_search,"is not in the list")

