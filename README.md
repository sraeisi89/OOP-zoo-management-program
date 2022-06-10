zoo management program.
We want to register new zoos in the system. Every zoo has a name and the size of its territory. The territory of a zoo is by default 100.

We want to place animals in zoos. Every animal has a name and a territory requirement (the amount of territory the animal needs to live). The territory requirement of an animal is by default 20.

When a zoo has enough free territory for the animal which we want to place there, then the zoo places the animal.

We also want to sell animals from a zoo to free up some territory to other animals. A zoo always sells the animal which requires the most territory. When a zoo sells an animal, it returns the sold animal and frees up its territory to be able to place new animals.

Using your solution, the following code should run without errors and print the expected results.

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
