import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        #It passes a None type to make sure the function catches it properly
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        #Passes an empty list and tests if the function catches it properly
        self.assertEqual(max_list_iter([]), None)
        #Checks if the function itself finds the maxiumum integer and returns it, with the list containing positive, negative, and identical numbers
        self.assertEqual(max_list_iter([2,1,1,5,8,8,-2,-203,-941]), 8)
        self.assertEqual(max_list_iter([-448,-203,-941]), -203)
        #Checks when the list just has one element
        self.assertEqual(max_list_iter([4]),4)

    def test_reverse_rec(self):
        #Checks if the function itself works and returns a reversed list
        t_list = reverse_rec([8,-2,5,9])
        self.assertEqual(t_list,[9,5,-2,8])
        self.assertEqual(reverse_rec([5,4,3]),[3,4,5])
        #Checks if the function catches a None type
        t2_list = None
        with self.assertRaises(ValueError):
            reverse_rec(t2_list)


    def test_bin_search(self):
        #Checks if function returns the index of the target number even with repeating numbers. It will return the first index in which that repeating number appears
        list_val =[0,1,2,3,4,4,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        self.assertEqual(bin_search(8, 2, 6, list_val), 6)
        #Checks if the function can find a value at index 0 because if there wasn't another variable that stayed constant, the function would loop forever
        self.assertEqual(bin_search(0, 0, 6, list_val), 0)
        #Checks if the function catches a None type
        list2_val = None
        with self.assertRaises(ValueError):
            bin_search(5, 0, 4, list2_val)
        #Checks if the function returns a None type if it can't find the target
        list3_val = [-2,3,6,9,10]
        self.assertEqual(bin_search(4, 2, 3, list3_val), None)
        #Checks if the function works with float median values
        self.assertEqual(bin_search(10, 1, 4, list3_val), 4)
        self.assertEqual(bin_search(7, 0, 5, [4,5,1,3,5,7]),5)

if __name__ == "__main__":
        unittest.main()

    
