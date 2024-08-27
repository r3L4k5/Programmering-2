
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
        self.offsprings: list = []
        self.fertility: int = fertility
    
    def __eq__(self, animal: object) -> bool:

        return self.species == animal.species

    def __add__(self, partner):

        if self != partner or self.sex == partner.sex:
            return

        for _ in range(randint(1, self.fertility)):
            
            self.offsprings.append(copy.deepcopy(self))
        
        
        