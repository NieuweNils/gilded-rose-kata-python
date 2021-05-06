# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import Inventory
from products import Product

if __name__ == "__main__":
    print ("OMGHAI!")
    products = [
        Product(name="+5 Dexterity Vest",
                sell_in=10,
                quality=20),
        Product(name="Aged Brie",
                sell_in=2,
                quality=0),
        Product(name="Elixir of the Mongoose",
                sell_in=5,
                quality=7),
        Product(name="Sulfuras, Hand of Ragnaros",
                sell_in=0,
                quality=80),
        Product(name="Sulfuras, Hand of Ragnaros",
                sell_in=-1,
                quality=80),
        Product(name="Backstage passes to a TAFKAL80ETC concert",
                sell_in=15,
                quality=20),
        Product(name="Backstage passes to a TAFKAL80ETC concert",
                sell_in=10,
                quality=49),
        Product(name="Backstage passes to a TAFKAL80ETC concert",
                sell_in=5,
                quality=49),
        Product(name="Conjured Mana Cake",
                sell_in=3,
                quality=6),  # <-- :O
    ]
    inventory = Inventory.from_list(products)
    days = 2
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        for product in inventory.products:
            print('%s (sell_in = %d, quality = %d)' % (product.name, product.sell_in, product.quality))
        print("")
        inventory.update()

