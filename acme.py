"""
ACME class to describe products that ACME makes
"""

import random


class Product:
    """
    An Acme product class
    """
    def __init__(
        self,
        name: str,
        price: int=10,
        weight: int=20,
        flammability: float=0.5,
            identifier: int=random.randint(1_000_000, 9_999_999)):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """
        describes how much someone would like to steal the product based
        on how much it costs over how much it weighs
        """
        price_to_weight = self.price / self.weight
        if price_to_weight < 0.5:
            return("Not so stealable...")
        elif price_to_weight <= 1.0:
            return("Kinda stealable.")
        else:
            return("Very stealable!")

    def explode(self):
        """explodes the object bassed on weight and flammability"""
        flam_times_weight = self.flammability * self.weight
        if flam_times_weight < 10:
            return("...fizzle.")
        elif flam_times_weight <= 50:
            return("...boom!")
        else:
            return("...BABOOM!!")


class BoxingGlove(Product):
    """Boxing glove product subclass"""

    """
    I tried everything I could think of to not have to
    repeat all these definitions,
    in order to only redifine weight,
    but unless I put in all the parameters again the weight
    wouldn't be changed from 20 to 10.
    """
    def __init__(
        self,
        name: str,
        price: int=10,
        weight: int=10,
        flammability: float=0.5,
            identifier: int=random.randint(1_000_000, 9_999_999)):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        """explodes the given glove's based on weight and flammability"""
        return("... it's a glove.")

    def punch(self):
        """ punches you based on the glvoe's weight'"""
        if self.weight < 5:
            return("That tickles.")
        elif self.weight < 15:
            return("Hey that hurt!")
        else:
            return("OUCH!")
