# Makefile for CPSI-27603 Programming II C++ projects
# Enforces C++11 and strict warnings (no warning compiles, as required by the course)

CXX = g++
CXXFLAGS = -std=c++11 -Wall -Wextra -Werror

TARGET = main
SRC = main.cpp

.PHONY: all build run clean

all: build

build: $(SRC)
	@echo "Compiling $(SRC) to $(TARGET)..."
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)
	@echo "✓ Build successful."

run: build
	@echo "Executing $(TARGET)..."
	@./$(TARGET)

clean:
	@echo "Cleaning up build artifacts..."
	rm -f $(TARGET)
	@echo "✓ Cleanup complete."
