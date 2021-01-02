class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity != other.quantity:
            return Cell(abs(self.quantity - other.quantity))
        else:
            return "Ячеек не осталось"

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        if self.quantity > other.quantity:
            return Cell(self.quantity // other.quantity)
        else:
            return Cell(other.quantity // self.quantity)

    def make_order(self, cells_in_row):
        row = ''
        for i in range(self.quantity // cells_in_row):
            row += f'{"*" * cells_in_row} \n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

    def __str__(self):
        return f"Клетка cостоит из {self.quantity} ячеек."


if __name__ == "__main__":
    cell_1 = Cell(5)
    cell_2 = Cell(15)
    cell_3 = Cell(10)
    print(cell_1 + cell_2)
    print(cell_2 - cell_1)
    print(cell_1 * cell_2)
    print(cell_1 / cell_2)
    print(cell_1.make_order(5))

