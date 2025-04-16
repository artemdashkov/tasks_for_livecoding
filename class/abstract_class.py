from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

    def move(self):
        pass

class Dog(Animal):

    def speak(self):
        return "Гав"

    # def move(self):
    #     return "бегать"

dog = Dog()
print(dog.speak())
# print(dog.move())