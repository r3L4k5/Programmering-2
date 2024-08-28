
import copy

from enum import Enum, auto
from random import randint


class Sex(Enum):
    MALE = auto()
    FEMALE = auto()


class Habitat(Enum):
    SAVANN = auto()
    RAINFOREST = auto()
    TUNDRA = auto()
    SEA = auto()
    DEEPSEA = auto()
    TEMPERATE = auto()
    STEPPE = auto()
    MOUNTAIN = auto()


class Animal():

    def __init__(self, species: str, sex: Sex, habitat: Habitat, fertility: int):

        self.species: str = species
        self.sex: Sex = sex
        self.habitat: Habitat = habitat
        self.fertility: int = fertility
    
    #Check if they're the same species
    def __eq__(self, animal: object) -> bool:

        return self.species == animal.species

    #Breeding by adding to animals
    def __add__(self, partner):

        if self != partner or self.sex == partner.sex:
            return

        offsprings = []

        for _ in range(randint(1, self.fertility)):
            
            offsprings.append(copy.deepcopy(self))
        
        return offsprings
    
    def __str__(self) -> str:
        return self.species


Anim1 = Animal("Dog", Sex.MALE, Habitat.TEMPERATE, 5)
Anim2 = Animal("Dog", Sex.FEMALE, Habitat.TEMPERATE, 5)

children = Anim1 + Anim2
print(children[0])
     
        