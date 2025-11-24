# 🧮 Matrix Calculator Project Statement

## 1. Problem Statement

Performing complex matrix operations manually or validating homework/research results for linear algebra problems can be tedious and prone to human error. There is a need for a **simple, reliable, and command-line accessible tool** that can accept matrix input with robust validation and execute fundamental matrix algebra functions—such as inversion, transposition, and combined operations (addition, subtraction, multiplication)—while ensuring mathematical prerequisites (like dimension matching) are met.

---

## 2. Scope of the Project

The scope of this project is to deliver a functional **Command-Line Interface (CLI)** application built in Python, leveraging the **NumPy library** to handle core mathematical computations.

The project encompasses:
* **Input Management:** Guided user input for matrix dimensions and elements, including multi-stage validation for data type and element count.
* **Fundamental Operations:** Implementation of core matrix operations (Inverse, Transpose, Addition, Subtraction, Multiplication).
* **Prerequisite Checking:** Automated checking of mathematical conditions (e.g., matrix shape for multiplication, square matrix for inverse) before attempting a calculation, providing clear error messages when operations are impossible.
* **Identity Check:** Functionality to compare two matrices for absolute equality.

The project **does not** cover advanced linear algebra topics such as eigenvalues, eigenvectors, LU decomposition, or symbolic computation.

---

## 3. Target Users

The primary target users for this Matrix Calculator include:

* **Students:** Those studying linear algebra, matrix theory, calculus, or engineering who need to practice, calculate, or verify their matrix-related assignments.
* **Educators:** Teachers and professors needing a quick, reliable tool to generate examples or check solutions for exams and lectures.
* **Engineers & Data Scientists:** Professionals who need to perform quick, ad-hoc matrix manipulations without launching a dedicated scientific computing environment.

---

## 4. High-Level Features

The application provides a guided, interactive workflow with the following high-level features:

### 📥 Input & Validation
* **Guided Input:** Step-by-step prompts for inputting up to two matrices (A and B).
* **Robust Error Handling:** Catches `ValueError` exceptions for non-integer dimension inputs and non-numerical element inputs, prompting the user for correction.
* **Dimension Check:** Ensures the number of provided elements exactly matches $rows \times cols$.

### ⚙️ Single-Matrix Operations
| Feature | Details |
| :--- | :--- |
| **Inverse Calculation** | Calculates $A^{-1}$ after checking for **square dimensions** and **non-singularity** ($\det(A) \neq 0$). |
| **Transpose Calculation** | Calculates $A^T$. |

### ➕ Combined Matrix Operations
| Feature | Details |
| :--- | :--- |
| **Addition/Subtraction** | Calculates $A \pm B$, only if matrices have **identical dimensions**. |
| **Multiplication** | Calculates $A \times B$, only if $C_A$ (columns of A) equals $R_B$ (rows of B). |
| **Identity Check** | Compares $A$ and $B$ to determine if they are **identical** (same shape and element values). |