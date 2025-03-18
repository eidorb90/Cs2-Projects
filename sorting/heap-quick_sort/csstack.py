# csstack.py
# Marcus Gubanyi
# 2025.02.19
# Defines a simple stack class built with an array.
# The purpose of this class is to work with a simple
# stack that only pushes and pops and has an underlying
# representation of a fixed-length array.
#
# Usage:
# from csstack import Stack
# s = Stack(max_size = 50)
# s.push( ___ )
# ___ = s.pop()

from csarray import Array

class Stack():
    """Stack object built with an array.

    Supports pushing and popping elements. Errors if max is exceeded.
    """

    def __init__(self, data = None, max_size = 100):
        
        self._data = Array(size = max_size)
        self._top = -1
        self._max_size = max_size

        if data is not None:
            for item in data:
                self.push(item)

    def is_empty(self):
        return self._top == -1

    def is_full(self):
        return self._top == self._max_size

    def push(self, item):
        if self.is_full():
            raise IndexError("Stack Overflow Error!")
        else:
            self._top += 1
            self._data[self._top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow Error!")
        else:
            popped = self._data[self._top]
            self._top -= 1
            return popped

# Example application of Stack class
def valid_brackets(string):
    stack = Stack()
    for c in string:
        if c in "([{":
            stack.push(c)
        elif stack.is_empty():
            return False
        else:
            bracket = stack.pop()
            if not (bracket == '(' and c == ')' or
                    bracket == '[' and c == ']' or
                    bracket == '{' and c == '}'):
                return False

    return stack.is_empty()
        
if __name__ == "__main__":
    test_strings = ["()", "[[[]]]{}", "([(){}])[]", "(]", "[[[]]", "(([[])])"]
    for s in test_strings:
        print(f"{s} valid? {valid_brackets(s)}")
