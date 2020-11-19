import math


class Matrix:
    def __init__(self, *args):
        self.rows = []
        for row in list(*args):
            self.rows.append(row)

    @staticmethod
    def from_values(*args):
        square = int(math.sqrt(len(args)))
        rows = []
        count = 0
        if square * square < len(args):
            square += 1
        for i in range(square):
            row = []
            for j in range(square):
                if count < len(args):
                    row.append(args[count])
                    count += 1
                else:
                    row.append(0)
            rows.append(row)
        return Matrix(rows)

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

    def do_operation(self, other, func):
        if isinstance(other, Matrix):
            new_matrix = Matrix()
            for i in range(len(self.rows)):
                row = []
                for j in range(len(self.rows[i])):
                    row.append(func(self.rows[i][j], other.rows[i][j]))
                new_matrix.rows.append(row)
            return new_matrix
        elif isinstance(other, int):
            new_matrix = Matrix()
            for i in range(len(self.rows)):
                row = []
                for j in range(len(self.rows[i])):
                    row.append(func(self.rows[i][j], other))
                new_matrix.rows.append(row)
            return new_matrix

    def __add__(self, other):
        return self.do_operation(other, lambda a, b: a + b)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self.do_operation(other, lambda a, b: a - b)

    def __rsub__(self, other):
        return self.do_operation(other, lambda a, b: b - a)

    def __mul__(self, other):
        return self.do_operation(other, lambda a, b: a * b)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self.do_operation(other, lambda a, b: a / b)

    def __rtruediv__(self, other):
        return self.do_operation(other, lambda a, b: b / a)

    def __repr__(self):
        return "\n".join([str(row) for row in self.rows])

    def __iter__(self):
        return iter(self.rows)


if __name__ == '__main__':
    matrix_from_values = Matrix.from_values(1, 2, 3, 4, 5)
    for number in matrix_from_values:
        print(number)

    matrix_from_list = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    for number in matrix_from_list:
        print(number)

    """
    Actually now I put use(test) cases in other file ;)
    """
