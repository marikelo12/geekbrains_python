from abc import abstractmethod, ABC


class Technics(ABC):
    def __init__(self, model, serial_no):
        self.model = model
        self.serial_no = serial_no
        self.department = None

    def _set_department(self, department):
        self.department = department

    @abstractmethod
    def __call__(self, data):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Printer(Technics):
    def print_smth(self, data: str):
        return f'Printer model {self.model} s/n {self.serial_no} printed {data}'

    def __call__(self, data):
        self.print_smth(data)

    def __str__(self):
        return f'Printer model {self.model} s/n {self.serial_no}'


class Xerox(Technics):
    def copy_smth(self, data: str):
        return f'Xerox model {self.model} s/n {self.serial_no} copied {data}'

    def __call__(self, data):
        self.copy_smth(data)

    def __str__(self):
        return f'Xerox model {self.model} s/n {self.serial_no}'


class Scanner(Technics):
    def scan_smth(self, data: str):
        return f'Scanner model {self.model} s/n {self.serial_no} scanned {data}'

    def __call__(self, data):
        self.scan_smth(data)

    def __str__(self):
        return f'Scanner model {self.model} s/n {self.serial_no}'


class Warehouse:
    def __init__(self, max_volume):
        self.max_volume = max_volume
        self.storage = {
            "scanners": set(),
            "xeroxes": set(),
            "printers": set()
        }
        self.add_mapper = {Scanner: "scanners", Printer: "printers", Xerox: "xeroxes"}
        self.total = 0

    def get_several_tecs_to_warehouse(self, num: int, tech_list):
        if type(num) != int:
            raise ValueError("Введите число!")
        for tech in tech_list[:num]:
            self.get_several_tecs_to_warehouse(tech)

    def get_tech_to_warehouse(self, technics: Technics):
        if self.total == self.max_volume:
            raise OverflowError("Склад заполнен до отказа!")
        self.storage[self.add_mapper[type(technics)]].add(technics)
        technics._set_department("warehouse")
        self.total += 1

    def get_tech_to_departament(self, tech_type, department):
        tech_to_dept = self.storage[tech_type].pop()
        tech_to_dept._set_department(department)
        self.total -= 1

    def __call__(self, *args, **kwargs):
        self.get_tech_to_warehouse(*args, **kwargs)

    def __str__(self):
        return f'Warehouse max capacity {self.max_volume} current {self.total} '


printer = Printer(1, 2)
printer_2 = Printer(1, 3)
scanner = Scanner(2, 3)
scanner_2 = Scanner(2, 5)
warehouse = Warehouse(10)
warehouse.get_tech_to_warehouse(printer)
warehouse.get_tech_to_departament("printers", "service")
