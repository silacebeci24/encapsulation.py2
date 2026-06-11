class Cat:
    def make_sound(self):
        print("Meow")


class Dog:
    def make_sound(self):
        print("Woof")


class Bird:
    def make_sound(self):
        print("Tweet")


animals = [Cat(), Dog(), Bird()]

for animal in animals:
    animal.make_sound()
