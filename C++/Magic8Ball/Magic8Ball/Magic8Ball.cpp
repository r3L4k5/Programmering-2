

#include <iostream>


int stringToInt(std::string text) {

    int num = 0;

    for (int i = 0; i < std::size(text); i++) {

        num += int(text[i]);
    }

    return num;
}


int main(){

    const std::string affarmativeAnswers[3] = { "Definitevly", "Yes", "Correct" };
    const std::string nonCommitantAnswers[3] = { "Ask again", "Concentrate and try again", "Hazy reply" };
    const std::string negativeAnswers[3] = { "Negative", "Incorrect", "False" };

    while (true){

        std::string inquery;
        std::string answer;

        std::cout << " " << std::endl << std::endl << "Your inquery: ";
        std::cin >> inquery;

        std::srand(stringToInt(inquery));

        int typeOfAnswer = std::rand() % 3;

        switch (typeOfAnswer){

            case 0:
                answer = affarmativeAnswers[std::rand() % std::size(affarmativeAnswers)];
                break;

            case 1:
                answer = nonCommitantAnswers[std::rand() % std::size(nonCommitantAnswers)];
                break;

            case 2:
                answer = negativeAnswers[std::rand() % std::size(negativeAnswers)];
                break;

            default:
                break;
        }

        std::cout << " -" << answer;
    }
}