class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        pass

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print(f'Для написания текста используется {self.title}')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print(f'Для создания эскиза используется {self.title}')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return print(f'Для флип-чарта используется {self.title}')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('маркер')
pencil.draw()
handle.draw()
pen.draw()

