import os

plu = {
    2091: ['bananas', 1.00],
    2093: ['apples', 2.00],
    2095: ['oranges', 2.50],
    2097: ['grapes', 2.15],
    4032: ['ribeye steak', 10.97],
    4034: ['eye of round steak', 9.32]
}

prices = []
products = []
sub_total = sum(prices)

def get_plu():
    print("See list of plus (p)")
    while True:
        IO = input("Enter plu, press q to checkout: >")
        if IO == 'q':
            show_cart()
            break
        else:
            add_plu(IO)
            continue

def add_plu(IO):
    prices.append(plu[int(IO)][1])
    products.append(plu[int(IO)][0])

def show_cart():
    print("\nCart:\n")
    for item in range(len(products)):
        print(f'{products[item]}: ${prices[item]}')
    print('\n')

get_plu()
