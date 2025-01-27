
class Human:

    def __init__(self, name: str, age: int, gender: str):
        self.name: str = name
        self.age: int = age
        self.gender: str = gender

class Man(Human):

    def __init__(self, name, age, gender, weight):
        super().__init__(name, age, gender)
        self.weight = weight

    def __str__(self):
        return f"name: {self.name}, age {self.age}, gender {self.gender}, weight {self.weight}"

man_1 = Man("Ivan", 17, "male", 60)
print(man_1)
