from product_names import ProductName
from products import AgedBrie
from products import BackstagePasses
from products import Sulfuras
from products import Conjured
from products import Product


class Factory:
    @staticmethod
    def create(name, sell_in, quality):
        if ProductName.AGED_BRIE.value in name.lower():
            return AgedBrie(name, sell_in, quality)
        elif ProductName.BACKSTAGE_PASSES.value in name.lower():
            return BackstagePasses(name, sell_in, quality)
        elif ProductName.SULFURAS.value in name.lower():
            return Sulfuras(name, sell_in, quality)
        elif ProductName.CONJURED.value in name.lower():
            return Conjured(name, sell_in, quality)
        else:
            return Product(name, sell_in, quality)
