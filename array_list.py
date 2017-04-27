
class ListClass:
    def __init__(self, array, length, capacity):
        self.array = array
        self.length = length
        self.capacity = capacity

    def __eq__(self, other):
        return ((type(other) == ListClass)
          and self.array == other.array
          and self.length == other.length
          and self.capacity == other.capacity
        )

    def __repr__(self):
        return ("ListClass({!r}, {!r}, {!r})".format(self.array, self.length, self.capacity))

# None - > list
# returns an empty list
def empty_list():
    return ListClass([], 0, 0)

# list index value - > list
# adds a value at an index in a list
def add(listy, index, value):
    #capacity stuff
    listy.array = [] * listy.capacity
    cur_index = listy.length - 1
    if index > listy.length:
        raise IndexError
    while (cur_index > index):
        listy.array[cur_index +1] = listy.array[cur_index]
        cur_index -= 1
    listy.array[cur_index + 1] = listy.array[cur_index]
    listy.array[cur_index] = value
    return listy.array

# list - > value
# finds the length of a list
def length(listy, len=0):
    if listy == None or listy.array == None:
        return len
    for i in listy.array:
        len +=1
    return len

# list index - > value
# finds the value of a list at an index
def get(listy, index, count =0):
    if listy == None:
        raise IndexError
    for i in listy.array:
        if count == index:
            return i
        count += 1

# list index value - > list
# sets an index to the specified value
def set(listy, index, value, count=0):
    if listy == None :
        raise IndexError
    for i in listy.array:
        if count == index:
            listy.array[index] = value
            return listy.array
        count +=1

# list index - > list
# removes an element at the specified index
def remove(listy, index, count=0):
    if listy == None:
        raise IndexError

