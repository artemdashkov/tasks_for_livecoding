class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year={self.year})"

# Создаем экземпляр класса
car = Car("Toyota", "Corolla", 2022)

# Выводим объект с использованием repr
print(repr(car))  # Явно вызывает метод __repr__

# Или просто выводим объект
print(car)  # Если __str__ не определен, будет вызван __repr__