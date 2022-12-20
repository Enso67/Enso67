# CIS115
#Ch9: Dictionaries and Sets


# ------- Problem #0 -------
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
profits = [1500, 500, 625, 900, 875, 1100, 375]

# Output the profits made on Thursday

#we want to wlays use inx
thurs = days.index('Thu')
print(profits[thurs])

# ------- Problem #1 -------
my_dictionary = {"King": 10, "Queen": 10, "Jack": 10, "Ten": 10, "Nine": 9}

# Step 1: Output the value of the Queen card
print(my_dictionary["Queen"])
#dict are unordered:cant be sorted - search and ref by keys
#key can be #s strings, tuples (immutable) No lists
      
# Step 2: Delete the Nine element from my_dictionary
del my_dictionary["Nine"]
      
#will delete the whole pair
#must always reference the key value

# Step 3: Output all remaining elements in my_dictionary
for key in my_dictionary:
      print(key, my_dictionary[key])
#have to call the dictionary at key value (Just like step 1)


# ------- Problem #2 -------
# Step 1: Create an empty dictionary
KAM = {}


# Step 2: Add the days and profits to the dictionary
# for Saturday and Sunday
KAM[days[5]] = profits[5]
#KAM[days.index["Sat"]] = profits[5]
#we set the key = value

KAM[days[6]] = profits[6]
print(KAM)
# Challenge: Add all the days and profits to the dictionary

for key in range(len(profits)):
    KAM[days[key]] = profits[key]


# ------- Problem #3 -------
# Step 1: Output the keys of the dictionary you created in #2
print(KAM.keys())
# Step 2: Output the values of the dictionary you created in #2

print(KAM)



# ------- Problem #4 -------
my_set = {1, 2, 3, 4, 5, 5, 5, 5}

# Output my_set
print(my_set)




# ------- Problem #5 -------
# Step #1: Create a set of temperatures and output the set
avg_temps_p_nc = set([54, 64, 74, 81, 88, 90, 88, 82, 73, 56])


# Step 2: Output the number of items in the set of temperatures

print(avg_temps_p_nc)




# CHALLENGE PROBLEMS

# Problem #1: Automotive Services
# Given the following services and corresponding price,
# store this information in an appropriate container.
#   oil change -- $35
#   tire rotation -- $19
#   car wash -- $7
# Write a program that accepts from input a request of an automobile service
# and returns the corresponding price. If a user requests a service not listed
# above, output an error message.




# Problem #2: Streaming Services
# services = ["Netflix", "Hulu", "Amazon Prime"]
# prices = [8.99, 11.99, 6.49]
# Store the services and prices in a dictionary by extracting them from the lists.
# Hint: don't create the dictionary manually.
# Print out the service and its corresponding price from the dictionary.




# Problem #3: Dictionary Challenge
# Write a program to:​
# Ask the user for the names and birth months of 3 friends ​
# Store each name and birth month in a dictionary
# Output the names of all friends whose birth month is in the second half of the year​






# Problem #4: Blackjack
# 1. Store names of player and dealer in variables
# 2. Ask how many rounds player would like to play and implement
#       your game to play the appropriate number of rounds
# 3. Store a deck of cards in an appropriate container
# 4. Using random.choice(deck), deal two cards to player and dealer
#       and keep track of both cards dealt. Make sure to import random
# 5. Create counter for player and dealer: counter1, counter2
# 6. Increment counters by value of cards dealt for dealer and player
# 7. Print counts for player and dealer
# 8. Continue to check if player wants to hit or stand and if hit, deal a card to player
# 9. Continue to check if dealer has less than 17 and if so, deal a card to dealer
# 10.Increment counters by value of cards dealt for dealer and player
# 11.Print counts for player and dealer
# 12.Use if-else statements to compare dealer with player and output "The winner is ..."




'''
# Problem #5: Natural Language Toolkit (NLTK) Text Files
# Import nltk module (https://www.nltk.org/book/ch01.html)
import nltk

# Download Gutenberg corpus (http://www.gutenberg.org/)
nltk.download('gutenberg')  

# Print list of all texts available from Gutenberg corpus
print('Texts: ', nltk.corpus.gutenberg.fileids())

# Select a text file from the list of 'Texts' above, and assign to the filename variable below as a string
filename = 

text = nltk.corpus.gutenberg.words(filename)
text_list = list(text)  # create a list of the words in your chosen file
print(text_list)

# Print the length of text_list


# Slice the text_list and print the first 50 elements


# Choose 2 words of interest and find the count of occurrences of the words in text_list
(hint: use the .count() method). Create a dictionary of word counts.


# Create a set of words from text_list


# Print length of set of unique words from text


# Create a list of the set of words and sort them in ascending order

'''

