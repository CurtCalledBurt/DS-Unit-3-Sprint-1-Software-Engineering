#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """ make sure weight is defaulting 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_non_default_stealability(self):
        """ tests if stealability works on non default values """
        prod = Product('Test Product', price=20, weight=10)
        self.assertEqual(prod.stealability(), "Very stealable!")


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        """ tests if generate_products is making 30 items by default"""
        seq = generate_products()
        self.assertEqual(len(seq), 30)

    def test_legal_names(self):
        """ tests that the names of the generated items are valid"""
        seq = generate_products()
        for prod in seq:
            p_name = prod.name
            words = p_name.split()
            adj = words[0]
            noun = words[1]

            self.assertIn(adj, ADJECTIVES)
            self.assertIn(noun, NOUNS)
            self.assertEqual(p_name, adj + ' ' + noun)


if __name__ == '__main__':
    unittest.main()
