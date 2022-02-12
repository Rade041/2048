""" Test for the core 2048 functions"""

import unittest

import core

class TestStackLeft(unittest.TestCase):

    def test_empty(self):
        """An empty row is unaffect by a move """
        result = core.stack_left([None, None, None, None])
        self.assertEqual(result, [None, None, None, None])


    def test_one_value(self):
        "A single non-None tile should be moved to the left" 
        result = core.stack_left([None, None, 2, None]) 
        self.assertEqual(result, [2, None, None, None])


    def test_two_values(self):
        "Two non-None tiles should retain their order" 
        result = core.stack_left([None, 2, None, 4])
        self.assertEqual(result, [2, 4, None, None])

    def test_three_values(self):
        "Three non-None tiles should retain their order" 
        result = core.stack_left([None, 2, 4, 2]) 
        self.assertEqual(result, [2, 4, 2, None])

    def test_four_values(self):
        "All non-None tiles should not move" 
        result = core.stack_left([4, 2, 4, 2])
        self.assertEqual(result, [4, 2, 4, 2])

class TestMergeLeft(unittest.TestCase):
    
    def test_empty(self):
        """An Empty Row is unaffected by a merge"""
        result = core.merge_left([None, None, None, None])
        self.assertEqual(result, [None, None, None, None])

    def test_one_value(self):
        """An Single value is unaffected by a merge"""
        result = core.merge_left([2, None, None, None])
        self.assertEqual(result, [2, None, None, None])

    def test_all_different(self):
        """Different values are unaffected by a merge"""
        result = core.merge_left([2, 4, 8, 16])
        self.assertEqual(result, [2, 4, 8, 16])

    def test_one_pair(self):
        """A Single pair is simple"""   
        result = core.merge_left([2, 2, None, None])
        self.assertEqual(result, [4, None, None, None])

    def test_value_before_pair(self):
        """"Simple merge with an additional tile to the left"""
        result = core.merge_left([4, 2, 2, None])
        self.assertEqual(result, [4, 4, None, None])

    def test_value_after_pair(self):
        """"Simple merge with an additional tile to the right """   
        result = core.merge_left([2, 2, 2, None])
        self.assertEqual(result, [4, None, 2, None])

    def test_larger_numbers(self):
        """A  Large pair with two tile to the left"""
        result = core.merge_left([64, 128, 256, 256])
        self.assertEqual(result, [64, 128, 512, None])

    def test_two_pairs(self):
        """Two pairs leaves a gap"""
        result = core.merge_left([2, 2, 2, 2])
        self.assertEqual(result, [4, None, 4, None])


    def merge_left(stacked_row):
        """Merge similar non-None items to the left"""
        for i in range(3):
            if stacked_row[i] and stacked_row[i] == stacked_row[i+1]:
                stacked_row[i] *= 2
                stacked_row[i + 1] = None
        return stacked_row
   




class TestMoveLeft(unittest.TestCase):
    
    def test_value_pair(self):
        input= [[None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None]]


        self.assertEqual(core.move_left(input),input)

    def test_empty(self):
        """The additional tile should be stacked into the merged pair"""
        input= [[None, 4, 4, 8],
                [2, None, 2, 2]
                [None, 2, 2, 2]
                [16, None, 16, 4]]

        expected = [[8, 8, None, None],
            [4, 2, None, None],
            [4, 2, None, None]
            [32, 4, None, None]]

        self.assertEqual(core.move_left(input),expected)

    def test_empty(self):
        """Two pairs are both merged and stacked"""
        input= [[2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2]]

        expected = [[4, 4, None, None],
            [4, 4, None, None],
            [4, 4, None, None],
            [4, 4, None, None]] 

        self.assertEqual(core.move_left(input),expected)

class TestTranspose(unittest.TestCase):
    """Transpose should flip the grid on the diagonal"""
    def test (self):
        input = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

        output = [[1, 5, 9, 13],
            [2, 6, 10, 14],
            [3, 7, 11, 15],
            [4, 8, 12, 16]]

        self.assertEqual(core.transpose(input),output)



if __name__ =='__main__':
    unittest.main ()

