# sorting_array_template.py
# Marcus Gubanyi
# 2025.01.014
# Defines an SortingArray class that sorts itself, extending
# the Array class.

# array.py must be in the same directory as this program
from csarray import Array
import random
import time

class SortingArray(Array):
    """SortingArray object with fixed size and sorting behaviors."""

    def is_in_order(self):
        """Determine if array is in order."""
        
        i = 0
        while i + 1 < len(self):
            if self[i] <= self[i+1]:
                i += 1
            else:
                return False
            
        return True

    def shuffle_sort(self):
        """Sort elements by shuffling them until they are in order."""
        
        while not self.is_in_order():
            random.shuffle(self._data)

    @staticmethod
    def test_shuffle_sort():
        """Test shuffle sort function, printing results for arrays of increasing size."""

        for s in range(2, 11):
            print("Testing Shuffle Sort on Random Array of Length", s)
            
            arr = SortingArray(size = s, default = 0)
            for i in range(s):
                arr[i] = random.randint(0, 100)

            start = time.time()
            arr.shuffle_sort()
            end = time.time()

            print(f"   Sorted {arr} in {end-start:.4f} seconds.\n")

    def insertion_sort(self):
        """Sorting array object with fixed sizes and sorting behavior"""
        for i in range(1, len(self._data)):
            temp = self._data[i]
            j = i - 1
            while j >= 0 and self._data[j] > temp:
                self._data[j+1] = self._data[j]
                j -= 1
            self._data[j+i] = temp

    @staticmethod
    def test_insertion_sort():
        """Test the insert sort function, printing results for arrays of increaing sizes"""

        for s in range(2, 11):
            print("Testing Insert Sort on Random Array of Length", s)

            arr = SortingArray(size=s, default=0)
            for i in range(s):
                arr[i] = random.randint(0,100)

            start = time.time()
            arr.insert_sort()
            end = time.time()

            print(f"    Sorted {arr} in {end-start:.4f} seconds.\n")


if __name__ == "__main__":
    SortingArray.test_shuffle_sort()
