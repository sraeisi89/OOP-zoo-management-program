
class Zoo:
    def __init__(self, name, territory=100):
        self.name = name
        self.territory = territory
        self.animals = []


    def sell(self):
        if len(self.animals) == 0:
            print(f"no animals to sell")
            return
        maxT = max(animal.animal_territory for animal in self.animals)
        for animal in self.animals:
            if animal.animal_territory == maxT:
                self.animals.remove(animal)
            return animal

    def get_territory_status(self):
        i = 0
        for animal in self.animals:
            i += animal.animal_territory
        return i


    def place_animal(self, animal):
        if self.get_territory_status() + animal.animal_territory > 100:
            print(f"there's no territory for {animal.animal_name}")
        else:
            self.animals.append(animal)
            print(f"{animal.animal_name} is placed in {self.name}")


class Animal:
    def __init__(self, name, territory=20):
        self.animal_name = name
        self.animal_territory = territory

budapest_zoo = Zoo('Budapest Zoo') # Created with 100 territory
berlin_zoo = Zoo('Berlin Zoo', 200) # Created with 200 territory
elephant = Animal('elephant', 50) # Created with 50 territory
giraffe = Animal('giraffe', 40) # Created with 40 territory
zebra = Animal('zebra') # Created with 20 territory
budapest_zoo.sell() # Should print: no animals to sell
budapest_zoo.place_animal(elephant) # Should print: elephant is placed in Budapest Zoo
budapest_zoo.place_animal(giraffe) # Should print: giraffe is placed in Budapest Zoo
budapest_zoo.place_animal(zebra) # Should print: no territory for zebra in Budapest Zoo
berlin_zoo.place_animal(budapest_zoo.sell()) # Should print: elephant is placed in Berlin Zoo
budapest_zoo.place_animal(zebra) # Should print: zebra is placed in Budapest Zoo

