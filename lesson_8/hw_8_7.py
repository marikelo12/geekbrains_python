class ComplexNumber:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        znac = ' + ' if self.b > 0 else ' - '
        b = f'{znac}{abs(self.b)}' if abs(self.b) != 1 else f'{znac}'
        if self.b != 0 and self.a != 0:
            return f"{self.a}{b}i"
        elif self.b != 0:
            return f'{self.b}i'
        else:
            return f"{self.a}"

    def __add__(self, other):
        c = self.a + other.a
        d = self.b + other.b
        return ComplexNumber(c, d)

    def __mul__(self, other):
        c = self.a * other.a - self.b * other.b
        d = self.a * other.b + self.b * other.a
        return ComplexNumber(c, d)


z_1 = ComplexNumber(2, 1)
z_2 = ComplexNumber(1, 2)
print(f'Результатом сложения комплексных чисел ({z_1}) и ({z_2}) будет число ({z_1 + z_2})')
print(f'Результатом умножения комплексных чисел ({z_1}) и ({z_2}) будет число ({z_1 * z_2})')