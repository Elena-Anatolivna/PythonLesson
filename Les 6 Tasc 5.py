class Stationery:
    def __init__(self, title):
        self.title = title
    def drow(self):
        print(f'Запуск отрисовки!')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def drow(self):
        print(f'Запуск отрисовки!\nРисует: {self.title}')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def drow(self):
        print(f'Запуск отрисовки!\nРисует: {self.title}')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def drow(self):
        print(f'Запуск отрисовки!\nРисует: {self.title}')


pen = Pen('ручка')
print(pen.drow())
pencil = Pencil('карандаш')
print(pencil.drow())
handle = Handle('ручка')
print(handle.drow())