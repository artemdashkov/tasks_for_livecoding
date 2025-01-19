class Point:
    """Описание класса"""
    color = "red"   # переменную внутри класса называют атрибутом КЛАССА или его свойством (данными).
                    # атрибуты класса общие, для всех его экземпляров
    circle = 2

    def set_coords(self, x, y):   # методы начинается с глагола, self - ссылка на объект класса
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

pt = Point()
pt.set_coords(1, 3)
print(pt.get_coords())