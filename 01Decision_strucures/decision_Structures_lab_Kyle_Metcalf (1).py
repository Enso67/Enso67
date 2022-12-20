#Age calculator


age = int(input("Please enter age\n"))

if age <= 1:
    print("infant")
elif age >1 and age < 13:
    print("child")
elif age >= 13 and age< 20:
    print("Teenager")
elif age>= 20:
    print("Adult")

#Money counting game


PENNIES = .01
NICKELS = .05
DIMES = .10
QUARTERS = .25

amt_pennies = int(input("Enter number of pennies"))
amt_nickels = int(input("Enter number of nickels"))
amt_dimes = int(input("Enter number of dimes"))
amt_quarters = int(input("Enter number of quarters"))

total_penn = amt_pennies * PENNIES
total_nick = amt_nickels * NICKELS
total_dime = amt_dimes * DIMES
total_quart = amt_quarters * QUARTERS

total = total_penn + total_nick + total_dime + total_quart

if total == 1:
    print("You win!")
elif total < 1:
        print("Less than one")
elif total >1:
        print("Greater than one")
        
    
