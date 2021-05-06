# -*- coding: utf-8 -*-
import unittest

from ..gilded_rose import Inventory
from ..product.product import Product


class GildedRoseTest(unittest.TestCase):
    def test_product_update(self):
        products = [Product(name="Product without special effects",
                            sell_in=10,
                            quality=20)]
        inventory = Inventory.from_list(products=products)
        inventory.update()
        self.assertEquals("Product without special effects", inventory.products[0].name)
        self.assertEquals(9, inventory.products[0].sell_in)
        self.assertEquals(19, inventory.products[0].quality)

    def test_product_quality_not_greater_than_50(self):
        products = [Product(name="quality at 50",
                            sell_in=2,
                            quality=50)]
        inventory = Inventory.from_list(products=products)
        inventory.update()
        self.assertEquals("quality at 50", inventory.products[0].name)
        self.assertEquals(1, inventory.products[0].sell_in)
        self.assertEquals(50, inventory.products[0].quality)

    def test_brie_update(self):
        products = [Product(name="aged brie",
                            sell_in=10,
                            quality=20)]
        inventory = Inventory.from_list(products=products)
        inventory.update()
        self.assertEquals("aged brie", inventory.products[0].name)
        self.assertEquals(9, inventory.products[0].sell_in)
        self.assertEquals(21, inventory.products[0].quality)

    def test_backstage_passes_update(self):
        products = [Product(name="Backstage passes to something",
                            sell_in=10,
                            quality=20)]
        inventory = Inventory.from_list(products=products)
        inventory.update()
        self.assertEquals("Backstage passes to something", inventory.products[0].name)
        self.assertEquals(9, inventory.products[0].sell_in)
        self.assertEquals(22, inventory.products[0].quality)



if __name__ == '__main__':
    unittest.main()
