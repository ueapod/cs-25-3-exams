class Animal:
    def __init__(self, name, age, species, weight, diet):
        self.name = name
        self.age = age
        self.species = species
        self.weight = weight
        self.diet = diet

        
        
    def eat():
        if self.species == "травоядный":
            set.diet = "Трава"
        else:
            set.diet = "Мясо"



    def sleep():
        if self.age <= 10:
            print("Спать более 10 часов")
        elif self.age >= 10:
            print("Спать менее 10 часов")
        else:
            print("Спать около 8 часов")


    


    def get_descriptuon():
        break






    def is_adult():
        break




    def get_diet_info():
        break



class Dog(Animal):
    def __init__(self, name, age, species, weight, diet, breed):
        super().__init__(name, age, species, weight, diet)

        self.breed = breed
