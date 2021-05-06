from product import Product


class BackstagePasses(Product):
    def _update_quality(self):
        if self.sell_in <= 0:
            self.quality = 0
        elif self.sell_in < 5:
            self.quality += 3
        elif self.sell_in < 10:
            self.quality += 2
        else:
            self.quality += 1
