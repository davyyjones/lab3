#stuff

# an AnyList is one of
# - None
# - Pair(value, list)

class Pair:
    def __init__(self, first, rest):
        self.first = first # any value
        self.rest = rest   # any list
    def __eq__(self, other):
        return type(other) == Pair and self.first == other.first and self.rest == other.rest
    def __repr__(self):
        return ("%r, %r" % (self.first, self.rest))

# no arg -> emptylist
# Returns an empty list
def empty_list():
    return Pair(None, None)

# list index value - > list
# adds a value to a specific index of a list
def add(listy, index, thing, count =0):
    #if index < 0 or index > length(listy):
    if count == index:
        if listy == None:
            return Pair(thing, None)
        return Pair(thing, Pair(listy.first, listy.rest))
    if listy == None:
        if count == 0:
            return None
        raise IndexError
    count += 1
    return Pair(listy.first, add(listy.rest, index, thing, count))

# list - > number
# finds length of a list
def length(listy, len =0):
    if listy == None:
        return len
    return length(listy.rest, len+1)

# list index - > value
# finds the value of an index position in a list
def get(listy, index, count =0):



import unittest

class testCase(unittest.TestCase):

    def test_get(self):
        t_listy = Pair('Bob', Pair(42, Pair('socks', None)))
        self.assertRaises(IndexError, get, Pair('bob', None), 5)


    def test_length(self):
        t_listy = Pair('Bob', Pair(42, Pair('socks', None)))
        self.assertEqual(0, length(None))
        self.assertEqual(3, length(t_listy))

    def test_add(self):
        t_listy = Pair('Bob', Pair(42, Pair('socks', None)))
        self.assertEqual(Pair('Joe', Pair('Bob', Pair(42, Pair('socks', None)))), add(t_listy,0,'Joe'))
        self.assertEqual(Pair('Bob', Pair(42, Pair('socks', Pair('Joe', None)))), add(t_listy, 3, 'Joe'))
        self.assertEqual(Pair('Joe', None), add(None, 0, 'Joe'))
        self.assertEqual(None, add(None, 1, 'Joe'))
        self.assertRaises(IndexError, add, Pair('bob', None), 5, 'Joe')
        #print(add(Pair('bob', None), 5, 'Joe'))

    def test_empty_list(self):
        self.assertEqual(None, None, empty_list())

    def test_Pair(self):
        self.assertEqual(Pair(1, None), Pair(1, None))

if (__name__ == '__main__'):
        unittest.main()