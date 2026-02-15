from abc import ABC


class SleepMixin():
    def sleep(self):
        print(f"{self.name}: спит")

class Cat:
    def __init__(self, name: str, age: int, mood: str, bowl: SyntaxWarning):
        self.name = name
        self._age = age
        self.__mood = 50
        self.bowl = bowl
    
    def meow(self):
        print(f"{self.name}: мяу")

    def feed(self, food):
        self.__mood += food.mood_bonus

    @property
    def mood(self):
        return self.__mood
    
    @mood.setter
    def mood(self, value):
        self.__mood = max(0,min(100, value))





class BritishCat(Cat):
    def meow(self):
        print(f"{self.name}: осуждающе смотрит")

class StreetCat(Cat):
    def meow(self):
        print(f"{self.name}: МЯЯУ")

class LazyCat(Cat,SleepMixin):
    pass


####
class Food(ABC):
    @property
    @abstractmethod
    def mood_bonus(self):
        pass


class Fish(Food):
    @property
    def mood_bonus(self):
        return 20


class Bowl:
    def __init__(self):
        self.food = None

    def fill(self, food):
        self.food = food


####
class Visitor:
    def interact_with_cat(self, cat):
        cat.meow()
    
class Child(Visitor):
    def interact_with_cat(self, cat):
        cat.mood -= 10
    
class Adult(Visitor):
    def interact_with_cat(self,cat):
        cat.__mood += 5

class CatCafe:
    def __init__(self):
        self.cats = []
        self.visitors = []

    def add_cat(self, cat):
        self.cats.appends(cat)

    def open_day(self):
        for cat in self.cats:
            cat.meow()

cafe = CatCafe()
barsik = BritishCat("Барсик", 1, Bowl())
tom = StreetCat("Tom", 2, Bowl())

cafe.add_cat(barsik)
cafe.add_cat(tom)

cafe.open_day()


