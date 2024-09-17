
from animal import Animal, Sex, Habitat


class Mammal(Animal):

    def __init__(self, species: str, sex: Sex, 
                habitat: Habitat, fertility: int, nipples: int):
        
        super().__init__(species, sex, habitat, fertility)

        self.nipples: int = nipples
    

class Rodent(Mammal):

    def __init__(self, species: str, sex: Sex, 
                habitat: Habitat, fertility: int, nipples: int, tooth: int):
        
        super().__init__(species, sex, habitat, fertility, nipples)

        self.tooth = tooth


class Primate(Mammal):
    
    def __init__(self, species: str, sex: Sex, 
                habitat: Habitat, fertility: int, nipples: int, strength: int):

        super().__init__(species, sex, habitat, fertility, nipples)

        self.strength = strength


class Chiroptera(Mammal):

    def __init__(self, species: str, sex: Sex, 
                habitat: Habitat, fertility: int, nipples: int, wing_span: int):

        super().__init__(species, sex, habitat, fertility, nipples)

        self.wing_span = wing_span


class Carnivora(Mammal):

    def __init__(self, species: str, sex: Sex, 
                habitat: Habitat, fertility: int, nipples: int, prey: str):

        super().__init__(species, sex, habitat, fertility, nipples)

        self.prey = prey