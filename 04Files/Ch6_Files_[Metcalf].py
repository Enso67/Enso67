# CIS115
# Ch6: Files and Exceptions


# ---- Problem #1: Write to a file ----

#Tab delimited files
# Step 1: Choose a filename (need to include extension .txt)
# and assign to a variable
#Always must be string (All info we write to the file)


# ---- Problem #2: Read from a file ----

# Step 1: Assign filename "numbers.txt" to a variable (need to include extension .txt)
filename = "numbers.txt"


# Step 2: Assign the file mode ("w", "a", "r")
file_mode = "r"


# Step 3: Open file for reading

output_file = open(filename, file_mode)


# Step 4: Read from file (practice with .read() and .readlines())

contents = output_file.readlines()

#.re prints out a single string
print(contents)

# Step 5: Process the data by summing the numbers.
total = 0
for num in contents:
    print(int(num))
    total += int(num)

print(total)

numbered_lists = []
for i in contents:
    print(int(num))
    numbered_lists.append(int(num))



# Step 6: Close file
output_file.close()



# Challenge #4: Find the average, max, and min number of the numbers.txt file.




# Challenge #5: Read the data from the Streaming_Services.txt file
# and store it in an appropriate container.
# Determine the most expensive service and the average price.




# Challenge #6: Ask the user for the number of data points to read
# from the numbers.txt file. While the data is not equal to
# the empty string '', read in the specified number of lines using .readline().
# Find the average of the numbers that are read from the file.






