import unittest
from SudokuStringValidator import *

class Test_test_Sudoku(unittest.TestCase):
     def test_LengthSudokuString(self):
        requestedString = '2#############62####1####7###6##8###3###9###7###6##4###4####8####52#############3'
        s_test = SudokuStringValidator()
        self.assertTrue(s_test.checkLengthOfString(requestedString),msg='should return true')

     def test_inputOfString001(self):
        requestedString = '2#############62####1####7###6##8###3###9###7###6##4###4####8####52#############3'
        s_test = SudokuStringValidator()
        self.assertTrue(s_test.inputOfString(requestedString),msg='should return true')

     def test_inputOfString002(self):
        requestedString = '2##a##########62#$##1####7###6##8###3###9###7#0#6##4###4####8####52##B##########3'
        s_test = SudokuStringValidator()
        self.assertFalse(s_test.inputOfString(requestedString),msg='should return false')


if __name__ == '__main__':
    unittest.main()



