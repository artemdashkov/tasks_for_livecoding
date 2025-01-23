

class Vector:

    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):     # validate - метод класса, cls - ссылка на текущий класс
                                # метод класса работает исключительно с атрибутами класса
                                # и не может обращаться к локальным атрибутам экземпляра класса
                                # т.к. нет ссылки на объект (self), с которым он должен работать
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod   # Определяются методы, которые не имеют доступа ни к атрибутам класса,
                    # ни к атрибутам его экземпляра
                    # обычно это делают для удобства, чтобы связать функцию с тематикой класса
                    # метод можно вызывать и внутри обычных методов
    def norm2(x, y):    # сервисная вспомагательная функция
        return x*x + y*y


    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y): # можно было указать Vector.validate(x)
            self.x = x
            self.y = y
        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

print(Vector.validate(105))
print(Vector.norm2(5, 6))
v = Vector(1, 4)
print(f"x = {v.x}")
print(f"y = {v.y}")