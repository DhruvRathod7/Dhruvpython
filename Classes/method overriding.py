class Animal:
    def __init__(self):
        print("This is Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        print("This is Mammal constructor")
        self.weight = 1
        super().__init__()

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim():
        print("swim")


m = Mammal()
print(m.age)
print(m.weight)
