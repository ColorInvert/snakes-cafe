print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
orders_dict = {}
user_response = ""
count = 0

#Provide infinite loop
while 1 == 1:
    user_response = input("> ")
    #break infinite loop if user types "quit"
    if user_response == "quit":
        break

    if user_response not in orders_dict:
        orders_dict[user_response] = 1
        print(f"** 1 order of {user_response} has been added to your meal **")
    else:
        orders_dict[user_response] += 1
        print(f"** {orders_dict[user_response]} orders of {user_response} have been added to your meal **")
