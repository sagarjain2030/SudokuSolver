import unittest
from Sudoku import Sudoku

class Test_test_Sudoku(unittest.TestCase):
    def test_checkSudokuString(self):
        requestedString = '2#############62####1####7###6##8###3###9###7###6##4###4####8####52#############3'
        s = Sudoku(requestedString)
        self.assertEqual(s.returnSudokuString(), requestedString,'should return requestedString')

if __name__ == '__main__':
    unittest.main()



