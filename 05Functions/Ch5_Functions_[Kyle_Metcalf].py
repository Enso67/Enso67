# Ch5_Functions_[Kyle_Metcalf].py
# Author: Prof. Parsons
# Last Updated: November 29, 2022
# Program demonstrates examples of functions

#Void functions usuallly print out info

"""Problem 1: Print Funny Face

Call the print_face function to output a funny face.
"""

# function definition
def print_face():
  print(": )")


# function call

print_face()

"""Problem 2: Print Message

Define a print_message function to output a message. Call the print_message
function.
"""
# function definition

def print_message():
  print("Taco's are great on Tuesday.\n")

# function call

print_message()


"""Problem 3: Print Different Funny Faces

Call the print_face function to output a funny face based on selection argument.
"""


# function definition
def print_face(selection):
  if selection == 0:
    print(": )")
  elif selection == 1:
    print("; D")
  elif selection == 2:
    print(": P")
  else:
    print(" ")


# function call
print_face(0)



"""Problem 4: Average List

Call the avg_list function to calculate the average of my_list and print theaverage.
"""

# function definition
def avg_list(list_input):
  list_avg = sum(list_input)/len(list_input)
  return list_avg


# main program
my_list = [1, 2, 3, 4, 5]

# function call




"""Problem 5: Tip Calculator

Write a function called tip_calc to calculate the tip of a restaurant bill.
The function has 2 parameters: bill and tip percentage.
Return the tip from the function.
"""


# function definition
def tip_calc(bill,tip_percentage):
  tip_total = bill * tip_percentage
  return tip_total
  
try:
  tip_percentage = float(input("Enter tip percentage"))
  bill = float(input("Enter bill amount."))
  print("$",tip_calc(bill,tip_percentage),"will be your tip.")
except ValueError:
  print("Enter valid Value")



'''
# main program
total_bill = float(input())
tip10 = tip_calc(total_bill, 0.10)
tip15 = tip_calc(total_bill, 0.15)
tip20 = tip_calc(total_bill, 0.20)
print("tip 10%: ", tip10, "\ntip 15%: ", tip15, "\ntip 20%: ", tip20)
'''

# Challenge 1: How can we calculate a 15% tip for multiple bill amounts using a loop?
#print("--15% Tip---")



# Challenge 2: How can we calculate multiple tip amounts for a bill of $25 using a loop?
#print("-- $25 bill --")





#Problem 6: Area of Circle


#> Define a function, circle_area(), to compute the area of a circle for anysize radius.
#eturn the area. Use math.pi from the math module.
import math
# Code from GPT
def calculate_area_of_circle(radius):
    area = 3.14 * (radius ** 2)
    return area
try:
  radius_to_calc = float(input("Enter radius"))
  print("The area if the circle is",calculate_area_of_circle(radius_to_calc))
except ValueError:
  print("Enter valid value")


#> Call the function to test if it accurately calculates area for a radius argument of 9 (area is 254.469).


import math
# function definition




# main program





"""Problem 7: Distance Equator

Euclidean Distance: d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

> Define a function, dist(), to compute the Euclidean distance of two points
with coordinates x1, y1, x2, and y2, using the formula above.
Print the distance in the function.

> Call the function to test the computation and output the distance. 
"""

import math
# function definition




# main program




"""Problem 8: Letter Grade Calculator

> Define a function to calculate a student's final letter grade.
Name the function appropriately and consider all parameters needed
to be passed to the function.

> Call the function to test if it outputs the correct letter grade.
"""

# function definition




# main program





"""### Challenge Problems

Problem 1: Sales Tax for Groceries

> Given the code used to calculate a grocery bill (while loop from Ch.5:1-5), define a function, calc_sales_tax(), to calculate 5% sales tax for a grocery bill and return the new recomputed grocery bill that includes sales tax.

> Call the function calc_sales_tax at the end of the program and output the total bill that includes sales tax.
"""

# function definition






# main program 






"""Problem 2: Create a List

> Write a program whose input is two integers. 

> Define a function, create_list(), that takes the two input numbers, and returns a list containing the first integer and subsequent increments of 10 as long as the value is less than or equal to the second integer.
"""

# function definition




# main program

"""Problem 3: Caesar Cipher

Write a function to to encrypt a word using a Caesar cipher.
Print out the final encrypted word.


> Accept a word from input and store as variable *word_to_encode*

> Loop over each character in *word_to_encode* and: 

* encode the character as an integer (hint: use ord() function)

* apply Caesar cipher to encoded integer (shift integer)

* convert each encoded integer to an encrypted character (hint: use chr() function)
and concatenate to final word

> Print the final encrypted word
"""

# function definition


  



# main program






"""Problem 4: Palindrome Problem

Write a function called check_palindrome to evaluate if a word is a palindrome (word is spelled the same forward and backward, e.g. "anna", "bob", "racecar").
"""

# function definition





# main program




"""Problem 5: Yearly Savings

Write a function called yearly_savings to compute the future value (see equation below) of a specified principal amount and rate of interest generated once per year over a *range* of years.

FV = P(1 + (r/n))**nt

> FV: Future Value

> P: Principal (initial savings)

> r: rate of interest

> n: number of times paid per year

> t: number of years
"""

# function definition





# main program





"""**Blackjack**

* Store names of player and dealer in variables
* Ask how many rounds player would like to play
* Deal two cards to player and dealer and keep track of both cards dealt using input()
* Create counter for player and dealer: counter1, counter2
* Increment counters by value of cards dealt for dealer and player
* Print counts for player and dealer

* Accept input from player to hit or stand until they are satisfied with their cards. (Hint: use a while loop)
* While dealer has less than 17, deal a card to dealer
* Increment counters by value of cards dealt for dealer and player
* Print counts for player and dealer
* Use if-else statements to compare dealer with player and output "The winner is ..."
* Implement playing multiple rounds based on user input for desired number of rounds. Loop through each round and play Blackjack, using your existing code.


* Define functions for repeated code in your game. Consider using multiple functions for different tasks (e.g. dealing, hitting/standing, determining winner)

"""







