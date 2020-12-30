class Stock:
    def __init__(self, name):
        self.name = name


class OfficeEquipment:
    def __init__(self, name, price, model, quantity):
        self.name = name
        self.price = price
        self.model = model
        self.quantity = quantity


class Printer(OfficeEquipment):
    def __init__(self, price, model, quantity, print_speed):
        super().__init__('Printer', price, model, quantity)
        self.print_speed = print_speed


class Scaner(OfficeEquipment):
    def __init__(self, price, model, quantity, resolution):
        super().__init__('Scaner', price, model, quantity)
        self.resolution = resolution


class Copier(OfficeEquipment):
    def __init__(self, price, model, quantity, max_size):
        super().__init__('Copier', price, model, quantity)
        self.max_size = max_size


stock = Stock('Stock №1')
