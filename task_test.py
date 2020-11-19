from task import Matrix
import numpy as np
import unittest


class TaskTest(unittest.TestCase):
    def setUp(self) -> None:
        data1 = np.random.randint(1, 10, size=(4, 4))
        data2 = np.random.randint(1, 10, size=(4, 4))
        self.matrix1 = Matrix(data1)
        self.matrix2 = Matrix(data2)
        self.np_matrix1 = np.array(data1)
        self.np_matrix2 = np.array(data2)

    def test_add_matrix(self):
        res = self.matrix1 + self.matrix2
        np_res = self.np_matrix1 + self.np_matrix2
        self.assertCountEqual(res.rows, np_res.tolist())

    def test_add_number(self):
        number = np.random.randint(10)
        res = self.matrix1 + number
        np_res = self.np_matrix1 + number
        self.assertCountEqual(res.rows, np_res.tolist())

    def test_add_number_rev(self):
        number = np.random.randint(10)
        res = number + self.matrix1
        np_res = number + self.np_matrix1
        self.assertCountEqual(res.rows, np_res.tolist())

    def test_sub_matrix(self):
        res = self.matrix1 - self.matrix2
        np_res = self.np_matrix1 - self.np_matrix2
        self.assertCountEqual(res.rows, np_res.tolist())

    def test_sub_number(self):
        number = np.random.randint(10)
        res = self.matrix1 - number
        np_res = self.np_matrix1 - number
        self.assertCountEqual(res.rows, np_res.tolist())

    def test_sub_number_rev(self):
        number = np.random.randint(10)
        res = number - self.matrix1
        np_res = number - self.np_matrix1
        self.assertCountEqual(res.rows, np_res.tolist())

    def test_mul_matrix(self):
        res = self.matrix1 * self.matrix2
        np_res = self.np_matrix1 * self.np_matrix2
        self.assertCountEqual(res.rows, np_res.tolist())

    def test_mul_number(self):
        number = np.random.randint(10)
        res = self.matrix1 * number
        np_res = self.np_matrix1 * number
        self.assertCountEqual(res.rows, np_res.tolist())

    def test_mul_number_rev(self):
        number = np.random.randint(10)
        res = number * self.matrix1
        np_res = number * self.np_matrix1
        self.assertCountEqual(res.rows, np_res.tolist())

    def test_div_matrix(self):
        res = self.matrix1 / self.matrix2
        np_res = self.np_matrix1 / self.np_matrix2
        self.assertCountEqual(res.rows, np_res.tolist())

    def test_div_number(self):
        number = np.random.randint(1, 10)
        res = self.matrix1 / number
        np_res = self.np_matrix1 / number
        self.assertCountEqual(res.rows, np_res.tolist())

    def test_div_number_rev(self):
        number = np.random.randint(10)
        res = number / self.matrix1
        np_res = number / self.np_matrix1
        self.assertCountEqual(res.rows, np_res.tolist())

    def test_mat_mul(self):
        res = self.matrix1 @ self.matrix2
        np_res = np.dot(self.np_matrix1, self.np_matrix2)
        self.assertCountEqual(res.rows, np_res.tolist())


if __name__ == '__main__':
    unittest.main()
