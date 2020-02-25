import unittest
from SudokuStringValidator import *

class Test_test_Sudoku(unittest.TestCase):
     def test_LengthSudokuString(self):
        requestedString = '2#############62####1####7###6##8###3###9###7###6##4###4####8####52#############3'
        s_test = SudokuStringValidator()
        self.assertTrue(s_test.checkLengthOfString(requestedString),msg='should return true')

if __name__ == '__main__':
    unittest.main()



