filename = "holiday_calories.txt"

file_mode = "r"
output_file = open(filename, file_mode)


#readlines will separate each line in a list
#read will just show you string
contents = output_file.readlines()

food = list(filename)




holidayD = {}

#slice the list at line 1
for i in contents[1:]:
    #split up each item in file
    line = (i.split())
    #assign values to each part of the list
    food = line[0]
    #covert calories to int
    calories = int(line[1])
    #store these items in dict by setting food to the key and calories to the value
    holidayD[food] = calories
print(holidayD)
#create a list of all the values in the dict
# we can also do the same with keys
values_list =  list(holidayD.values())
#find max value in values of dict
max_value = max(values_list)
#find the index of the max value
idx = values_list.index(max_value)
#make a list of keys to index the item in the list of keys
keys_list = list(holidayD.keys())
#print keys list at indexed value
print(keys_list[idx])


#we can sort the individual items with a key - this will allow us to asscoiate 
#this can can be called to give the individual value
'''
#print the 2nd index in between each file
for line in contents:
#split will create a list with two different elements (any single space, tab new line
    line_split = line.split()
    print((line_split[1]))


# .split method will divide a lists of string by "\n"," ", "\t".
#Creating a new list
txt = "CIS_115"
print(txt)
txt_list = txt.split("_")
print(txt_list)
#CSV files will be separated by commas
#txt = txt.replace(" ","")
'''

