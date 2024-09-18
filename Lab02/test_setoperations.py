# test_setoperations.py
import unittest
from setoperations import make_set, is_set, union, intersection



class TestSetOperations(unittest.TestCase):

    def test_make_set(self):
        self.assertEqual(make_set([1, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_is_set(self):
        self.assertTrue(is_set([1, 2, 3, 4, 5]))
        self.assertFalse(is_set([5, 5]))
        self.assertTrue(is_set([]))
        self.assertFalse(is_set(None))

    def test_union(self):
        self.assertEqual(union([1,2], [2,3]), [1,2,3])
        self.assertEqual(union([], [2,3]), [2,3])
        self.assertEqual(union([1,1,1], [2,3]), [])

    def test_intersection(self):
        self.assertEqual(intersection([1,2], [2,3]), [2])
        self.assertEqual(intersection([], [2,3]), [])
        self.assertEqual(intersection([1,1,1], [2]), [])
        self.assertEqual(intersection([1,2,3], [4,5,6]), [])
        self.assertEqual(intersection([1,2,3], [3,4,5]), [3])


if __name__ == '__main__':
    unittest.main()