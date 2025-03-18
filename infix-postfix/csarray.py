# csarray.py
# Marcus Gubanyi
# 2025.01.14
# Defines a simple array class with only basic behaviors.
# The purpose of this class is to work with a simple
# sequential, indexed data structure without the additional
# behaviors of a python list.
#
# Usage:
# from array import Array
# a = Array(data = [2,3,4])

class Array():
    """Array object with a fixed size.

    Supports setting and getting values with 0-based indices.
    """
    def __init__(self, data = None, size = 0, default = 0):
        """Initialize an Array object.
        Usage:
        arr1 = Array([2,3,4])
        arr2 = Array(size = 3, default = 4)
              -> array contains [4,4,4]
        """
        
        self._data = data if data is not None else []
        while len(self._data) < size:
            self._data.append(default)

    def __setitem__(self, index, new_value):
        """Set element with subscript index to new_value.
        Usage: arr[2] = 3.14
        """
        self._data[index] = new_value

    def __getitem__(self, index):
        """Return the element at subscript index."""
        return self._data[index]

    def __str__(self):
        return str(self._data)

    def __len__(self):
        """Return the size of the array.
        Usage: len(arr)
        """
        return len(self._data)

    def __iter__(self):
        """Iterator for the array object. Used for in operator in if and for."""
        return iter(self._data)
            

# Example Usage
if __name__ == "__main__":

    # Calls __init__
    arr = Array([5,4,3])

    # Calls __str__
    print(arr)
    
    # Calls __getitem__ and __setitem__
    temp = arr[0]
    arr[0] = arr[-1]
    arr[-1] = temp

    # Calls __iter__
    for element in arr:
        print(element)
    
        
