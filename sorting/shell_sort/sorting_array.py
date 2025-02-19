"""
insert_sort.py
Brodie Rogers <brodie.rogers@students.cune.edu
1/27/25


"""

from csarray import Array
import random
import time
from tqdm import tqdm
import csv


class SortingArray(Array):
    """SortingArray object with fixed size and sorting behaviors."""

    def shell_sort(self):
        """Sort elements by sorting different shells 'smaller arrays' of a large array."""
        # store the arr in a more normal var
        arr = self._data

        # Get the initial Gap size for the array
        gap = self.calc_init_gap(arr)

        while gap > 0:
            for i in range(gap, len(arr)):
                temp = arr[i]
                j = i - gap

                while j >= 0 and arr[j] > temp:
                    arr[j + gap] = arr[j]
                    j = j - gap

                arr[j + gap] = temp

            # reduce the gap
            gap = (gap - 1) // 3

    def calc_init_gap(self, arr):
        """
        Calculates the inital gap that should be used. We get this number from the Knuth Sequence.

        if k = # of iterations
        then (3^k - 1) / 2
        = sequence output

        In the Knuth sequence we start at 1 and with each iteration we multiply by 3 then add 1.
        The First few iterations are as follows

        [1, 4, 13, 40, 121]

        """
        len_arr = len(arr)
        start = 1

        # Loop and find the output that is higher than the len
        while start < len_arr:
            start *= 3
            start += 1
        # Go back one iteration so we are smaller than the len of the arr
        start = (start - 1) // 3

        # return approiate gap size
        return start

    @staticmethod
    def save_data(t, data):
        """
        Used to save the different data into a csv to create charts of the times
        """
        # Set the file based on the input 't'
        if t == "r":
            file_name = "random.csv"
        elif t == "a":
            file_name = "asceding.csv"
        elif t == "d":
            file_name = "descending.csv"
        else:
            print("please give 'r', 'a', or 'd' for the t value")

        # Save the Data
        try:
            with open(file_name, "a") as file:
                writer = csv.writer(file)
                writer.writerow(data)
            file.close()
        except Exception as e:
            print(f"Could save data. {e}")

    @staticmethod
    def test_shell_sort():
        """Test Shell sort function, printing results for arrays of increasing size."""

        sizes = [10, 100, 1000, 10000, 20000, 100000]
        time_data = []
        epochs = 100

        for i in tqdm(range(epochs), desc="Processing"):
            time_data = []
            for s in sizes:
                # Create Random Arrays
                arr = SortingArray(size=s, default=0)
                for i in range(s):
                    arr[i] = random.randint(0, 100)

                # Time the Algorithm
                start = time.time()
                arr.shell_sort()
                end = time.time()

                time_data.append(round(end - start, 4))
            SortingArray.save_data("r", time_data)

            time_data = []
            for s in sizes:
                # Create Ascending Arrays
                arr = SortingArray(size=s, default=0)
                for i in range(1, s):
                    arr[i] = i

                # Time the Algorithm
                start = time.time()
                arr.shell_sort()
                end = time.time()
                time_data.append(round(end - start, 4))
            SortingArray.save_data("a", time_data)

            time_data = []
            for s in sizes:
                # Create Descending Arrays
                arr = SortingArray(size=s, default=0)
                temp = s
                for i in range(s):
                    arr[i] = temp
                    temp -= 1

                # Time the Algorithm
                start = time.time()
                arr.shell_sort()
                end = time.time()
                time_data.append(round(end - start, 4))
            SortingArray.save_data("d", time_data)


if __name__ == "__main__":
    SortingArray.test_shell_sort()
