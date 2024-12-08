
from animal import Animal, Sex, Habitat

class Fish(Animal):

    def __init__(self, species: str, sex: Sex, habitat: Habitat, fertility: int, fins: int ):
        
        super().__init__(species, sex, habitat, fertility)

