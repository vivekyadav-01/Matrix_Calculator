print("----------MATRIX CALCULATOR------------")
import numpy as np
def input_matrix_function(name):
    print(f"\n----- Enter Details for Matrix {name} -----") 
    try:
        rows=int(input(f"Enter the number of rows for Matrix {name}: "))
        cols=int(input(f"Enter the number of columns for Matrix {name}: "))
        print("Enter the entries in a single line, separated by spaces (e.g., 1 2 3 4):")
        while(True):
            try:
                entries=list(map(float, input().split()))  
                if(len(entries)!=rows*cols):
                    print(f"Error: Expected {rows * cols} entries but got {len(entries)}. Please re-enter.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please ensure all entries are numbers separated by spaces.")
        matrix=np.array(entries).reshape(rows, cols)
        print(f"\nThe entered matrix {name} is:")
        print(matrix)
        return matrix
    except ValueError:
        print("Invalid input for rows/columns. Please enter integers.")
        return None
def inverse_function(matrix,name):
    if(matrix is None):
        return
    rows,cols=matrix.shape
    if(rows!=cols):
        print(f"Matrix {name} is not a square matrix. Inverse is not possible.")
        return
    determinant=np.linalg.det(matrix)
    print(f"\nDeterminant of Matrix {name} is: {determinant:.4f}")
    if(abs(determinant) > 1e-9):  
        matrix_inv=np.linalg.inv(matrix)
        print(f"The inverse matrix of {name} is:\n", matrix_inv)
    else:
        print(f"Matrix {name} is singular as Determinant is zero. Inverse is not possible.")
def transpose_function(matrix,name):
    if(matrix is None):
        return
    A_transpose=matrix.transpose()
    print(f"\nTranspose of Matrix {name} is:\n", A_transpose)
    return A_transpose
def addition_function(matrix_A, matrix_B):
    if(matrix_A is None or matrix_B is None):  
        return
    if(matrix_A.shape==matrix_B.shape):
        result_matrix=matrix_A+matrix_B
        print("\nThe sum of Matrix A and B is:\n", result_matrix)
    else:
        print("\nMatrix addition is not possible. Matrices must have the same dimensions.")
def subtraction_function(matrix_A, matrix_B):
    if(matrix_A is None or matrix_B is None):
        return
    if(matrix_A.shape==matrix_B.shape):
        result_matrix=matrix_A-matrix_B
        print("\nThe Subtraction (A - B) of Matrix A and B is:\n", result_matrix)
    else:
        print("\nMatrix subtraction is not possible. Matrices must have the same dimensions.")
def multiplication_function(matrix_A, matrix_B): 
    if(matrix_A is None or matrix_B is None):  
        return
    if(matrix_A.shape[1]==matrix_B.shape[0]):
        result_matrix=np.dot(matrix_A,matrix_B)
        print("\nThe Multiplication (A x B) of Matrix A and B is:\n", result_matrix)
    else:
        print("\nMatrix multiplication (A x B) is not possible. The number of columns in Matrix A must equal the number of rows in Matrix B.")
def identical_matrix_check(matrix_A, matrix_B):
    if(matrix_A is None or matrix_B is None): 
        print("Cannot check for equality: One or both matrices are invalid.")
        return     
    if(np.array_equal(matrix_A, matrix_B)):
        print("\n The matrices are Identical.")
    else:
        if(matrix_A.shape!=matrix_B.shape):
            print(f"\n The matrices are Not Identical because they have different dimensions: {matrix_A.shape} vs {matrix_B.shape}.")
        else:
            print("\n The matrices are Not Identical (same shape, but different elements).")
def matrix_calculator():
    matrix_A=input_matrix_function("A")
    if(matrix_A is None):
        print("\nProgram terminated due to invalid input for Matrix A.")
        print("\n--------Thank You for using Matrix Calculator----------")
        return
    print("\n----- Operations for Matrix A -----")
    try:
        if int(input("ENTER (1) IF YOU WANT INVERSE OF MATRIX A OTHERWISE (0):"))==1:
            inverse_function(matrix_A, "A")
        if int(input("ENTER (1) IF YOU WANT TRANSPOSE OF MATRIX A OTHERWISE (0):"))==1:
            transpose_function(matrix_A, "A")
    except ValueError:
        print(" Invalid input for choice. Skipping remaining Matrix A operations.")
    try:
        add_matrix_B_choice = int(input("\nIf you want to add another matrix (B) for combined operations (1), otherwise (0): "))
    except ValueError:
        print("Invalid input for choice. Skipping combined operations.")
        add_matrix_B_choice=0 
    if (add_matrix_B_choice==1):
        matrix_B=input_matrix_function("B")
        if (matrix_B is None):
            print("\nCombined operations skipped due to invalid input for Matrix B.")
        else:
            print("\n----- Operations for Matrix B and Combined Operations (A & B) -----")
            try:
                if int(input("ENTER (1) IF YOU WANT INVERSE OF MATRIX B OTHERWISE (0):"))==1:
                    inverse_function(matrix_B, "B")
                if int(input("ENTER (1) IF YOU WANT TRANSPOSE OF MATRIX B OTHERWISE (0):"))==1:
                    transpose_function(matrix_B, "B")
                if int(input("ENTER (1) IF YOU WANT Addition of Matrix A and B OTHERWISE (0):"))==1:
                    addition_function(matrix_A, matrix_B)
                if int(input("ENTER (1) If YOU WANT Subtraction of Matrix A and B (A-B) OTHERWISE (0):"))==1:
                    subtraction_function(matrix_A, matrix_B)
                if int(input("ENTER (1) IF YOU WANT Multiplication of Matrix A and B (A*B) OTHERWISE (0):"))==1:
                    multiplication_function(matrix_A, matrix_B)
                if int(input("ENTER (1) IF YOU WANT TO CHECK WHETHER Matrix A and Matrix b are Identical OTHERWISE (0):"))==1:
                    identical_matrix_check(matrix_A,matrix_B)
            except ValueError:
                print(" Invalid input for choice. Skipping remaining combined operations.")
    print("\n--------Thank You for using Matrix Calculator----------")
if __name__=="__main__":
    matrix_calculator()
