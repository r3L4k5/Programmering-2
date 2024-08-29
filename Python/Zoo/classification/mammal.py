
from animal import Animal, Sex, Habitat


class Mammal(Animal):

    def __init__(self, species: str, sex: Sex, 
                habitat: Habitat, fertility: int, nipples: int):
        
        super().__init__(species, sex, habitat, fertility)

        self.nipples: int = nipples
    

class Rodent(Mammal):

    def __init__(self, species: str, sex: Sex, 
                habitat: Habitat, fertility: int, nipples: int):

        super().__init__(species, sex, habitat, fertility, nipples)


class Primate(Mammal):
    
    def __init__(self, species: str, sex: Sex, 
                habitat: Habitat, fertility: int, nipples: int):

        super().__init__(species, sex, habitat, fertility, nipples)


class Chiroptera(Mammal):

    def __init__(self, species: str, sex: Sex, 
                habitat: Habitat, fertility: int, nipples: int):

        super().__init__(species, sex, habitat, fertility, nipples)


class Carnivora(Mammal):

    def __init__(self, species: str, sex: Sex, 
                habitat: Habitat, fertility: int, nipples: int):

        super().__init__(species, sex, habitat, fertility, nipples)