#include<iostream>

#include<cstdlib>

#include<ctime>

#include <string>

using namespace std;


void GameDetail(int maxTry);
string SecretWord();




int main(){

    int maxTries = 5;
    int RemainingTries = 5;
    char guessLetter;
    string SecretWord;
    int SecretWordLength;















    string SecretWord(){
                
        string animals[] = {"dog", "cat","hippo", "monkey", "alligator","lion","chimpanzee", "raccoon", "rabbit", "chicken"};

        srand(time(NULL));

        int word_length = *(&animals +1) - animals;
        
        int random_index = (rand() % 10);
        
        string word = animals[random_index];
        
        return word;
    }


    void GameDetail(int maxTries) {
            cout << "\n"
    "        .-------------------------------------------------------------------------------.\n"
    "        |      _      _                                                                  |\n"
    "        |     | |    | |   __ _    _ __      __ _        /\\/\\      __ _    _ __          |\n"
    "        |     | |----| |  / _  |  |  _ \\    / _` |      /    \\    / _  |  |  _  \\        |\n"
    "        |     | |----| | | (_| |  | | | |  | (_| |     / /\\/\\ |  | (_| |  | | | |        |\n"
    "        |     |_|    |_|  \\_ _ |  |_| |_|   \\__, |     \\/    \\/   \\_ _ |  |_| |_|        |\n"
    "        |                                    |___/                                       |\n"
    "        .--------------------------------------------------------------------------------.\n";

    cout << "The purpose of this game is to guess an animal name, secretly chosen by the application\n\n";
    cout << "You have to guess one letter at a time and you can have " << maxTries << " wrong attempts\n\n";
    cout << "Enter a lower-case letter and don't forget to enter key after each guess\n\n";
    cout << "Let's play the game!\n\n";
    }





}