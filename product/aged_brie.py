from product import Product


class AgedBrie(Product):
    def _update_quality(self):
        if self.quality <= 50:
            self.quality += 1

