
#include <iostream>
#include <string>


std::string toRobberLanguage(std::string text) {
    
    char vowels[9] = {'a', 'e', 'i', 'o', 'u', 'y'};

    std::string result;
    
    for (char letter : text ) {
        
        bool isVowel = false;
        
        for (char vowel : vowels) {
            
            if (letter == vowel) {
                
                isVowel = true;
            }
        }
        
        if (isVowel) {
            result += letter;
        }

        else {
            result += letter;
            result += 'o';
            result += letter;
        }
        
    }
    
    return result;
}


int main() {
    
    while (true) {

        std::string input;
        std::cin >> input;
        
        std::cout << toRobberLanguage(input) << std::endl;
    }

    return 0;
}