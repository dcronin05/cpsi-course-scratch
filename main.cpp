// AI Disclaimer: This code was written from scratch with ai
// assistance to setup the environment. I also consulted deeply
// with ai in a separate session that had access to the code
// but was never allowed to modify it. I asked questions and
// then manually implemented or didn't implement suggested changes.
// The IDE I wrote in didn't have ai context for it's autocomplete,
// but I it did give me extensive autocomplete help with loop
// declaration and other boilerplate stuff.

#include <iostream>
#include <limits>
#include <string>

const std::string MENU_HEADER = "=== Grade Calculator & Star Triangle ===";
const std::string MENU_CHOICES =
    "1. Calculate Letter Grade\n2. Print Triangle of Stars\n3. Exit";
const std::string PROMPT_CHOICE = "Enter your choice (1-3): ";
const std::string INVALID_CHOICE = "Invalid input. Please try again.";
const std::string PROMPT_SCORE = "Enter score (0.0-100.0): ";
const std::string PROMPT_TRIANGLE_HEIGHT = "Enter triangle height (1-20): ";

void printMenu();
int getValidatedMenuChoice();

char calculateLetterGrade(double score);
double getValidatedScore();
void printGrade(double score);

void printTriangle(int height);
int getValidatedTriangleHeight();

int getValidInput(const std::string &prompt, int min, int max);
double getValidInput(const std::string &prompt, double min, double max);

int main() {
  while (true) {
    printMenu();
    int choice = getValidatedMenuChoice();

    switch (choice) {
    case 1: {
      double score = getValidatedScore();
      printGrade(score);
      break;
    }
    case 2: {
      int height = getValidatedTriangleHeight();
      printTriangle(height);
      break;
    }
    case 3:
      std::cout << "Goodbye!" << std::endl;
      return 0;
    }
  }

  return 0;
}

// 1. Menu Functions
void printMenu() {
  std::cout << MENU_HEADER << std::endl;
  std::cout << MENU_CHOICES << std::endl;
}

int getValidatedMenuChoice() {
  int choice = getValidInput(PROMPT_CHOICE, 1, 3);

  return choice;
}

// 2. Grade Calculator Functions
char calculateLetterGrade(double score) {
  if (score >= 90) {
    return 'A';
  } else if (score >= 80) {
    return 'B';
  } else if (score >= 70) {
    return 'C';
  } else if (score >= 60) {
    return 'D';
  } else {
    return 'F';
  }
}

double getValidatedScore() {
  double score = getValidInput(PROMPT_SCORE, 0.0, 100.0);

  return score;
}

void printGrade(double score) {
  char letterGrade = calculateLetterGrade(score);
  std::cout << "Score: " << score << " = Grade: " << letterGrade << std::endl;
}

// 3. Triangle Functions
void printTriangle(int height) {
  for (int i{0}; i < height; ++i) {
    std::cout << std::string(height - i - 1, ' ');
    std::cout << std::string(i + 1, '*');
    std::cout << std::endl;
  }
}

int getValidatedTriangleHeight() {
  int height = getValidInput(PROMPT_TRIANGLE_HEIGHT, 1, 20);

  return height;
}

// 4. Input Validation Helpers
int getValidInput(const std::string &prompt, int min, int max) {
  double val = getValidInput(prompt, static_cast<double>(min), static_cast<double>(max));

  if (val != static_cast<int>(val)) {
    std::cout << INVALID_CHOICE << std::endl;
    return getValidInput(prompt, min, max);
  }

  return static_cast<int>(val);
}

double getValidInput(const std::string &prompt, double min, double max) {
  std::cout << prompt;

  double input{};
  if ((std::cin >> input).fail() || input < min || input > max ||
      std::cin.peek() != '\n') {
    std::cout << INVALID_CHOICE << std::endl;
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    input = getValidInput(prompt, min, max);
  }

  return input;
}
