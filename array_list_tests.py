import unittest

class testCase(unittest.TestCase):
    def test_remove(self):
        t_listy = ListClass([0, 1, 2, 3], 5, 6)
        self.assertRaises(IndexError, remove, None, 2)

    def test_set(self):
        t_listy = ListClass([0, 1, 2, 3], 5, 6)
        self.assertEqual([5, 1, 2, 3], set(t_listy, 0, 5))

    def test_get(self):
        t_listy = ListClass([0, 1, 2, 3], 5, 6)
        self.assertEqual(1, get(t_listy, 1))

    def test_length(self):
        t_listy = ListClass([0, 1, 2, 3], 5, 6)
        self.assertEqual(4, length(t_listy))
        #print(length(t_listy))

    def test_add(self):
        t_listy = ListClass([0,1,2,3], 4, 6)
       # print(add(t_listy, 0, 1))

    def test_empty_list(self):
        self.assertEqual(ListClass([], 0, 0), empty_list())

    def test_List(self):
        self.assertEqual(ListClass(1, None, 1), ListClass(1, None, 1))


if (__name__ == '__main__'):
    unittest.main()