class Clothes:

    def __init__(self, name, size):
        self.name = name
        self.size = size


class Coat(Clothes):
    @property
    def tissue_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    @property
    def tissue_consumption(self):
        return round(self.size * 2 + 0.3, 2)


if __name__ == "__main__":
    coat = Coat('Пальто', 1)
    suit = Suit('Костюм', 2)
    coat_2 = Coat('Па', 2)
    print(f'На пальто {coat.size}-го размера потребуется {coat.tissue_consumption} м ткани')
    print(f'На костюм {suit.size}-го размера потребуется {suit.tissue_consumption} м ткани')
    print(f'Итого потребуется {coat.tissue_consumption + suit.tissue_consumption} м ткани')
