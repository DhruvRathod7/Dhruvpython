class Human:
    def eat(self):
        print("roar")


class Paneer(Human):
    def fly(self):
        print("Eat")


class Punjabi(Paneer):
    def walk(self):
        print("spicy")


p = Punjabi()
print(issubclass(Punjabi, Human))
