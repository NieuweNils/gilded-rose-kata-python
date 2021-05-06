from product_name import ProductName
from aged_brie import AgedBrie
from backstage_passes import BackstagePasses
from sulfuras import Sulfuras
from conjured import Conjured
from product import Product


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
