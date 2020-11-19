import numpy as np


class Matrix:
    def __init__(self, *args):
        self.rows = []
        for row in list(*args):
            self.rows.append(row)

    def __add__(self, other):
        if isinstance(other, Matrix):
            new_matrix = Matrix()
            for i in range(len(self.rows)):
                row = []
                for j in range(len(self.rows[i])):
                    row.append(self.rows[i][j] + other.rows[i][j])
                new_matrix.rows.append(row)
            return new_matrix
        elif isinstance(other, int):
            new_matrix = Matrix()
            for i in range(len(self.rows)):
                row = []
                for j in range(len(self.rows[i])):
                    row.append(self.rows[i][j] + other)
                new_matrix.rows.append(row)
            return new_matrix

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Matrix):
            new_matrix = Matrix()
            for i in range(len(self.rows)):
                row = []
                for j in range(len(self.rows[i])):
                    row.append(self.rows[i][j] - other.rows[i][j])
                new_matrix.rows.append(row)
            return new_matrix
        elif isinstance(other, int):
            new_matrix = Matrix()
            for i in range(len(self.rows)):
                row = []
                for j in range(len(self.rows[i])):
                    row.append(self.rows[i][j] - other)
                new_matrix.rows.append(row)
            return new_matrix

    def __rsub__(self, other):
        return self - other

    def __mul__(self, other):
        if isinstance(other, Matrix):
            new_matrix = Matrix()
            for i in range(len(self.rows)):
                row = []
                for j in range(len(self.rows[i])):
                    row.append(self.rows[i][j] * other.rows[i][j])
                new_matrix.rows.append(row)
            return new_matrix
        elif isinstance(other, int):
            new_matrix = Matrix()
            for i in range(len(self.rows)):
                row = []
                for j in range(len(self.rows[i])):
                    row.append(self.rows[i][j] * other)
                new_matrix.rows.append(row)
            return new_matrix

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, int):
            new_matrix = Matrix()
            for i in range(len(self.rows)):
                row = []
                for j in range(len(self.rows[i])):
                    row.append(self.rows[i][j] / other)
                new_matrix.rows.append(row)
            return new_matrix

    def __matmul__(self, other):
        new_matrix = Matrix()
        for i in range(len(self.rows)):
            row = []
            for j in range(len(self.rows[i])):
                mul_sum = 0
                for k in range(len(self.rows[i])):
                    mul_sum += self.rows[i][k] * other.rows[k][j]
                row.append(mul_sum)
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

    matrix3 = 10 - matrix1
    print_matrix("matrix3", matrix3)

    # arr1 = np.array([[1, 2],
    #                  [3, 4]])
    # arr2 = np.array([[1, 2],
    #                  [3, 4]])
    # arr1 = arr2 / arr1
    # print_matrix("arr1", arr1)

