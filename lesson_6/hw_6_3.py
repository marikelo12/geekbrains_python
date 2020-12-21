class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())


p = Position('Иван', 'Иванов', 'Менеджер', 1000000, 1000000)
print(p.get_full_name(), p.get_total_income())
