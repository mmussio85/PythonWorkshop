from __future__ import division

class Matrix(object):

    def __init__(self, rows):
        self.rows = rows

    '''Aux methods '''

    def __reduceMatrix(self, mat, i, j):
        '''Reduce the matrix removing the current row and column.
        Args:
            mat: The matrix.
            i: Row number.
            j: Column number

        Returns:
            A reduced matrix.
        '''

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
        '''Get rows without repetition.
        Args:
            listRows: the rows to be retrieved
        Returns:
            a list of rows
        '''

        result = list()
        for i in listRows:
            if self.rows[i - 1] not in result:
                result.append(self.rows[i - 1])
        return result

    def getColumns(self, listColumns):
        '''Get columns without repetition.
        Args:
            listColumns: the columns to be retrieved
        Returns:
            a list of columns
        '''

        result = list()
        selectedColumns = [[row[j - 1] for row in self.rows ] for j in listColumns]
        for i in selectedColumns:
            if i not in result:
                result.append(i)
        return result

    def getMatrixFromColumn(self, initialX, initialY, height, width):
        '''Get matrix by column.
        Args:
            initialX: row of the top left element in the matrix.
            initialY: column of the top left element in the matrix..
            height: height of the desired matrix.
            width: with of the desired matrix.

        Returns:
            a matrix with dimensions <height, width> and top left item in <initialX, initialY>.
        '''

        if (len(self.rows) == 0) or (initialX + height > len(self.rows)) or (initialY + width > len(self.rows[0])):
            raise Exception('Wrong matrix dimensions.')
        else:
            selectedRows = list(range(initialX, initialX + height))
            rowFilteredMat = Matrix([self.rows[i - 1] for i in selectedRows ])
            selectedColumns = list(range(initialY, initialY + width))
            return Matrix([[rowFilteredMat.rows[i][j - 1] for j in selectedColumns ] for i in range(len(rowFilteredMat.rows))  ])

    def __str__(self):
        return '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
