#Software sales

#Enter cost of the sale
total_cost = int(input("Enter total cost"))

Ten = .1
Twenty = .2
Thirty = .3
Fourty = .4
#Total number sold         
sales = int(input("Enter total sold\n"))

#calculate discount
after_discount_Ten = total_cost - (total_cost* Ten)
    
after_discount_Twenty = total_cost - (total_cost* Twenty)

after_discount_Thirty = total_cost - (total_cost* Thirty)

after_discount_Fourty = total_cost - (total_cost* Fourty)

# determine discount
if sales >= 100:
    print("40% discount",after_discount_Fourty)
elif sales <= 99 and sales >= 50:
    print("30% discount",after_discount_Thirty)
elif sales <= 49 and sales >= 20:
    print("20% discount",after_discount_Twenty)
elif sales >= 10 and sales <= 19:
    print("10% discount",after_discount_Ten)
else:
    print("No discount")

