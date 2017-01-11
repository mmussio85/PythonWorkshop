from __future__ import division
from Matrix import Matrix

import unittest

class TestMatrix(unittest.TestCase):

    def testAdd(self):
        matA = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        matB = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        self.assertTrue(matA.sum(matB).getRows([1,2,3]) == [[2,3, 4], [5, 6, 7], [8, 9, 10]])

    def testScalar(self):
        matA = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertTrue(matA.scalar(1/2).getRows([1,2,3]) == [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0], [3.5, 4.0, 4.5]])

    def testProd(self):
        matA = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertTrue(matA.prod(matA).getRows([1,2,3]) == [[30, 36, 42], [66, 81, 96], [102, 126, 150]])

    def testTrasp(self):
        matA = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertTrue(matA.trasp().getRows([1,2,3]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def testDeterminant(self):
        matA = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
        self.assertTrue(matA.determinant() == 0)

    def testGetRows(self):
        matA = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        self.assertTrue(matA.getRows([1, 2, 3]) == [[1, 1, 1]])

    def testAdj(self):
        matA = Matrix([[1, 2, 3], [4, 8, 6], [12, 8, 9]])
        self.assertTrue(matA.adj().getRows([1,2,3]) == [[24, 6, -12], [36, -27, 6], [-64, 16, 0]])

    def testGetMatrixFromColumn(self):
        matA = Matrix([[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]])
        self.assertTrue(matA.getMatrixFromColumn(initialX=2,initialY=2, height=3, width=3).getRows([1,2,3]) == [[2, 2, 2], [3, 3, 3], [4, 4, 4]])

    def testInv(self):
        matA = Matrix([[1, 2, 3], [0, 1, 2], [1, 2, 4]])
        matAinv = matA.inv()
        c = matA.prod(matAinv).getRows([1,2,3])
        self.assertTrue(matA.prod(matAinv).getRows([1,2,3]) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    def testGetMatrixFromColumnException(self):
        with self.assertRaises(Exception):
            matA = Matrix([[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]])
            matA.getMatrixFromColumn(initialX=2,initialY=2, height=3, width=10)

    def testGetColumn(self):
        matA = Matrix([[1, 1, 1, 1, 1], [2, 2, 2, 5, 2], [3, 3, 3, 5, 3], [3, 3, 3, 5, 3], [5, 5, 5, 5, 5]])
        self.assertTrue(matA.getColumns([3,4,5]) == [[1, 2, 3, 3, 5], [1, 5, 5, 5, 5]])

if __name__ == '__main__':
    unittest.main()