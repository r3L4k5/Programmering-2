// Calculator.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <array>

using namespace std;




int main()
{
    double num1, num2;
    char opr = ' ';

    cout << endl << " Operation (+ - * /): ";
    cin >> opr;
    cout << endl;

    cout << " First number: ";
    cin >> num1;
    cout << endl;

    
    cout << " Second number: ";
    cin >> num2;
    cout << endl;

    int res = 0;

    switch (opr){

    case '+':
        res = num1 + num2;
        break;

    case '-':
        res = num1 - num2;
        break;

    case '*':
        res = num1 * num2;
        break;

    case '/':
        res = num1 / num2;
        break;

    default:
        cout << " Operation: '" << opr << "' is invalid!" << endl;
        return 0;
    }
    
    cout << " Result: " << res << endl;
    return 0;

}

