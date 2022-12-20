#Kyle Metcalf 11/2 CIS-115

##1. Input an integer indicating the number of floating-point values that will be accepted from input.

num = int(input("Enter total number of values\n"))

##2. Create an empty list.

normal = []

##3. Until you have input the proper number of new values from input, accept new values and append them to the list.
for i in range(num):
    value = int(input("Enter your value\n"))
    normal.append(value)


##4. Find the max value of the list.

print("Maximum value",(max(normal)))

##5. Using a for loop, iterate through the list and normalize each value. Print each normalized value.

normalized = []

for i in normal:
    normalized.append(i/max(normal))

print(normalized)

#numpy

import numpy

print(numpy.array(normal)/max(normal))

