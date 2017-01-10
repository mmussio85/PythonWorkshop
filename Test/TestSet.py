from Set import Set
import unittest

class TestSet(unittest.TestCase):

    def testAdd(self):
        newSet = Set([1, 2, 3, 4, 1, 3, 7])
        newSet.add(8)
        setB = Set([8])
        self.assertTrue(setB.isIncluded(newSet))

    def testRemove(self):
        newSet = Set([1, 2, 3, 4, 1, 3, 7])
        newSet.remove(1)
        setB = Set([1])
        self.assertFalse(setB.isIncluded(newSet))

    def testDiff(self):
        newSet = Set([1, 2, 3, 4, 1, 3, 7])
        setB = Set([2, 3])
        self.assertTrue(newSet.diff(setB) == [1,  4,  7])

    def testIncluded(self):
        newSet = Set([1, 2, 5])
        setB = Set([2,3,1,6,2, 5])
        self.assertTrue(newSet.isIncluded(setB))

    def testIntersection(self):
        newSet = Set([3,4,5,8])
        setB = Set([1,7,3,8,3])
        self.assertTrue(newSet.intersection(setB) == setB.intersection(newSet) and newSet.intersection(setB) == [3, 8])

    def testDiffSim(self):
        newSet = Set([1, 2, 3, 4, 1, 3, 7])
        setB = Set([2, 8, 9])
        self.assertTrue(newSet.diffSim(setB) == [1,  3,  4, 7, 8, 9])

    def testProdCart(self):
        newSet = Set([1, 2, 3, 4, 1, 3, 7])
        newSetB = Set([1, 2, 3, 4, 1, 8, 3, 7])
        self.assertTrue(newSet.prodCart(newSetB) == [(1, 1), (1, 2), (1, 3), (1, 4), (1, 8), (1, 7), (2, 1), (2, 2),
                                                     (2, 3), (2, 4), (2, 8), (2, 7), (3, 1), (3, 2), (3, 3), (3, 4),
                                                     (3, 8), (3, 7), (4, 1), (4, 2), (4, 3), (4, 4), (4, 8), (4, 7),
                                                     (7, 1), (7, 2), (7, 3), (7, 4), (7, 8), (7, 7)])

    def testPot(self):
        newSet = Set([1, 2, 3, 4, 1, 8, 3, 7])
        self.assertTrue((newSet.pot() == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4],
                                         [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4], [8], [1, 8], [2, 8],
                                         [1, 2, 8], [3, 8], [1, 3, 8], [2, 3, 8], [1, 2, 3, 8], [4, 8], [1, 4, 8],
                                         [2, 4, 8], [1, 2, 4, 8], [3, 4, 8], [1, 3, 4, 8], [2, 3, 4, 8], [1, 2, 3, 4, 8],
                                         [7], [1, 7], [2, 7], [1, 2, 7], [3, 7], [1, 3, 7], [2, 3, 7], [1, 2, 3, 7],
                                         [4, 7], [1, 4, 7], [2, 4, 7], [1, 2, 4, 7], [3, 4, 7], [1, 3, 4, 7],
                                         [2, 3, 4, 7], [1, 2, 3, 4, 7], [8, 7], [1, 8, 7], [2, 8, 7], [1, 2, 8, 7],
                                         [3, 8, 7], [1, 3, 8, 7], [2, 3, 8, 7], [1, 2, 3, 8, 7], [4, 8, 7], [1, 4, 8, 7],
                                         [2, 4, 8, 7], [1, 2, 4, 8, 7], [3, 4, 8, 7], [1, 3, 4, 8, 7], [2, 3, 4, 8, 7],
                                         [1, 2, 3, 4, 8, 7]]) and len(newSet.pot()) == 2 ** len(newSet.diff(Set([]))))

if __name__ == '__main__':
    unittest.main()