import numpy as np


class Matrix:
    def __init__(self, *args):
        self.rows = []
        for row in list(*args):
            self.rows.append(row)

    def __add__(self, other):
        new_matrix = Matrix()
        for i in range(len(self.rows)):
            row = []
            for j in range(len(self.rows[i])):
                row.append(self.rows[i][j] + other.rows[i][j])
            new_matrix.rows.append(row)
        return new_matrix

    def __repr__(self):
        return "\n".join([str(row) for row in self.rows])


def print_matrix(name, matrix):
    print("\n*** {} ***\n{}".format(name, matrix))


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2],
                      [3, 4]])
    matrix2 = Matrix([[2, 4],
                     [6, 8]])

    print_matrix("matrix1", matrix1)
    print_matrix("matrix2", matrix2)

    matrix3 = matrix1 + matrix2
    print_matrix("matrix3", matrix3)

# @ - dot product

# arr1 = np.array([[1, 2],
#                  [3, 4]])
# arr2 = np.array([[2, 4],
#                  [6, 8]])
#
# arr3 = arr1 * arr2
# arr4 = np.dot(arr1, arr2)
# print(arr1)
# print(arr2)
# print("arr3:\n{}".format(arr3))
# print("arr4:\n{}".format(arr4))

# Matrix.


# Write a class that can represent any 4𝑥4 real matrix.
# Include two functions to calculate the sum and dot product of two matrices.
# Next, write a program that imports this library module and use it to perform calculations.
# You CAN'T use numpy.
# Examples:
#
# matrix_1 = Matrix(4.,5.,6.,7.)
# matrix_2 = Matrix(2.,2.,2.,1.)
#
# matrix_3 = matrix_2 @ matrix_1
# matrix_4 = matrix_2 + matrix_1
# matrix_4 = 6 + matrix_1
# matrix_4 = matrix_1 + 6
#
# expand your solution to include other operations like
# - subtraction 
# - inversion
# - string representation 
#
# Try to expand your implementation as best as you can.
# Think of as many features as you can, and try implementing them.
# Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
# Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
# The goal of this task is for you to SHOW YOUR BEST python programming skills.
# Impress everyone with your skills, show off with your code.
#
# Your program must be runnable with command "python task.py".
# Show some usecases of your library in the code (print some things)
# Delete these comments before commit!
#
# Good luck.
