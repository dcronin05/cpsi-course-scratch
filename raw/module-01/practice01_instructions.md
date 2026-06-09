[Video: Programming 2: How to use GitHub and Codespace?](https://youtube.com/watch?v=ADncVDH2wLo)

###

### Practice Assignment: Module 1 - C++ Fundamentals Review

#### Overview

Create a **C++ console menu application** with two options:

- **Option 1**: Calculate a letter grade from a numeric score
- **Option 2**: Print a right-aligned triangle made of * characters

This practice focuses on **functions**, **input validation**, **control flow**, and **consistent output formatting**.

##### Learning Objectives

- Implement functions with proper parameters and return types
- Handle user input and menu selection
- Use control structures (if/else, loops)
- Format output consistently
- Practice modular program organization (functions + a clean main loop)

#### Instructions

- Create **one C++ program** with a repeating menu
- Implement the required functions exactly as specified
- Validate input and handle invalid selections gracefully
- After finishing an option, return to the menu until the user exits
- Use proper C++ conventions (**std:: prefix**, no using namespace std;)

#### File Naming and Submission

##### GitHub Classroom Link

Complete this practice through **GitHub Classroom**. 👉 **GitHub Classroom Assignment Link:** [https://classroom.github.com/a/iSUGhlbp](https://classroom.github.com/a/iSUGhlbp)

**EDIT: There seems to be an issue for some people. If you have issues go to **[**https://github.com/settings/organizations**](https://github.com/settings/organizations)** and accept my class. Then try the link again. I will send you an invite to your email once I see your github username.  Be sure to accept the invite so you don't have to do this again.**

##### File Naming

- **Main Program:** main.cpp

##### AI Disclaimer Requirement

**CRITICAL:** Your main.cpp must include an AI Disclaimer at the top. The autograder may look for this exact phrase.

**Examples of AI Disclaimers (choose one, or write your own):**

**No AI Use:**

```cpp
// AI Disclaimer: This code was written without the use of AI tools.
// Any assistance received was from course materials, textbooks, or instructor guidance only.


```

**Minimal AI Use (e.g., syntax help, debugging):**

```cpp
// AI Disclaimer: This code was written with minimal AI assistance.
// Used AI for: syntax checking and debugging only.
// Core logic and problem-solving approach are my own work.

```

**Moderate AI Use (e.g., structure suggestions):**

```cpp
// AI Disclaimer: This code was written with moderate AI assistance.
// Used AI for: code structure suggestions and algorithm guidance.
// I implemented the solutions and modified the AI suggestions to fit the requirements.

```

##### Submission Process

1. Create main.cpp
2. Commit and push to GitHub
3. Submit your repository URL on Blackboard (or the course submission system)

**Example repository URL (what to submit):** https://github.com/Seward-Classes/practice-01-username

**Important:** Submit the **repository link**, not a link to:

- A specific file (example of what *not* to submit): https://github.com/Seward-Classes/practice-01-username/blob/main/main.cpp
- A Codespace (Codespaces links are typically **private** and the instructor/autograder cannot access them)

#### Practice 01: Menu Application

#### Requirements

##### 1. Menu System

Your program must:

- Display a menu with numbered options
- Loop back to the menu after each operation
- Handle invalid menu input gracefully
- Allow users to exit the program

##### 2. Letter Grade Calculator (Option 1)

##### Required Function

```cpp
char calculateLetterGrade(double score);

```

##### Behavior

- **Input range**: 0.0 to 100.0 (inclusive)
- **Reject** scores outside this range
- **Grading scale**:
- A: 90.0 – 100.0
- B: 80.0 – 89.9
- C: 70.0 – 79.9
- D: 60.0 – 69.9
- F: 0.0 – 59.9
- **Output format** (exact):
- Score: [score] = Grade: [letter]

##### 3. Triangle of Stars (Option 2)

##### Required Function

```cpp
void printTriangle(int height);

```

##### Behavior

- **Input range**: 1 to 20 (inclusive)
- **Reject** heights outside this range
- Print a **right-aligned** triangle of * characters

Example for height 4:

```cpp
   *
  **
 ***
****

```

##### 4. Main Function Requirements

You must implement:

```cpp
int main();

```

##### Behavior

- Return 0 for successful execution
- Keep looping until the user chooses to exit
- For invalid selections or invalid values, display:
- Invalid input. Please try again.
- Exit option must display:
- Goodbye!

##### 5. Input/Output Specifications

##### Menu Display

```cpp
=== Grade Calculator & Star Triangle ===
1. Calculate Letter Grade
2. Print Triangle of Stars
3. Exit
Enter your choice (1-3):

```

##### Prompts

- Enter your choice (1-3):
- Enter score (0.0-100.0):
- Enter triangle height (1-20):

##### Error Message

- Invalid input. Please try again.

##### Function Signatures (Required)

```cpp
char calculateLetterGrade(double score);
void printTriangle(int height);
int main();

```

#### Example Output

##### Menu Display

```cpp
=== Grade Calculator & Star Triangle ===
1. Calculate Letter Grade
2. Print Triangle of Stars
3. Exit
Enter your choice (1-3):

```

##### Letter Grade Example

```cpp
Enter score (0.0-100.0): 87.5
Score: 87.5 = Grade: B

```

##### Triangle Example

```cpp
Enter triangle height (1-20): 4
   *
  **
 ***
****

```

##### Error Handling Examples

```cpp
Enter score (0.0-100.0): 150
Invalid input. Please try again.
Enter triangle height (1-20): 25
Invalid input. Please try again.
Enter your choice (1-3): 5
Invalid input. Please try again.

```

#### Technical Requirements

- **Language**: C++ (C++11 or later)
- **Compilation**: Must compile with g++ **without warnings**
- **File structure**: Single main.cpp file
- **No external libraries**: Use only standard C++ libraries
- **All functions implemented in the same file**

#### Submission Checklist

- [ ] Created main.cpp
- [ ] Included AI disclaimer at the top of main.cpp
- [ ] Menu prints in the exact required format
- [ ] Option 1 calls calculateLetterGrade(double score)
- [ ] Score validation rejects values outside 0.0–100.0
- [ ] Grade output matches: Score: [score] = Grade: [letter]
- [ ] Option 2 calls printTriangle(int height)
- [ ] Height validation rejects values outside 1–20
- [ ] Triangle is right-aligned and matches the example formatting
- [ ] Exit option (3) prints Goodbye!
- [ ] Invalid selections/values print Invalid input. Please try again.
- [ ] Code uses std:: prefix (no using namespace std;)
- [ ] Program compiles and runs without warnings
- [ ] Committed and pushed to GitHub, and submitted the repo link

#### Getting Started Tips

1. Build the menu loop in main() first (print menu → read choice → switch/if)
2. Implement calculateLetterGrade next and test with boundary scores (59.9, 60.0, 69.9, 70.0, etc.)
3. Implement printTriangle and test with heights 1, 4, and 20
4. Add input validation and ensure the program returns to the menu after each operation
