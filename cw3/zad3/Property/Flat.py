from cw3.zad3.Property.Property import Property


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat located at {self.address} with {self.area} sqm area, {self.rooms} rooms, priced at {self.price}, located on floor {self.floor}."
