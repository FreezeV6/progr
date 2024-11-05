class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Library:\n"
                f"  City: {self.city}\n"
                f"  Street: {self.street}\n"
                f"  Zip Code: {self.zip_code}\n"
                f"  Open Hours: {self.open_hours}\n"
                f"  Phone: {self.phone}")
