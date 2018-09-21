class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} в движении. Скорость {self.speed}')

    def stop(self):
        print(f'Машина {(self.name)} остановилась')

    def turn(self, direction):
        print(f'Машина {(self.name)} повернула {direction}')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police = False):
        Car.__init__(self, speed, color, name, is_police)

class SportCar(Car):

    def __init__(self, speed, color, name, is_police = False):
        Car.__init__(self, speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police = False):
        Car.__init__(self, speed, color, name, is_police)

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police = True):
        Car.__init__(self, speed, color, name, is_police)


car = PoliceCar('120', 'Grey', 'Lada')

car.go()
car.stop()
car.turn('Налево')
