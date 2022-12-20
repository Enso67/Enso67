'''
password = "password*"
user_password = input("Password\n")

while user_password != password:
    print("Wrong password")
    user_password = input("Password\n")
else:
    print("Correct password")


goal = 20
num = int(input("How many customers have you helped?"))
while num < goal:
    print(num)
    num += 1
'''

grade = float(input("Enter grade\n"))
while grade < 0 or grade > 100:
    print("Error: invalid input. You entered", grade,"and expected grade is between 0 and 100")
    grade = float(input("Enter a new grade")
    if grade >=0 and grade <= 50:
                  break
else:
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")
print("Come see me")

#while loop to determine commission
keep_going = "y"
while keep_going == "y":
        sales = float(input("Enter total sales"))
        comm_rate = float(input("Enter comm_Rate"))
        commission = sales * comm_rate
        print(commission)
        keep_going = input("type y to continue")
else:
        print("End")

#whle loop to determine salary
hourly_rate = 15

num_hours = int(input("Enter number of hours\n")

while num_hours < 0 and num_hours > 60:
    print("Error, too little or too many hours")
    num_hours = int(input("Enter number of hours\n")

salary = num_hours * hourly_rate

print("Total salary\n", salary)

