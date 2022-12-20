

# take input and check to see if it is a palindrome
word = input("Enter a word and check to see if it is a palindrome\n")

if word[::-1] != word:
        print("Not a palindrome")
else:
        print("Palindrome")

#this code sets j to -1 and counts backwards into the negatives
word_2 = input("Enter a word and check to see if it is a palindrome\n")
j = -1

#i is based on the range of the length of the word 
for i in range(len(word)):
        if word_2[i] != word_2[j]:
                print("Not a palindrome")
                break
        j = j-1
else:
        print("PALINDROME")

#this will use reverse list and only check half the list
#more effecient
word_3 = input("Enter a word and check to see if it is a palindrome\n")
rev_word = list(word_3)
rev_word.reverse()
for i in range(len(word_3) // 2):
        if word[i] != rev_word[i]:
                print("Not a palindrome")
                break
        else:
                print("PALINDROME")
