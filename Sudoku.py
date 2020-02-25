from SudokuStringValidator import *

class Sudoku(object):
    """description of class"""
    def __init__(self,sudokuString):
        self.stringValidator = SudokuStringValidator()
        isValidString = self.stringValidator.checkLengthOfString(sudokuString)
        if(isValidString):
            self.sudokuString = sudokuString
        else:
            return False 

    def returnSudokuString(self):
        return self.sudokuString

    



