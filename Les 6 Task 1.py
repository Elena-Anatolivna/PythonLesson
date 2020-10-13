from time import sleep

class TrafficLight:

    __color = ['красный', 'желтый', 'зеленый']

    def running (self):
        i = 0
        while True:
            print(f'Включается: {TrafficLight.__color[0]} цвет')
            sleep(7)
            print(f'Включается: {TrafficLight.__color[1]} цвет')
            sleep(2)
            print(f'Включается: {TrafficLight.__color[2]} цвет')
            sleep(4)
            i += 1




traffic_light = TrafficLight()
print(traffic_light.running())



