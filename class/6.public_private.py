#  pip install accessify - установка пакета для более лучше защиты приватных методов и свойств
from accessify import private, protected # для создания првиатных и защищенных методов (только методы)

class Point:
    """
    Механизм инкапсуляции
    attribute (без одного или двух подчеркиваний вначале) - публичное свойство (public)
    _attribute (с одним подчеркиванием) - режим доступа protected (служит для обращения внутри класса
    и во всех его дочерних классах)
    __attribute (с двумя подчеркиваниями) - режим доступа private (служит для обращения только внутри
    класса)
    """

    def __init__(self, x=0, y=0):
        # self._x = x     # в python "_" лишь сигнализирует программисту, что свойство является защищенным,
                        # но никак явно не ограничивает к нему доступ из вне
                        # т.е. _ указывает, что это внутренняя служебная переменная
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):  # метод сеттер (интерфейсный метод)
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self):    # метод геттер (интерфейсный метод)
        return self.__x, self.__y

pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt.get_coord())
print(dir(pt))  # dir - посмотреть какие свойства существуют в экземпляре класса pt
print(pt._Point__x) # _Point__x, _Point__y - кодовые имена приватных свойств
print(pt._Point__y)
