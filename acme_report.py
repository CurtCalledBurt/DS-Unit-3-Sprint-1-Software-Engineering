""" products in acme """

import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products: int=30):
    """
    creates the inputed integer number (30 by default)
    of Product class objects
    """
    products = []
    for _ in range(num_products):

        adj = random.choice(ADJECTIVES)
        noun = random.choice(NOUNS)
        name = adj + ' ' + noun

        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)

        prod = Product(
            name,
            price=price,
            weight=weight,
            flammability=flammability)
        products.append(prod)
    return(products)


def inventory_report(seq):
    """
    prints the number of unique names of items, avg price,
    avg weight, and avg flammability of a list of Product class
    objects
    """
    num_prod = len(seq)

    names = set()
    avg_price = 0
    avg_weight = 0
    avg_flam = 0
    for prod in seq:
        names.add(prod.name)
        avg_price += prod.price
        avg_weight += prod.weight
        avg_flam += prod.flammability

    avg_price = avg_price / num_prod
    avg_weight = avg_weight / num_prod
    avg_flam = avg_flam / num_prod

    print("ACME Inventory Report \n")
    print(f"Number of Unique Products {len(names)} \n")
    print(f"Average Price: {avg_price} \n")
    print(f"Average Weight: {avg_weight} \n")
    print(f"Average Flammability: {avg_flam} \n")

    return None

if __name__ == '__main__':
    inventory_report(generate_products())
