from sup_class.carClass import Car
from trunk import Trunk


car = Car("VW", 2013, 3.2, "10000$", 200000)
car.description()
print('Хотите обновить пробег? Введите новый пробег: ', end='')
car.get_update_mileage(input())
print('Хотите обновить стоимость? Введите новую цену: ', end='')
car.get_update_price(input())
car.description()


trunk = Trunk('Грузовик', 'Камаз', 2000, 5.6, 98765, 1000000)
trunk.description()
trunk.get_update_price(111)
trunk.description()
