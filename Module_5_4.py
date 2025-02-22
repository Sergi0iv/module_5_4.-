class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history += args
        return object.__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):

        if new_floor >= 1 and new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует!')

    def __eq__(self, other):
        if self.number_of_floors == other.number_of_floors:
            return True
        else:
            return False

    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории.')



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)