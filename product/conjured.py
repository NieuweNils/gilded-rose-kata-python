from product import Product


class Conjured(Product):
    def _update_quality(self):
        self.quality -= 2

