class SudokuStringValidator(object):
    def __init__(self):
        pass

    def checkLengthOfString(self,sudokuString):
        if(len(sudokuString) != 81):
            return False
        return True
