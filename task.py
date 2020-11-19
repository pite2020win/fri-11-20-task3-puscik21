class Matrix:
    def __init__(self, *args):
        self.rows = []
        for row in list(*args):
            self.rows.append(row)

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
    """
    Actually now I put use(test) cases in other file ;)
    """
    pass
