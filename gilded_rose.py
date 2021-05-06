# -*- coding: utf-8 -*-
from product.factory import Factory


class Inventory(object):
    def __init__(self, products):
        self.products = products

    @classmethod
    def from_list(cls, product_list):
        products = []
        for product in product_list:
            products.append(Factory.create(name=product.name,
                                           sell_in=product.sell_in,
                                           quality=product.quality))
        return cls(products)

    def update(self):
        for product in self.products:
            product.update_features()
