class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Привет, меня зовут {self.name}."

class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        return f"Я {self.species} и издаю звук."

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return f"Я еду на {self.brand}."

class SuperBeing(Person, Animal, Vehicle):
    def __init__(self, name, species, brand):
 
        Person.__init__(self, name)
        Animal.__init__(self, species)
        Vehicle.__init__(self, brand)

    def super_power(self):
        return "Я обладаю сверхспособностью!"
