
from os import system

from mammal import *
from animal import Sex, Habitat

#Different habitats with their repsective animals

rainforest = [ Primate("Gorrilla", Sex.MALE, Habitat.RAINFOREST, 1, 2, 1800),
               Primate("Orangutang", Sex.FEMALE, Habitat.RAINFOREST, 1, 2, 500),
               Primate("Chimpanzee", Sex.FEMALE, Habitat.RAINFOREST, 1, 2, 300),

               Carnivora("Tiger", Sex.MALE, Habitat.RAINFOREST, 8, 3, "Wild Pig")
               ]

forest = [ Rodent("Squirrel", Sex.FEMALE, Habitat.FOREST, 3, 4, 23), 
           Rodent("Mouse", Sex.MALE, Habitat.FOREST, 3, 4, 18),

           Carnivora("Wolf", Sex.MALE, Habitat.FOREST, 9, 6, "Deer"),
           Carnivora("Bear", Sex.MALE, Habitat.FOREST, 7, 2, "Salmon")
           ]

cave = [Chiroptera("Bat", Sex.FEMALE, Habitat.CAVE, 1, 2, 44)]

marsh = [Rodent("Capybara", Sex.MALE, Habitat.MARSH, 5, 4, 20)]


def show_animals(habitat):

    #Cleans up terminal and creates a top-margin
    system("cls"), print("\n")

    #Loops through and prints the aninmals in a a habitat
    for animal in habitat:
        print("You're seeing a " + animal.species, end="\n\n")

    input("Enter to go back... ")

    visit_habitat()


def visit_habitat():
    
    system("cls"), print("\n")

    #Displays all available habitats
    print("1. Rainforest", "2. Forest", "3. Cave", "4. Marsh", sep="  \n\n", end="\n\n")

    #Check if an int is inputted
    try:
        habitat_num = int(input("Enter number: "))
    except ValueError:
        print("\nEnter a number! ")
    
    #Different arguments passed based on habitat
    match habitat_num:
        
        case 1:
            show_animals(rainforest)

        case 2:
            show_animals(forest)

        case 3:
            show_animals(cave)

        case 4:
            show_animals(marsh)

        #Incase of unavailable number
        case _:
            input("\nInvalid habitat! ")
            visit_habitat()

visit_habitat()


