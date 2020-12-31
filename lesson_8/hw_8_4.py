class WareHouse:
    def __init__(self, name):
        self.name = name


class OfficeEquipment:
    def __init__(self, name, price, model, quantity, store: "WareHouse"):
        self.name = name
        self.price = price
        self.model = model
        self.quantity = quantity
        self.store = store

    def __str__(self):
        params = ''
        for key in self.__dict__:
            if key == 'store':
                params = f"{params}{key} : {self.__dict__[key].name} \n"
            else:
                params = f"{params}{key} : {self.__dict__[key]} \n"
        return params


class Printer(OfficeEquipment):
    def __init__(self, price, model, quantity, print_speed, store):
        super().__init__('Printer', price, model, quantity, store)
        self.print_speed = print_speed


class Scanner(OfficeEquipment):
    def __init__(self, price, model, quantity, resolution, store):
        super().__init__('Scaner', price, model, quantity, store)
        self.resolution = resolution


class Copier(OfficeEquipment):
    def __init__(self, price, model, quantity, max_size, store):
        super().__init__('Copier', price, model, quantity, store)
        self.max_size = max_size


if __name__ == "__main__":
    warehouse = WareHouse('Stock №1')
    office_tech = [Printer(5000, 'Samsung', 5, 500, warehouse),
                   Scanner(2000, 'HP', 10, '1920x1080', warehouse),
                   Copier(2000, 'Xerox', 7, 'A3', warehouse)]
    for el in office_tech:
        print(el)

