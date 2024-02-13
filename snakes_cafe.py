import sys
order = {
    'appetizers': {
        'wings': 0,
        'cookies': 0,
        'spring rolls': 0
    },

    'entrees': {
        'salmon': 0,
        'steak': 0,
        'meat tornado': 0,
        'a literal garden': 0
    },

    'desserts': {
        'ice cream': 0,
        'cake': 0,
        'pie': 0
    },

    'drinks': {
        'coffee': 0,
        'tea': 0,
        'unicorn tears': 0
    },

    'custom': {

    }
}

def quit_program():
    quit_input = input('Would you like to quit? Type y to close program, type n to keep ordering.')
    quit_input = quit_input.strip()
    quit_input = quit_input.lower()

    if quit_input == 'y':
        print('Goodbye! Come again!')
        sys.exit()
    elif quit_input == 'n':
        print('Here is your current order: ')
        print_order()
    else:
        print('Sorry, I did not understand your command. Please enter y for yes, n for no.')

def print_order():
    # Loop through the main dictionary
    for course, food in order.items():
        # Only print items that have been added to order, not whole menu.
        for item, count in food.items():
            if count > 0:
                print(f"{course}-- {item} : {count}")

def main_program_loop():
    print(
        """**************************************
        **    Welcome to the Snakes Cafe!   **
        **    Please see our menu below.    **
        **
        ** To quit at any time, type "quit" **
        ** To see your current order, type "order" **
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
        Unicorn Tears""")

    print("""***********************************
    ** What would you like to order? **
    ***********************************""")

    while True:
        order_input = input('>')
        order_input = order_input.strip()
        order_input = order_input.lower()

        if order_input == 'quit':
            quit_program()
        elif order_input == 'order':
            print_order()
        else:
            found = False
            # loop through order dictionary to find thing
            for course, food in order.items():
                # if found, add to order
                if order_input.lower() in food:
                    order[course][order_input] += 1
                    found = True
                    if order[course][order_input] <= 1:
                        print(f"**{order[course][order_input]} order of {order_input} has been added to your order**")
                    else:
                        print(f"**{order[course][order_input]} orders of {order_input} has been added to your order**")
                    break
            if not found:
                new_input = input('''The kitchen fairies did not find this item on the menu. If you would like to order
                this anyway, type 'enchant me' to add it to your order. If you did not mean to order this, type 'jk' to 
                keep ordering from the menu.''')
                new_input = new_input.strip()
                new_input = new_input.lower()

                if new_input == 'enchant me':
                    order['custom'][order_input] = 1
                    print(f"**{order['custom'][order_input]} added to order!")
                elif new_input == 'jk':
                    continue
                else:
                    input('Sorry, I did not understand your input. Please try again.')


if __name__ == "__main__":
    main_program_loop()



