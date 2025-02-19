"""
insert_sort.py
Brodie Rogers <brodie.rogers@students.cune.edu
1/27/25

This module implements shell sort algorithm using a custom Array class.
The implementation includes functionality to test and benchmark the algorithm
with different input sizes and data arrangements.
"""

from csarray import Array
import random
import time
from tqdm import tqdm
import csv


class SortingArray(Array):
    """
    SortingArray object with fixed size and sorting behaviors.

    This class extends the Array class to add sorting capabilities,
    specifically implementing the Shell Sort algorithm. It includes
    methods for sorting, gap calculation, and performance testing.
    """

    def shell_sort(self):
        """
        Sort elements using the Shell Sort algorithm.

        Shell Sort works by comparing elements separated by a gap.
        The gap starts large and progressively reduces until it reaches 1,
        effectively becoming an insertion sort. This implementation uses
        Knuth's sequence for gap calculation.

        Time Complexity:
            - Best Case: O(n log n)
            - Average Case: O(n^1.5)
            - Worst Case: O(n^2)

        Space Complexity: O(1) as it sorts in-place
        """
        arr = self._data

        gap = self.calc_init_gap(arr)

        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i - gap

                while j >= 0 and arr[j] > temp:
                    arr[j + gap] = arr[j]
                    j = j - gap

                arr[j + gap] = temp

            gap = (gap - 1) // 3

    def calc_init_gap(self, arr):
        """
        Calculate the initial gap size using Knuth's sequence.

        The sequence follows the formula: (3^k - 1) / 2
        where k is the number of iterations. The sequence generates
        gap sizes: 1, 4, 13, 40, 121, ...

        Args:
            arr: The array for which to calculate the initial gap

        Returns:
            int: The largest gap size less than the array length
        """
        len_arr = len(arr)
        start = 1

        while start < len_arr:
            start *= 3
            start += 1
        start = (start - 1) // 3

        return start

    @staticmethod
    def save_data(t, data):
        """
        Save sorting performance data to CSV files.

        Args:
            t (str): Type of data being saved:
                     'r' for random array data
                     'a' for ascending array data
                     'd' for descending array data
            data (list): List of timing measurements to save

        Raises:
            Exception: If file operations fail
        """
        if t == "r":
            file_name = "random.csv"
        elif t == "a":
            file_name = "asceding.csv"
        elif t == "d":
            file_name = "descending.csv"
        else:
            print("please give 'r', 'a', or 'd' for the t value")

        try:
            with open(file_name, "a") as file:
                writer = csv.writer(file)
                writer.writerow(data)
            file.close()
        except Exception as e:
            print(f"Could save data. {e}")

    @staticmethod
    def test_shell_sort():
        """
        Benchmark the Shell Sort implementation with various input sizes.

        Tests the algorithm with three different array arrangements:
            1. Random order arrays
            2. Ascending order arrays
            3. Descending order arrays

        For each arrangement, tests array sizes:
            [10, 100, 1000, 10000, 20000, 100000]

        Performs 100 epochs of testing and saves timing data to CSV files.
        Each timing measurement is rounded to 4 decimal places.
        """
        sizes = [10, 100, 1000, 10000, 20000, 100000]
        time_data = []
        epochs = 100

        for i in tqdm(range(epochs), desc="Processing"):
            time_data = []
            for s in sizes:
                arr = SortingArray(size=s, default=0)
                for i in range(s):
                    arr[i] = random.randint(0, 100)

                start = time.time()
                arr.shell_sort()
                end = time.time()

                time_data.append(round(end - start, 4))
            SortingArray.save_data("r", time_data)

            time_data = []
            for s in sizes:
                arr = SortingArray(size=s, default=0)
                for i in range(1, s):
                    arr[i] = i

                start = time.time()
                arr.shell_sort()
                end = time.time()
                time_data.append(round(end - start, 4))
            SortingArray.save_data("a", time_data)

            time_data = []
            for s in sizes:
                arr = SortingArray(size=s, default=0)
                temp = s
                for i in range(s):
                    arr[i] = temp
                    temp -= 1

                start = time.time()
                arr.shell_sort()
                end = time.time()
                time_data.append(round(end - start, 4))
            SortingArray.save_data("d", time_data)


if __name__ == "__main__":
    SortingArray.test_shell_sort()
