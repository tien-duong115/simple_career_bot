#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{   
  string firstname, lastname;
  cout << "enter your firstname: ";
  cin >> firstname;
  cout << "enter your lastname: ";
  cin >> lastname;

  cout << "your full name is "<< firstname << " " << lastname << "-->";
  return 0;
}