class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Happiness: {self.happiness}")
        return self

    def feed(self):
        self.health += 10
        self.happiness += 10
        return self
    
class Lion(Animal):
    def __init__(self, name, age, health=85, happiness=60):#lion attributes
        super().__init__(name, age, health, happiness)#common with super take super value
        self.mane_length = 20  # Unique attribute for Lion

    def display_info(self):
        super().display_info()
        print(f"Mane Length: {self.mane_length}")
        return self
    
    def feed(self):
        self.health += 12
        self.happiness += 8
        return self

class Tiger(Animal):
    def __init__(self, name, age, health=85, happiness=75):
        super().__init__(name, age, health, happiness)
        self.stripe_count =100  # Unique attribute for Tiger

    def display_info(self):
        super().display_info()
        print(f"Stripe Count: {self.stripe_count}")
        return self

    def feed(self):
        self.health += 10
        self.happiness += 10
        return self
    
class Bear(Animal):
    def __init__(self, name, age, health=90, happiness=80):
        super().__init__(name, age, health, happiness)
        self.cave_size = 50  # Unique attribute for Bear

    def display_info(self):
        super().display_info()
        print(f"Cave Size: {self.cave_size}")
        return self

    def feed(self):
        self.health += 8
        self.happiness += 12
        return self

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []# list
        self.name = zoo_name
    def add_lion(self, name,age):
        self.animals.append( Lion(name,age) )# method of the list object that adds a new element to the end of the list.
        return self
    def add_tiger(self, name,age):
        self.animals.append( Tiger(name,age) )
        return self
    def print_all_info(self):
        print("-"*25, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
        return self

zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala",5),zoo1.add_lion("Simba",3)
zoo1.add_tiger("Rajah",3).add_tiger("Shere Khan",7)
zoo1.print_all_info()
#Feed the animals
print("\nFeeding the animals...\n")
for animal in zoo1.animals:
    animal.feed()
zoo1.print_all_info()
