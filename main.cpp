// AI Disclaimer: This code was written with minimal AI assistance.
// Used AI for: workspace setup and boilerplates only.
// Core logic and problem-solving approach are my own work.

#include <iostream>

// Function declarations (required)
char calculateLetterGrade(double score);
void printTriangle(int height);

int main() {
    int choice = 0;
    while (true) {
        std::cout << "\n=== Grade Calculator & Star Triangle ===\n";
        std::cout << "1. Calculate Letter Grade\n";
        std::cout << "2. Print Triangle of Stars\n";
        std::cout << "3. Exit\n";
        std::cout << "Enter your choice (1-3): ";
        
        if (!(std::cin >> choice)) {
            std::cout << "Invalid input. Please try again.\n";
            std::cin.clear();
            std::cin.ignore(10000, '\n');
            continue;
        }

        if (choice == 3) {
            std::cout << "Goodbye!\n";
            break;
        } else if (choice == 1) {
            double score;
            std::cout << "Enter score (0.0-100.0): ";
            if (!(std::cin >> score) || score < 0.0 || score > 100.0) {
                std::cout << "Invalid input. Please try again.\n";
                std::cin.clear();
                std::cin.ignore(10000, '\n');
            } else {
                char grade = calculateLetterGrade(score);
                std::cout << "Score: " << score << " = Grade: " << grade << "\n";
            }
        } else if (choice == 2) {
            int height;
            std::cout << "Enter triangle height (1-20): ";
            if (!(std::cin >> height) || height < 1 || height > 20) {
                std::cout << "Invalid input. Please try again.\n";
                std::cin.clear();
                std::cin.ignore(10000, '\n');
            } else {
                printTriangle(height);
            }
        } else {
            std::cout << "Invalid input. Please try again.\n";
        }
    }
    return 0;
}

char calculateLetterGrade(double score) {
    // TODO: Implement grading logic:
    // A: 90.0 - 100.0, B: 80.0 - 89.9, C: 70.0 - 79.9, D: 60.0 - 69.9, F: 0.0 - 59.9
    if (score >= 90.0) return 'A';
    if (score >= 80.0) return 'B';
    if (score >= 70.0) return 'C';
    if (score >= 60.0) return 'D';
    return 'F';
}

void printTriangle(int height) {
    // TODO: Implement right-aligned triangle of '*'
    for (int i = 1; i <= height; ++i) {
        for (int j = 0; j < height - i; ++j) {
            std::cout << " ";
        }
        for (int j = 0; j < i; ++j) {
            std::cout << "*";
        }
        std::cout << "\n";
    }
}
