class Car():
    """создание класса родителя"""

    def __init__(self, model, age, engie, price, mileage):
        """метод конструктор класса"""
        self.model = model
        self.age = age
        self.engie = engie
        self.price = price
        self.mileage = mileage
        self.wheel = 4
        print('Модель создана')

    def description(self):
        """метод вызова описания экзепляра класса класса"""
        decr = f"Модель машыны: {self.model}, года выпуска - {self.age}, объем двигателя: {self.engie}, колесная база {self.wheel} колеса. Пробег - {self.mileage}. Цена: {self.price}"
        print(decr)

    def get_update_mileage(self, mileage):
        """метод изменения пробега экзепляра класса класса"""
        self.mileage = mileage
        print(f"Пробег машины машины {self.model} обновлен. Новый пробег {self.mileage}")
        # print('Хотите обновить стоимость машины')

    def get_update_price(self, price):
        """метод изменения стоимости экзепляра класса класса"""
        self.price = price
        print(f"Цена машины {self.model} обновлена. Новая стоимость {self.price}")

