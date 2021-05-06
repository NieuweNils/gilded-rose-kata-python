class Product:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def _update_sell_in(self):
        if self.sell_in > 0:
            self.sell_in -= 1

    def _update_quality(self):
        if 50 > self.quality > 0:
            if self.sell_in < 0:
                self.quality -= 2
            else:
                self.quality -= 1

    def update_features(self):
        self._update_sell_in()
        self._update_quality()


