from cw3 import Property

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House located at {self.address} with {self.area} sqm area, {self.rooms} rooms, priced at {self.price}, plot size {self.plot} sqm."
