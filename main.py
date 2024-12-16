import numpy as np
import math

# A method that retrieves 3 matrices, taking the input from the user
def linear_equation_input(equations, variables):
    final_variables = np.array(np.zeros((variables, 1)))
    final_results = np.array(np.zeros((equations,1)))
    final_numbers = np.array(np.zeros((variables,equations)))
    for i in range(0,equations):
        final_results[i,0] = float(input(f"Enter result for equation {i+1}: "))
        for x in range(0, variables):
            final_numbers[i,x] = float(input(f"Enter number for equation {i+1} variable {x+1}: "))
    return final_variables, final_results, final_numbers
            

def gauss_jordan(equations, variables):
    final_variables, final_results, final_numbers = linear_equation_input(equations, variables)
    
    # Declaring n, and m to shorten our code, Didn't utilize it well, unfortunately
    n = len(final_results)
    m = n - 1
    final_concate = np.concatenate((final_numbers, final_results), axis=1, dtype = float)

    # Forward elimination, to eliminate all numbers below the first row
    for i in range(len(final_results-1)):
            for j in range(i+1, len(final_results)):
                if final_concate[i,i] != 0:
                    final_concate[j,:] = final_concate[j,:] - (final_concate[j,i] / final_concate[i,i]) * final_concate[i,:]

    # Finding the last variable
    final_variables[m] = final_concate[m][n] / final_concate[m][m]

    # Backward substitution, to find the rest of the variables using the last variable
    for k in range(n - 2, -1, -1):
        final_variables[k] = final_concate[k][n]
        for l in range(k + 1, n):
            final_variables[k] = final_variables[k] - final_concate[k][l] * final_variables[l]
        final_variables[k] = final_variables[k] / final_concate[k][k]
        
    print("Final result",final_variables)

    return final_variables
    
def cramer_rule(equations, variables):
    final_variables, final_results, final_numbers = linear_equation_input(equations, variables)

    # Determinant of the main matrix
    a_det = np.linalg.det(final_numbers)

    # Substitution of the final results in the main matrix
    n = len(final_results)
    for i in range(0, n):
        tempMatrix = np.copy(final_numbers)
        for j in range(0, n):
            tempMatrix[j][i] = final_results[j]
            final_variables[i] = np.linalg.det(tempMatrix) / a_det # Determinant of the substituted matrix / determinant of the main matrix to find the result for the variable

    print("Final result",final_variables)
        
    return final_variables

def matrixAdd():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    matrix1 = np.array(np.zeros((rows,columns)))
    matrix2 = np.array(np.zeros((rows,columns)))
    matrix3 = np.array(np.zeros((rows,columns)))
    for i in range(0, rows):
        for j in range(0, columns):
            matrix1[i][j] = float(input(f"Enter row {i+1} column {j+1} for matrix 1: "))
            matrix2[i][j] = float(input(f"Enter row {i+1} column {j+1} for matrix 2: "))
            matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
    
    print(f"Final result: {matrix3}")
    return matrix3

def matrixSub():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    matrix1 = np.array(np.zeros((rows,columns)))
    matrix2 = np.array(np.zeros((rows,columns)))
    matrix3 = np.array(np.zeros((rows,columns)))
    for i in range(0, rows):
        for j in range(0, columns):
            matrix1[i][j] = float(input(f"Enter row {i+1} column {j+1} for matrix 1: "))
            matrix2[i][j] = float(input(f"Enter row {i+1} column {j+1} for matrix 2: "))
            matrix3[i][j] = matrix1[i][j] - matrix2[i][j]
    
    print(f"Final result: {matrix3}")
    return matrix3


def matrixMul():
    rows1 = int(input("Enter the number of rows for matrix 1: "))
    columns1 = int(input("Enter the number of columns matrix 1: "))
    rows2 = int(input("Enter the number of rows for matrix 2: "))
    columns2 = int(input("Enter the number of columns matrix 2: "))
    if(columns1 != rows2):
        print("Invalid, columns of matrix 1 must equal rows of matrix 2")
    
    matrix1 = np.array(np.zeros((rows1,columns1)))
    matrix2 = np.array(np.zeros((rows2,columns2)))
    for i in range(0, rows1):
        for j in range(0, columns1):
            matrix1[i][j] = float(input(f"Enter row {i+1} column {j+1} for matrix 1: "))
    
    for i in range(0, rows2):
        for j in range(0, columns2):
            matrix2[i][j] = float(input(f"Enter row {i+1} column {j+1} for matrix 2: "))
    matrix3 = np.array(np.zeros((rows1,columns2)))

    for i in range(0, rows1):
        for j in range(0, columns2):
            for k in range(0, columns1):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]

    print(f"Final result: {matrix3}")
    
    return matrix3

def matrixMulScalar():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    scalar = int(input("Enter the scalar: "))
    matrix1 = np.array(np.zeros((rows,columns)))
    for i in range(0, rows):
        for j in range(0, columns):
            matrix1[i][j] = float(input(f"Enter row {i+1} column {j+1}: ")) * scalar
    
    print(f"Final result: {matrix1}")
    return matrix1

def matrixTranspose():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    matrix1 = np.array(np.zeros((rows,columns)))
    matrix2 = np.array(np.zeros((rows,columns)))
    for i in range(0, rows):
        for j in range(0, columns):
            matrix1[i][j] = float(input(f"Enter row {i+1} column {j+1}: "))
    
    for i in range(0, rows):
        for j in range(0, columns):
            matrix2[i][j] = matrix1[j][i]
    
    print(f"Final result: {matrix2}")
    return matrix2

def matrixDeterminant():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    matrix1 = np.array(np.zeros((rows,columns)))
    for i in range(0, rows):
        for j in range(0, columns):
            matrix1[i][j] = float(input(f"Enter row {i+1} column {j+1}: "))
    
    print(f"Final result: {np.linalg.det(matrix1)}")
    return np.linalg.det(matrix1)

def matrixInverse():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    matrix1 = np.array(np.zeros((rows,columns)))
    cofactor = np.array(np.zeros((rows,columns)))
    for i in range(0, rows):
        for j in range(0, columns):
            matrix1[i][j] = float(input(f"Enter row {i+1} column {j+1}: "))

    for i in range(0, rows):
        for j in range(0, columns):
            minor = np.delete(np.delete(matrix1, i, 0), j, 1)
            cofactor[i][j] = np.linalg.det(minor) * (-1) ** (i + j)

    matrixInverse = np.transpose(cofactor) / np.linalg.det(matrix1)
    print(f"numpy result: {np.linalg.inv(matrix1)}")
    print(f"Final result: {matrixInverse}")
    return matrixInverse

def matrixEigenValues():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    matrix1 = np.array(np.zeros((rows,columns)))
    for i in range(0, rows):
        for j in range(0, columns):
            matrix1[i][j] = float(input(f"Enter row {i+1} column {j+1}: "))
    
    print(f"Final result: {np.linalg.eig(matrix1)}")
    return np.linalg.eig(matrix1)

def matrixEigenVectors():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    matrix1 = np.array(np.zeros((rows,columns)))
    for i in range(0, rows):
        for j in range(0, columns):
            matrix1[i][j] = float(input(f"Enter row {i+1} column {j+1}: "))
    
    print(f"Final result: {np.linalg.eig(matrix1)}")
    return np.linalg.eig(matrix1)

def main():
    option = int(input("Enter 0.Solve linear equations 1.Matrix addition 2.Matrix subtraction 3.Matrix multiplication\n4.Matrix multiplication scalar 5.Matrix transpose 6.Matrix determinant 7.Matrix inverse\n8.Matrix eigen values 9.Matrix eigen vectors: "))

    match (option):
        case 0:
            option2 = int(input("Enter 1.Gauss Jordan 2.Cramer Rule: "))
            equations = int(input("Enter number of equations: "))
            variables = int(input("Enter number of variables: "))
            if equations != variables:
                print("Invalid input, equations must best equal to variables")
                return
    
            if option2 == 1:
                gauss_jordan(equations, variables)
            elif option2 == 2:
                cramer_rule(equations, variables)
            else:
                print("Invalid option")
        case 1: 
            matrixAdd()
        case 2:
            matrixSub()
        case 3:
            matrixMul()
        case 4:
            matrixMulScalar()
        case 5:
            matrixTranspose()
        case 6:
            matrixDeterminant()
        case 7:
            matrixInverse()
        case 8:
            matrixEigenValues()
        case 9:
            matrixEigenVectors()
        case _:
            print("Invalid option")

main()