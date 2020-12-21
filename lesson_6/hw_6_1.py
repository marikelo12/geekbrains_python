from time import sleep


class TrafficLight:
    def __init__(self, __color):
        self.__color = __color

    def running(self):
        i = 0
        for i in range(len(self.__color)):
            print(self.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            else:
                sleep(2)
                i += 1


trafficLight = TrafficLight(['Красный', 'Желтый', 'Зеленый'])
trafficLight.running()
