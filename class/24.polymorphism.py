class Base:
    def get_pr(self):
        raise NotImplemented("необходимо определить метод в классе")

class Rectangle(Base):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_pr(self):
        return 2 * self.a + 2 * self.b

class Square(Base):

    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4*self.a

class Triangle(Base):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # def get_pr(self):
    #     return self.a + self.b + self.c

list_objects = [Rectangle(1, 2), Rectangle(3, 4),
                Square(5), Square(6),
                Triangle(7,8,9), Triangle(10,11,12)]

for x in list_objects:
    print(x.get_pr())