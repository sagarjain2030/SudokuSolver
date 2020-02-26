class SudokuStringValidator(object):
    def __init__(self):
        pass

    def checkLengthOfString(self,sudokuString):
        if(len(sudokuString) != 81):
            return False
        return True

    def inputOfString(self,sudokuString):
        possibleInputs = ['1','2','3','4','5','6','7','8','9','#']
        for elem in list(sudokuString):
            if elem not in possibleInputs:
                return False
        return True