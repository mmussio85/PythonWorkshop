# coding: utf-8

from Set import Set
import unittest
import subprocess


import subprocess

class TestPTree(unittest.TestCase):

    def testPtree(self):
        output = subprocess.check_output("python ..\PTree.py  .", shell=True)
        a = u'{0}'.format('.\n' + '├── '.decode('utf8') + 'TestEtlMovies.py\n' + '├── '.decode('utf8') + 'TestMatrix.py\n' + '├── '.decode('utf8') + 'TestPTree.py\n' + '├── '.decode('utf8') + 'TestSet.py\n' + '└── '.decode('utf8') + '__init__.py\n')
        b = u'{0}'.format(output.decode('utf-8'))
        self.assertTrue(a == b)



if __name__ == '__main__':
    unittest.main()