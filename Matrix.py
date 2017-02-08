from __future__ import division

class Matrix(object):

    def __init__(self, rows):
        self.rows = rows
        self.__checkValidMatrix()
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
        '''Get the Determinant of the matrix.
        Args:
            mat: The matrix.
        Returns:
            The determinant of the matrix.
        '''

        if len(mat) == 1:
            return mat[0][0]
        elif len(mat) == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        else:
            return sum([((-1) ** col) * mat[0][col] * self.__getDeterminant(self.__reduceMatrix(mat, 0, col)) for col in range(len(mat))])

    def __getAdj(self, mat):
        '''Get de adjoint matrix.
        Args:
            mat: The matrix.
        Returns:
            A reduced matrix.
        '''

        if len(mat) == 1:
            return mat[0][0]
        elif len(mat) > 1:
            return Matrix([[((-1) ** (col + row) ) * self.__getDeterminant(self.__reduceMatrix(mat, row, col)) for col in range(len(mat))] for row in range(len(mat)) ])

    def __checkValidMatrix(self):
        '''Check if the matrix has the correct dimensions.
        Returns:
            True if the matrix has the correct dimensions, otherwise returns False.
        '''

        if len(self.rows) < 1:
            raise Exception("Matrix entered in an incorrect format.")
        else:
            if not(reduce(lambda x, y: x and y,
                          map(lambda x: True if len(x) == len(self.rows[0]) else False, self.rows))):
                raise Exception("Matrix entered in an incorrect format.")

    def sum(self, matrixB):
        '''Sum two matrices.
        Args:
            matrixB: The matrix.
        Returns:
            The sum of both matrices.
        '''

        if not ((len(self.rows) != len(matrixB.rows)) or (len(self.rows[0]) == len(matrixB.rows[0]))):
            raise Exception("Matrices do not have the same dimensions.")
        else:
            return Matrix([[self.rows[i][j] + matrixB.rows[i][j] for j in range(len(self.rows[0]))] for i in range(len(self.rows))])

    def scalar(self, const):
        '''Product between a matrix and a scalar.
        Args:
            const: The const scalar.
        Returns:
            The sum of both matrices.
        '''

        return Matrix([[self.rows[i][j] * const for j in range(len(self.rows[0]))] for i in range(len(self.rows))])

    def prod(self, matrixB):
        '''Product between two matrices.
        Args:
            matrixB: The matrix.
        Returns:
            The product of both matrices.
        '''

        if (len(self.rows[0]) != len(matrixB.rows)):
            raise Exception("Matrices cannot be multiplicated.")
        else:
            return Matrix([[sum(self.rows[i][k] * matrixB.rows[k][j] for k in range(len(self.rows[0]))) for j in
                        range(len(matrixB.rows[0]))] for i in range(len(self.rows))])

    def trasp(self):
        '''Transpose the matrix.
        Returns:
            The tespose matrix.
        '''

        return Matrix([list(i) for i in zip(*self.rows)])

    def determinant(self):
        '''Get the Determinant of the matrix(starts base excecution of the recursion).
        Returns:
            The determinant of the matrix.
        '''

        return self.__getDeterminant(self.rows)

    def adj(self):
        '''Get de adjoint matrix(starts base excecution of the recursion).
        Returns:
            A reduced matrix.
        '''

        return self.__getAdj(self.trasp().rows)

    def inv(self):
        '''Inverse of the matrix.
        Returns:
            The inverse matrix.
        '''

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
            if i < 1 or i > len(self.rows):
                raise Exception('{0} {1} {2}'.format("The row ", i, "does not belong into the matrix range."))
            else:
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
        for i in listColumns:
            if i < 1 or i > len(self.rows[0]):
                raise Exception('{0} {1} {2}'.format("The columnn ", i, "does not belong into the matrix range."))
        selectedColumns = [[row[j - 1] for row in self.rows] for j in listColumns]
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

        if (len(self.rows) == 0) or (height < 0 or height >  len(self.rows) and width < 0 or width > len(self.rows[0])) \
                or (initialX + height - 1 > len(self.rows)) or (initialY + width - 1 > len(self.rows[0])):
            raise Exception('Wrong matrix dimensions.')
        else:
            selectedRows = list(range(initialX - 1, initialX + height - 1))
            rowFilteredMat = Matrix([self.rows[i] for i in selectedRows ])
            selectedColumns = list(range(initialY, initialY + width))
            return Matrix([[rowFilteredMat.rows[i][j - 1] for j in selectedColumns ] for i in range(len(rowFilteredMat.rows))  ])

    def __str__(self):
        return '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
if __name__ == '__main__':
    a = Matrix([])

    print a
