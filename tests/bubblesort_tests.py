import sys
import unittest
sys.path.append('../SortingAlgos/')
from SortingAlgos import bubblesort
import testdata as td

class TestBubblesort(unittest.TestCase):

    def test1(self):
        self.assertEqual(bubblesort(td.input1, td.intcomp), td.expected1, td.msg1)

    def test2(self):
        self.assertEqual(bubblesort(td.input2, td.intcomp), td.expected2, td.msg2)

    def test3(self):
        self.assertEqual(bubblesort(td.input3, td.intcomp), td.expected3, td.msg3)
    
    def test4(self):
        self.assertEqual(bubblesort(td.input4, td.intcomp), td.expected4, td.msg4)

    def test5(self):
        self.assertEqual(bubblesort(td.input5, td.stringcomp), td.expected5, td.msg5)
    
    def test6(self):
        self.assertEqual(bubblesort(td.input6, td.stringcomp), td.expected6, td.msg6)

if __name__ == '__main__':
    unittest.main()