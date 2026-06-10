// AI Disclaimer: This code was written with minimal AI assistance.
// Used AI for: workspace setup and boilerplates only.
// Core logic and problem-solving approach are my own work.

#include <iostream>

// Function declarations (required)
int doubleValue(int x);
void echoWord();
void twoNumbers();

int main() {

  //   twoNumbers();

  //   echoWord();

  int x{};
  if (x = 10) {
  };

  return 0;
}

int doubleValue(int x) { return x * 2; }

void echoWord() {
  std::string word{};
  std::cin >> word;
  std::cout << "Your word is: " << word << std::endl;
}

void twoNumbers() {
  int first{}, second{};
  std::cout << "Enter two numbers separated by a space: ";
  std::cin >> first >> second;
  std::cout << std::endl
            << first << " + " << second << " = " << first + second << std::endl;
}