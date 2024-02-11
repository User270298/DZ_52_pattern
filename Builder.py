# Task 1 Builder
class Sushi:
    def __init__(self, builder):
        self.rice = builder.rice
        self.vasabi = builder.vasabi
        self.soy = builder.soy
        self.eel=builder.eel

class SushiBuilder:
    def __init__(self, name):
        self.name= name
        self.rice = False
        self.vasabi = False
        self.soy = False
        self.eel=False

    def add_rice(self):
        self.rice=True
        return self

    def add_vasabi(self):
        self.vasabi=True
        return self

    def add_soy(self):
        self.soy=True
        return self

    def add_eel(self):
        self.eel=True
        return self

    def build(self):
        return Sushi(self)

# sushi_builder=SushiBuilder('Futomaki')
# sushi=sushi_builder.add_rice().add_eel().add_vasabi()
# print(sushi.__dict__)


from abc import abstractmethod
class PastaFactory:
    def create_pasta(self):
        pass

class SpaghettiFactory(PastaFactory):
    def create_pasta(self):
        return Spaghetti()

class CarbonaraFactory(PastaFactory):
    def create_pasta(self):
        return Carbonara()

class FettuccineFactory(PastaFactory):
    def create_pasta(self):
        return Fettuccine()

class Pasta:
    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_toppings(self):
        pass

    @abstractmethod
    def add_seasoning(self):
        pass

class Spaghetti(Pasta):
    def get_type(self):
        return "Спагетти"

    def add_sauce(self):
        print("Добавляем помидорный соус")

    def add_toppings(self):
        print("Добавляем мясной фарш")

    def add_seasoning(self):
        print("Посыпаем пармезаном")

class Carbonara(Pasta):
    def get_type(self):
        return "Пенне"

    def add_sauce(self):
        print("Добавляем сливочный соус")

    def add_toppings(self):
        print("Добавляем кусочки куриного мяса")

    def add_seasoning(self):
        print("Посыпаем базиликом и орегано")

class Fettuccine(Pasta):
    def get_type(self):
        return "Карбонара"

    def add_sauce(self):
        print("Добавляем сливочно-грибной соус")

    def add_toppings(self):
        print("Добавляем кусочки ветчины")

    def add_seasoning(self):
        print("Посыпаем пармезаном и зеленью")

spaghetti_factory = SpaghettiFactory()
spaghetti = spaghetti_factory.create_pasta()
print("Приготовленная паста:", spaghetti.get_type())
spaghetti.add_sauce()
spaghetti.add_toppings()
spaghetti.add_seasoning()

carbonara_factory = CarbonaraFactory()
carbonara = carbonara_factory.create_pasta()
print("\nПриготовленная паста:", carbonara.get_type())
carbonara.add_sauce()
carbonara.add_toppings()
carbonara.add_seasoning()

fettuccine_factory = FettuccineFactory()
fettuccine = fettuccine_factory.create_pasta()
print("\nПриготовленная паста:", fettuccine.get_type())
fettuccine.add_sauce()
fettuccine.add_toppings()
fettuccine.add_seasoning()
