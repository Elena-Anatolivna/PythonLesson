class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_left(self):
        return f'{self.name} повернула на лево'

    def turn_right(self):
        return f'{self.name} повернула на право'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def swow_speed(self):
        self.speed = int(self.speed)
        if self.speed > 60:
            print('Вы превысили скорость!')
        elif self.speed < 60:
            print('Не привышайте скорость свыше 60 км/ч')

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def swow_speed(self):
        self. speed = int(self.speed)
        if self.speed > 40:
            print('Вы превысили скорость!')
        elif self.speed < 40:
            print('Не привышайте скорость свыше 40 км/ч')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def max_speed(self):
        self.speed = int(self.speed)
        if self.speed >= 150:
            print(f'{self.name}: спортивная машина')
        elif self.speed < 150:
            print(f'{self.name} может ездить быстрее')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police == True:
            print(f'{self.name} полицейская машина')
        else:
            print(f'{self.name} не полицейская машина')


niva = WorkCar('30', 'серый', 'Niva', False )
print(niva.speed)
print(niva.stop())
print(niva.swow_speed())


mazda = TownCar('50', 'синий', 'Mazda', True)
print(mazda.name)
print(mazda.color)
print(mazda.swow_speed())

ferrari = SportCar('139', 'красный', 'Ferrari', False)
print(ferrari.speed)
print(ferrari.turn_left())
print(ferrari.max_speed())

suzuki = PoliceCar('75', 'белый', 'Suzuki', False)
print(suzuki.go())
print(suzuki.turn_right())
print(suzuki.police())



















#    audi = SportCar(100, 'Red', 'Audi', False)
 #   oka = TownCar(30, 'White', 'Oka', False)
 #   lada = WorkCar(70, 'Rose', 'Lada', True)
 #   ford = PoliceCar(110, 'Blue', 'Ford', True)
 #   print(lada.turn_left())
 #   print(f'When {oka.turn_right()}, then {audi.stop()}')
 #   print(f'{lada.go()} with speed exactly {lada.show_speed()}')
 #   print(f'{lada.name} is {lada.color}')
  #  print(f'Is {audi.name} a police car? {audi.is_police}')
  ##  print(audi.show_speed())
   # print(oka.show_speed())
   # print(ford.police())
  # 3 print(ford.show_speed())


