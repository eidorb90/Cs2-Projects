"""
insert_sort.py
Brodie Rogers <brodie.rogers@students.cune.edu
1/27/25

My on implementation of the insert sort methond on arrays
Along with a testing function to test the speeds of this algorithm
"""

from csarray import Array
import random
import time
import csv
import math


class SortingArray(Array):
    """
    SortingArray object with fixed size and sorting behaviors.
    """

    def insertion_sort(self):
        """
        Sorting array object with fixed sizes and sorting behavior.
        """
        for i in range(1, len(self._data)):
            # Insert arr[i] into sorted portion of arr[0:i]
            temp = self._data[i]
            j = i - 1
            # Loop through the already sorted arr along with the 1 added index
            while j >= 0 and self._data[j] > temp:
                # Preform the swap and decrease j
                self._data[j + 1] = self._data[j]
                j -= 1
            # Insert the number we are sorting into the correct index
            self._data[j + 1] = temp

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
    def gen_insertion_sort_test_data():
        """
        Test the insert sort function, printing results for arrays of increaing sizes.
        Creates arrays of different sizes and permutation of data.
        """

        sizes = [10, 100, 1000, 10000, 20000]
        time_data = []
        # Random Arrays
        epochs = 100
        for i in range(epochs):
            print(f"Starting epoch{i}")
            time_data = []
            for s in sizes:
                # Create Random Arrays
                arr = SortingArray(size=s, default=0)
                for i in range(s):
                    arr[i] = random.randint(0, 100)

                # Time the Algorithm
                start = time.time()
                arr.insertion_sort()
                end = time.time()

                time_data.append(round(end - start, 4))
            SortingArray.save_data("r", time_data)

            # Already Sorted Arrays
            time_data = []
            for s in sizes:
                # Create Ascending Order Arrays
                arr = SortingArray(size=s, default=0)
                for i in range(1, s):
                    arr[i] = i

                # Time the Algorithm
                start = time.time()
                arr.insertion_sort()
                end = time.time()

                time_data.append(round(end - start, 4))
            SortingArray.save_data("a", time_data)

            # Decreasing Order Arrays
            time_data = []
            for s in sizes:
                # Create Descending Order Arrays
                arr = SortingArray(size=s, default=0)
                temp = s
                for i in range(s):
                    arr[i] = temp
                    temp -= 1

                # Time the Algorithm
                start = time.time()
                arr.insertion_sort()
                end = time.time()

                time_data.append(round(end - start, 4))
            SortingArray.save_data("d", time_data)
        print("Finished testing and saving.")


if __name__ == "__main__":
    SortingArray.gen_insertion_sort_test_data()
