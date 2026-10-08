from abc import ABC, abstractmethod

class Animal(ABC):
    count = 0

    def __init__(self, name):
        self.name = name
        Animal.count += 1

    @abstractmethod
    def food_per_day(self):
        pass

class Lion(Animal):
    def food_per_day(self):
        return 5

class Rabbit(Animal):
    def food_per_day(self):
        return 0.5

class Elephant(Animal):
    def food_per_day(self):
        return 50

class Zoo:
    def __init__(self):
        self._animals = []

    def add(self,animal):
        self._animals.append(animal)

    def daily_food(self):
        df = 0
        for animal in self._animals:
            df += animal.food_per_day()
        return df

animal1 = Lion('Африканец')
animal2 = Rabbit('Мики')
animal3 = Elephant('Жиробас')
#Имена придумала Сестра

zoo1 = Zoo()

zoo1.add(animal1)
zoo1.add(animal2)
zoo1.add(animal3)

print(zoo1.daily_food())