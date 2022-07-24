class Animal:
    cool = True

    def make_sound(self,sound):
        print(f"This animal says {sound}")

class Cat(Animal):
    pass

blue = Animal()
garfild = Cat()

garfild.make_sound("MEOW")
blue.make_sound("MEOW, MEOW")

