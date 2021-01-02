class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print(f"{self.name} поехала")

    def stop(self):
        return print(f"{self.name} остановилась")

    def turn_right(self):
        return print(f"{self.name} повернула направо")

    def turn_left(self):
        return print(f"{self.name} повернула налево")

    def show_speed(self):
        return print(f"{self.name} едет со скоростью {self.speed} км/ч.")

    def police(self):
        if self.is_police:
            return print(f"{self.name} полицейская машина")
        else:
            return print(f"{self.name} не полицейская машина")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 60:
            return print(f"{self.name} едет со скоростью {self.speed}")
        else:
            return print(f"Превышение скорости автомобилем {self.name}."
                         f" Скорость {self.speed} км/ч. Максимальная 60 км/ч ")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 40:
            return print(f"{self.name} едет со скоростью {self.speed}")
        else:
            return print(f"Превышение скорости автомобилем {self.name}."
                         f" Скорость {self.speed} км/ч. Максимальная 40 км/ч ")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


ferrari = SportCar(200, 'Желтый', 'Феррари', False)
nissan = TownCar(30, 'Белый', 'Ниссан', False)
toyota = WorkCar(70, 'Серый', 'Тойота', True)
lada = PoliceCar(110, 'Синний', 'Жигули', True)

ferrari.show_speed()
toyota.police()
toyota.show_speed()
ferrari.go()
lada.turn_left()
lada.turn_right()
nissan.stop()
ferrari.police()
print(lada.name)
print(ferrari.color)
