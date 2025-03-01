# Program

> **The main purpose of this program is to apply all the Linear Algebra concepts we have learned at Tishk International University, Computer Engineering, 2nd grade so far.**

## Workflow

The program first tells you to enter a method to test:

### Solve linear equations:
It will ask you for to choose a method to solve with, either *Gauss-Jordan* or *Cramer's rule*, and then it will ask you to enter the amount of variables and equations you have to check if it is conveninent to find a solution or not, after that, it will ask you to enter the matrices and their values, and solve by the method.

* Gauss-Jordan:
Works by firstly, **forward elimination**, that basically eliminates everything starting on the left side, and before *(row = column)*, which will result in finding the value of the last variable. And secondly, by finding the value of the last variable, we then, can find the other values through **backward substitution**, basically substituting the value in other equations to find the rest of the values.

* Cramer's rule:
Works by finding the determinant for the original matrix first, and then loops (from 0 to how many variables we have), everytime it loops, it creates a temporary matrix and substitute the equations results in a specific column in the original matrix, and then find the temporary matrix's determinant, then divide the temporary determinant by the original determinant to find the value for the corresponding variable to which column we have substituted the equations results.

### Matrix Addition
Takes two matrices, add them in a third matrix, and then return the third matrix.

### Matrix Subtraction
Takes two matrices, subtract them in a third matrix, and then return the third matrix.

### Matrix Multiplication
Takes two matrices, multiply the row of the first matrix by the column of the second matrix, add them in a third matrix, and then return the third matrix.

### Matrix Multiplication by scalar
Takes one matrix and a scalar, multiplies the scalar by all the rows and columns inside the matrix, and then return the new matrix.

### Matrix Transpose
Takes one matrix, swaps the rows and columns, stores the new values in a second matrix, and then return the second matrix.

### Matrix Determinant
Takes one matrix, finds the determinant by using NumPy. You can find it by finding the minors and cofactors and following the **a(1,1)c(1,1) + a(2,2)c(2,2) + a(3,3)c(3,3) + a(n,n)c(n,n)**, where a is the original value in the original matrix, c is the corresponding value in the cofactor matrix (This can be done for one row), and then return the new matrix.

### Matrix Inverse
Takes one matrix, stores the determinant of the original matrix,finds the minors and cofactor for it using **Cij=(−1)^i+j * det(Aij)**, then finds the transpose of the cofactor matrix to get the adjoint, applies **1/|det(A)| * adj(A)**, stores the value in a new matrix, and then return the new matrix.

### Matrix Eigen Value and Eigen Vectors
Takes one matrix, finds the eigen values, store them in a variable called **(w)**, then finds the eigen vectors, store them in a variable called **(v)**, all by using NumPy, and then return the matrices **(w)** and **(v)**
