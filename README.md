# Matrix_Calculator
This project is a Python-based interactive matrix calculator designed to help users perform essential matrix operations directly through the terminal. It supports creating matrices, validating inputs, and executing various operations such as inverse, transpose, addition, subtraction, and multiplication.
# Matrix Calculator

## Project Title
Matrix Calculator – Interactive Command-Line Matrix Operation Tool

## Overview
This project is a Python-based interactive matrix calculator designed to help users perform essential matrix operations directly through the terminal. It supports creating matrices, validating inputs, and executing various operations such as inverse, transpose, addition, subtraction, and multiplication.

The program guides the user step-by-step, making it suitable for beginners learning matrix concepts and Python programming.

## Features
- Interactive input system for matrix creation
- Input validation for dimensions and numerical entries
- Supports core matrix operations:
  - Matrix Inverse
  - Matrix Transpose
  - Matrix Addition
  - Matrix Subtraction
  - Matrix Multiplication
- Handles errors such as:
  - Non-square matrix for inverse
  - Mismatched dimensions for addition/subtraction
  - Invalid multiplication dimensions
- Clean and user-friendly terminal prompts

## Technologies / Tools Used
- **Python 3**
- **NumPy** for numerical operations
- Standard I/O for user interaction

## Steps to Install & Run the Project
Follow these steps to set up and execute the program:

### 1. Install Python
Ensure Python 3.x is installed.

### 2. Install Required Library
Open a terminal and run:
```bash
pip install numpy
```

### 3. Save the Program
Copy the provided code into a file named:
```
matrix_calculator.py
```

### 4. Run the Program
Execute the script using:
```bash
python matrix_calculator.py
```

## Instructions for Testing
Use the following steps to test all functionalities:

1. **Run the program** and enter valid dimensions (e.g., 2×2, 3×3).
2. **Enter matrix values** in one line as prompted.
3. **Test individual operations**:
   - Enter `1` or `0` when asked to compute inverse or transpose.
4. **Test combined operations** by selecting option to enter Matrix B.
5. **Try mismatched matrices** to verify error messages:
   - Different-sized matrices for addition/subtraction
   - Invalid dimensions for multiplication
6. **Test with singular matrices** (determinant = 0) to validate inverse error handling.




---
