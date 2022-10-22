import os

# List of products
products = {
    4011: ["Bananas", 1.0],
    3032: ["Apples", 2.0],
    4048: ["Grapes", 2.50],
    3379: ["Oranges", 3.25],
    2233: ["Milk", 5.00],
    5553: ["Ribeyes", 8.25],
    4080: ["Soup", 10.00]
}

list = [

    [4011, "Bananas"], 
    [3032, "Apples"], 
    [4048, "Grapes"], 
    [3379, "Oranges"], 
    [2233, "Milk"], 
    [5553, "Ribeyes"], 
    [4080, "Soup"]

]

names = []
amounts = []

# Add items to register
def add_items():
    count = 0
    while True:
        print("To view list of plu's press p...")
        user = input("Enter a plu or c to checkout >")
        if count == 3:
            os.system('cls')
        if user == 'c':
            display_items()
        elif user == 'p':
            for i in range(len(list)):
                print(list[i])
        else:
            count += 1
            name = products[int(user)][0]
            price = products[int(user)][1]
            names.append(name)
            amounts.append(price)
            for i in range(len(names)):
                item = names[i]
            for a in range(len(amounts)):
                dollar = amounts[a]
            print(f'\n{item}: ${dollar:.2f}0\n')

# Calculate Totals
def calculate_totals():
    tp = 0.0825
    sub_total = sum(amounts)
    tax = tp * sub_total
    total = sub_total + tax
    display_totals(sub_total, tax, total)

# Display Totals
def display_totals(sub_total, tax, total):
    os.system('cls')
    print(f'Subtotal: ${sub_total:.2f}')
    print(f'Tax: ${tax:.2f}')
    print(f'Total: ${total:.2f}\n')
    ui = input("Press c to continue checkout...")
    if ui == 'c':
        checkout(total)
    else:
        print(f'Sorry invalid input: {ui}, quitting...')

# Display change
def checkout(total):
    tender = input('Enter tender $')
    if tender != '0':
        change = float(tender) - total
        os.system('cls')
        print(f'Total: ${total:.2f}')
        print(f'Tender: ${tender}')
        print(f'Change: ${change:.2f}')
        print('\nThanks for shopping with us!!')
        new_customer()
    else:
        print('Sorry must enter amount above zero...')
        quit()

# Display Items
def display_items():
    os.system('cls')
    print(f'\nProducts added: \n')
    x = 0
    while x < len(names):
        print(f'{names[x]}: ${amounts[x]}0')
        x += 1
    ui = input("\nPress c to checkout...")
    if ui == "c":
        calculate_totals()
    else:
        print("Entered an invalid key \nquitting...")


# Ask if new customer to ring up
def new_customer():
    names.clear()
    amounts.clear()
    user = input("New customer?: (y, n) >")
    if user == 'y':
        add_items()
    elif user == 'n':
        print("Please start the program over...")
        quit()

# Main function
def main():
    os.system('cls')
    new_customer()

main()