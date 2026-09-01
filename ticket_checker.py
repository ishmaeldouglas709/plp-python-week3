#TICKET CHECKER, CHILDREN PAY CHILDREN ALLOCATED PRICE WHILE ADULTS PAY FULL PRICE

age=int(input("What is your age:"))
is_adult = age >= 18

ticket_price = {
    "adult":1500,"children":500
}

if is_adult :
    #pays adult price
    print(f'The ticket price is: {ticket_price["adult"]}')
else :
    #pays child price
    print(f'The ticket price is: {ticket_price["children"]}')
    
