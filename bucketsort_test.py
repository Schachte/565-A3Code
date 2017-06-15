import unittest
from bucketsort import bucket_sort, check_list_of_numerics

'''
@Author: Ryan Schachte
@Description:   nlogn sorting algorithm. Partitions data elements into buckets
                and performs insertion sort on each bucket to yield a master
                sorted array.
@565 A1 Testing Implementation
@Implementation Ideas for Algorithm Gathered from the following sources:
    - http://www.programming-algorithms.net/article/41160/Bucket-sort
    - https://www.youtube.com/watch?v=VuXbEb5ywrU
    - https://stackoverflow.com/questions/10892677/optimal-bucket-size-and-no-of-buckets
    - https://www.youtube.com/watch?v=geVyIsFpxUs
'''

'''
Requirements:
'''

class BucketSortTestCase(unittest.TestCase):

    def test_empty_input_is_empty(self):
        '''Input empty list returns empty list'''

        #Empty list returns a valid empty list
        self.assertEqual([], bucket_sort([]))

    def test_input_is_list_of_numerics(self):
        '''Ensure that the input list contains only numeric values'''

        #Set of 1 valid int
        self.assertTrue(check_list_of_numerics([4]))

        #Multiple valid ints
        self.assertTrue(check_list_of_numerics([4, 50, 100, 55]))

        #Valid negative values
        self.assertTrue(check_list_of_numerics([-1]))

        #Valid list of float value
        self.assertTrue(check_list_of_numerics([65.7]))

    def test_input_not_a_list(self):
        '''Ensures TypeError is raised when input is not a list'''

        #Raises error on just an integer
        with self.assertRaises(TypeError):
            bucket_sort(0)

        #Raises error on just a string
        with self.assertRaises(TypeError):
            bucket_sort('f')

        #Raises error on just a tuple
        with self.assertRaises(TypeError):
            bucket_sort(())

        #Raises error on just a dictionary
        with self.assertRaises(TypeError):
            bucket_sort({})

    def test_input_fails_on_non_numerics(self):
        '''Ensure type error is raised when input list is filled with non-numerics'''

        #Raises error on list of string values
        with self.assertRaises(TypeError):
            bucket_sort(['1', '2', '4'])

        #Raises error on list of characters
        with self.assertRaises(TypeError):
            bucket_sort(['a', 'b', 'c'])

        #Raises error on list of characters
        with self.assertRaises(TypeError):
            bucket_sort([True])

        #Raises error on hex
        with self.assertRaises(TypeError):
            bucket_sort(["0x{0:04x}".format(42)])

    def test_input_fails_on_mixed_numerics(self):
        '''Ensure type error is raised when input list is filled with non-numerics AND numerics'''

        #Raises error on list of string values
        with self.assertRaises(TypeError):
            bucket_sort(['1', 2, '4'])

        #Raises error on list of string values
        with self.assertRaises(TypeError):
            bucket_sort(['a', 2, 'c'])

        #Raises error on list of string values
        with self.assertRaises(TypeError):
            bucket_sort([True, 1])

    def test_input_one_numeric_outputs_same_numeric(self):
        '''Inputting list of one integer/float outputs that same list'''

        #Test input variety 1
        self.assertEqual([1], bucket_sort([1]))

        #Test input variety 2
        self.assertEqual([-1], bucket_sort([-1]))

        #Test input variety 3
        self.assertEqual([55.6], bucket_sort([55.6]))


    def test_input_outputs_sorted_list(self):
        '''Ensures valid input of numerics outputs same list of sorted numerics'''

        #Sorted variety 1
        self.assertEqual([1,2,3,4,5], bucket_sort([5,4,3,2,1]))

        #Sorted variety 2
        self.assertEqual([134.0,2005.7,30000,40000,5000000], bucket_sort([5000000,2005.7,40000,134.0,30000]))

if __name__ == '__main__':
    unittest.main()
