
import copy

from enum import Enum, auto
from random import randint, choice


class Sex(Enum):
    MALE = auto()
    FEMALE = auto()


class Habitat(Enum):
    SAVANN = auto()
    RAINFOREST = auto()
    TUNDRA = auto()
    FOREST = auto()
    STEPPE = auto()
    MOUNTAIN = auto()
    MARSH = auto()
    CAVE = auto()


class Animal():

    def __init__(self, species: str, sex: Sex, 
                habitat: Habitat, fertility: int):

        self.species: str = species
        self.sex: Sex = sex
        self.habitat: Habitat = habitat
        self.fertility: int = fertility

    
    #Check if they're the same species
    def __eq__(self, animal: object) -> bool:

        return self.species.lower() == animal.species.lower()


    #Breeding by adding to animals
    def __add__(self, partner):

        if self != partner or self.sex == partner.sex:
            raise ValueError("Failed to breed, either different species or same sex")

        #Random amount of offsprings between 50% and 133% of the average amount of offsprings birthed, a.k.a 'self.fertility'.
        #Rounded because no partial offsprings. Loops through the random amount of offsprings chosen
        #and creates a deepcopy that is appended to an 'offsprings' list which is returned at the end.
        #Randomizes sex by converting 'Sex' Enum into list and puttng it into 'choice()'
        
        offsprings = []
        
        for _ in range(randint(round(0.5 * self.fertility), round(1.5 * self.fertility))):
            
            birthed = copy.deepcopy(self)
            birthed.sex = choice(list(Sex))
            
            offsprings.append(birthed)
        
        return offsprings
    

    def __str__(self) -> str:
        return self.species

