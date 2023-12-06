from sup_class.carClass import Car


class Trunk(Car):
    """класс потомок класса Car"""

    def __init__(self, type_model, model, age, engie, price, mileage):
        super().__init__(model, age, engie, price, mileage)
        self.wheel = 8
        self.type_model = type_model

    def description(self):
        """переопределение метода родителя_класса"""
        decr = f"Вид {self.type_model}. Модель машыны: {self.model}, колесная база {self.wheel} колеса. Цена: {self.price}"
        print(decr)
