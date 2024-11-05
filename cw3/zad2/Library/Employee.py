class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Employee:\n"
                f"  Name: {self.first_name} {self.last_name}\n"
                f"  Hire Date: {self.hire_date}\n"
                f"  Birth Date: {self.birth_date}\n"
                f"  Address: {self.city}, {self.street}, {self.zip_code}\n"
                f"  Phone: {self.phone}")
