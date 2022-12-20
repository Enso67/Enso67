#1 read data from Streaming_services.txt

#2 store data in apropriate container

#3output avg of all services


#4 write average price to new file [name]_files_Lab.txt

#incorporate exceptions /// try accept statements
# a function is a group of statements that perform a group of tasks
#splitting the code into functions is called moudlarization
#code will be simpler, can be reused (whicsh will prevent mistakes)
#easier to debug
#calling functions will make the code much easier to organize
#different team memebers can write different functions
#void function - no return statement - most of the time will be print statement
#value returning function
#most of the time we will use
#def main():
#def function_name("parameters"):
#the parameters are variables
#most of the time you will import matplot lib functions before the main statement
#there are global and local sets of information in the main funct
# will call function by function_name() (argument) (ex argv argC)
'''
def name():
     print('Kyle')
name()
#book practice
def show_double(number):
    result = number * 2
    print(result)
    
value = 5
show_double(value)

#function is still void 0 no return statement
def add_numbers(number1, number2):
    total = number1+ number2
    #these are local variables used within function
    print(total)

add_numbers(2,5)
#these arguments do not need to be 'number1' and 'number2'
#only order matters
add_numbers(age,friends_age)

                  
#ask the user to input their age and their friends ages
#call add numbers to add users age and their friends age

#write a program to define difference in their age
def difference(age,friends_age):
    diff = friends_age - age
    if diff < 0:
        diff_fix = diff * -1
        print('The difference is', diff_fix)
    else:
        print('The difference is', diff)


age = int(input("What is your age?\n"))
friends_age = int(input("What is your friends age\n"))

#use function parameters in order
difference(friends_age,age)


#value returning fuction
def sum_numbers(num1,num2):
    result = num1 + num2
    return result

#we will need a print statement
result = sum_numbers(2,5)
#if you just print this  it will not be stored in memory
print(result)
'''
#this does not work as a value returning statement
def difference(age,friends_age):
    diff = friends_age - age
    if diff < 0:
        diff_fix = diff * -1
        print('The difference is', diff_fix)
    else:
        print('The difference is', diff)
    return diff

age = int(input("What is your age?\n"))
friends_age = int(input("What is your friends age\n"))

#use function parameters in order
diff = difference(friends_age,age)
print(diff *-1)