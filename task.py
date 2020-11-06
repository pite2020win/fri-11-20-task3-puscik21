class Matrix:
    def __init__(self, *args):
        self.rows = []
        for row in args:
            self.rows.append(row.numbers)

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.rows)):
            new_matrix.append(self.rows[i] + other.rows[i])
        return new_matrix

    def __repr__(self):
        return "\n".join([str(row) for row in self.rows])


class Row:
    def __init__(self, *args):
        self.numbers = args


if __name__ == '__main__':
    row1 = Row(1, 2, 3, 4)
    row2 = Row(1, 2, 3, 4)
    row3 = Row(1, 2, 3, 4)
    row4 = Row(1, 2, 3, 4)
    matrix1 = Matrix(row1, row2, row3, row4)
    matrix2 = Matrix(row1, row2, row3, row4)

    matrix1 = matrix1 + matrix2
    print(matrix1)

