class Bowl:
    def __init__(self, name: str):
        self.eat_name = name

    def eat(self, cat_name: str):
        print(f"{cat_name} покушал {self.eat_name}")


class JumpMixin:
    def jump(self):
        print(f"я {self.name} прыгнул")


class Cat:
    def __init__(self, name: str, age: int, dish: Bowl):
        self.__name = name
        self.__age = age
        self.dish = dish

    def meow(self):
       print(f"{self.__name} is meowing") 

    @property
    def name(self):
        return self.__name


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0 or value < self.__age:
            raise ValueError("Неверно задан возраст кота")

        self.__age = value


    def eat(self):
        self.dish.eat(self.__name)

class BritishCat(Cat, JumpMixin):
    def meow(self):
        print("осуждающий взгляд")



meal = Bowl("мясо")
cat1 = Cat("Tom", 2,meal)
cat2 = BritishCat("Felix", 2, meal)

cat2.jump()
cat1.eat()