
#include <iostream>
#include <vector>
#include <sstream>
#include <random>


std::string randomObject() {

    int probability = rand() % 100 + 1;

    if ( probability <= 3) {

        //Rock
        return "()";
    
    } else if (probability <= 40) {

        //Tree
        return " T";

    } else {

        //Grass
        return " ;";
    }
}


std::vector<std::vector<std::string>> createWorld() {

    std::vector<std::vector<std::string>> world(20, std::vector<std::string> (50, ""));

    for (int y = 0; y < world.size(); y++) {

        for (int x = 0; x < world[y].size(); x++) {

            world[y][x] = randomObject();
        }
    }

    return world;
}


void displayWorld(std::vector<std::vector<std::string>> world) {

    for (std::vector<std::string>& row : world) {

        std::cout << std::endl;

        for (std::string& tile : row) {
            
            std::cout << tile;
        }
    }
}


void listen() {

    int x;

    std::cout << std::endl;
    std::cin >> x;
}


int main() {

    std::srand(time(0));

    displayWorld(createWorld());

    listen();

}