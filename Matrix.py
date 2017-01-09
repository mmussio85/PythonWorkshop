from __future__ import division

class Matrix(object):
    def __init__(self, rows):
        self.rows = rows

    #PRIVATE OPS

    def __reduceMatrix(self, mat, i, j):
        return [row[:j] + row[j + 1:] for row in (mat[:i] + mat[i + 1:])]

    def __getDeterminant(self, mat):
        if len(mat) == 1:
            return mat[0][0]
        elif len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        else:
            return sum([((-1) ** col) * mat[0][col] * self.__getDeterminant(self.__reduceMatrix(mat, 0, col)) for col in range(len(mat))])
    def __getAdj(self, mat):
        if len(mat) == 1:
            return mat[0][0]
        elif len(mat) > 1:
            return Matrix([[((-1) ** (col + row) ) * self.__getDeterminant(self.__reduceMatrix(mat, row, col)) for col in range(len(mat))] for row in range(len(mat)) ])

    def sum(self, matrixB):
        return Matrix([[self.rows[i][j] + matrixB.rows[i][j] for j in range(len(self.rows[0]))] for i in range(len(self.rows))])

    def scalar(self, const):
        return Matrix([[self.rows[i][j] * const for j in range(len(self.rows[0]))] for i in range(len(self.rows))])

    def prod(self, matrixB):
        return Matrix([[sum(self.rows[i][k] * matrixB.rows[k][j] for k in range(len(self.rows[0]))) for j in
                        range(len(self.rows[0]))] for i in range(len(self.rows))])

    def trasp(self):
        return Matrix([[self.rows[j][i] for j in range(len(self.rows[0]))] for i in range(len(self.rows))])

    def determinant(self):
        return self.__getDeterminant(self.rows)

    def adj(self):
        return self.__getAdj(self.trasp().rows)

    def inv(self):
            if self.determinant() == 0:
                raise Exception("Matrix has no inverse.")
            else:
                t = 1.0 / self.determinant()
                adj = self.adj()
                return self.adj().scalar(1 / self.determinant())

    def getRows(self, listRows):
        result = list()
        for i in listRows:
            if self.rows[i - 1] not in result:
                result.append(self.rows[i - 1])
        return result

    def getColumns(self, listColumns):
        result = list()
        selectedColumns = [[row[j - 1] for row in self.rows ] for j in listColumns]
        for i in selectedColumns:
            if i not in result:
                result.append(i)
        return result

    def getMatrixFromColumn(self, initialX, initialY, height, width):
        selectedRows = list(range(initialX, initialX + height))
        rowFilteredMat = Matrix(self.getRows(selectedRows))
        selectedColumns = list(range(initialY, initialY + width))
        return Matrix(rowFilteredMat.getColumns(selectedColumns)).trasp()

    def __str__(self):
        return '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])


if __name__ == "__main__":
    matA = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print matA
    matB = Matrix([[2, -3, 8], [10, 11, 12], [3, 4, 5]])
    matC = Matrix([[2, 1, 0], [1, -1, 1], [0, 2, -1]])

    print matA.sum(matB)
    print matA.scalar(3)
    print matA.prod(matB)
    print matA.trasp()
    a = matB.determinant()
    b = matA.adj()
    print b
    a = matC.inv()
    print a.prod(matC)
    matD = Matrix([[2, 1, 0], [1, -1, 1], [2, 1, 0]])
    matD.getRows([1,2,3])
    matE = Matrix([[2, 1, 1], [1, 1, 1], [2, 1, 1]])
    print matE.getColumns([1, 2])
    matF = Matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], \
                   [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])

    print matF
    print matF.getMatrixFromColumn(2,2,2,2)




