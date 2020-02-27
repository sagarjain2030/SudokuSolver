import unittest
from Util import *

class Test_test_Sudoku(unittest.TestCase):
    def test_cross(self):
        crossList = cross('123','456')
        x = set(crossList)
        referList =['14','15','16','24','25','26','34','35','36'] 
        y = set(referList)
        z = x.difference(y)
        self.assertEqual(not x.difference(y),True,'something wrong with cross function')
        
if __name__ == '__main__':
    unittest.main()
