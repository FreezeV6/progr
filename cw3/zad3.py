class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House located at {self.address} with {self.area} sqm area, {self.rooms} rooms, priced at {self.price}, plot size {self.plot} sqm."

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat located at {self.address} with {self.area} sqm area, {self.rooms} rooms, priced at {self.price}, located on floor {self.floor}."


house = House(area=120, rooms=5, price=350000, address="123 Maple Street", plot=500)
print(house)

flat = Flat(area=80, rooms=3, price=200000, address="456 Oak Avenue", floor=4)
print(flat)
