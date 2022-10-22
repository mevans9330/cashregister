import os

# List of plus and associated products
plu = {
    2091: ['bananas', 1.00],
    2093: ['apples', 2.00],
    2095: ['oranges', 2.50],
    2097: ['grapes', 2.15],
    4032: ['ribeye steak', 10.97],
    4034: ['eye of round steak', 9.32]
}

# Array to store each product and price
prices = []
products = []

# Gets the items from the customer
def get_plu():
    os.system('cls')
    while True:
        show_plu()
        IO = input("Enter plu, press enter to checkout: >")
        if IO == '':
            os.system('cls')
            show_cart()
            break
        else:
            if int(IO) not in plu.keys():
                print("Please enter a valid Plu...")
                os.system('cls')
                continue
            else:
                add_plu(IO)
                os.system('cls')
                print(f'Added: {plu[int(IO)][0]}\n')
                continue

# Shows list of plus and products
def show_plu():
    for key, value in plu.items():
        print(key, value)
    print('\n')

# Adds the items to the above arrays
def add_plu(IO):
    prices.append(plu[int(IO)][1])
    products.append(plu[int(IO)][0])

# Shows the items in the cart
def show_cart():
    print("\nCart:\n")
    for item in range(len(products)):
        print(f'{products[item]}: ${prices[item]}')
    print('\n')
    # user_in = input('Press q to cash out >')
    os.system('PAUSE')
    checkout()

# Cash out the customer
def checkout():
    os.system('cls')
    sub_total = sum(prices)
    tax_percent = 0.0825
    tax = sub_total * tax_percent
    total = sub_total + tax
    # if user_in == 'q':
    print(f'Subtotal: ${sub_total:.2f}')
    print(f'Tax: ${tax:.2f}')
    print(f'Total: ${total:.2f}\n')
    tender = input('Enter tender: >$')
    get_change(tender, total)

def get_change(tender, total):
    print(f'\nTender: ${tender}')
    change = float(tender) - total
    print(f'Change: ${change:.2f}\n')
    print('Thank you for shopping with us!!\n')
    os.system('PAUSE')
    os.system('cls')

get_plu()
