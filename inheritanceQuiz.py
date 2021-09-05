class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    


coolguy = Person("Kenny", 22)




class Mutants(Person):
    def __init__(self, name, age, power, affiliation):
        self.power = power
        self.affiliation = affiliation
        Person.__init__(self, name, age)


class Avengers(Mutants):
    def __init__(self, name, age, power, affiliation):
        super().__init__(name, age, power, affiliation)
    

jeangrey = Mutants("Jean Grey", age= 23, power="Pheonix Force", affiliation="X-Men")
profX = Mutants("Charles Xavier", 45 ,"Telekinetic", "X-Men")
magneto = Mutants("Erik Lensherr", 45, "Magnetism", "Brotherhood of evil")
tony = Avengers("Tony Stark", 33, "Iron Man", "Avengers")

print('\n')


def printDetails(person):
    print(person.name)
    print(person.age)
    print(person.power)
    print(person.affiliation)
    print('\n')


printDetails(profX)
printDetails(magneto)
printDetails(tony)
printDetails(jeangrey)


