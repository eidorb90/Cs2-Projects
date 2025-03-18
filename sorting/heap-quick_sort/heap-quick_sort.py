from csarray import Array
from csstack import Stack
import random
import time
from tqdm import tqdm
import csv
import sys 

sys.setrecursionlimit(10**6)


class SortingArray(Array):
    def heap_sort(self):
        arr = self._data
        n = len(arr)
        for i in range(n - 1, -1, -1):
            self.heapify(arr, i, n)

        # assume arr is max heap after heapifying it
        j = n - 1
        while j > 0:
            temp = arr[0]
            arr[0] = arr[j]
            arr[j] = temp
            self.heapify(arr, 0, j)
            j -= 1

    def heapify(self, arr, i, j):
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            if right < j and arr[right] > arr[left] and arr[right] > arr[i]:
                arr[i], arr[right] = arr[right], arr[i]
                i = right
            elif left < j and arr[left] > arr[i]:
                arr[i], arr[left] = arr[left], arr[i]
                i = left
            else:
                break

    def recur_quick_sort(self, arr, low, high):
        if low >= high:
            return 
        else:
            mid = self.partition(arr, low, high)
            self.recur_quick_sort(arr, low, mid-1)
            self.recur_quick_sort(arr, mid+1, high)

    def itter_quick_sort(self, arr):
        stack = Stack()
        stack.push((0, len(arr) - 1))

        while not stack.is_empty():
            low, high = stack.pop()
            pivot = self.partition(arr, low, high)

            if low < pivot - 1:
                stack.push((low, pivot - 1))
            if pivot + 1 < high:
                stack.push((pivot + 1, high))

    def itter_insert_quick_sort(self, arr):
        stack = Stack()
        stack.push((0, len(arr) - 1))

        while not stack.is_empty():
            low, high = stack.pop()
            # Use insertion sort for small partitions
            if high - low < 1000:  # Much smaller threshold value
                # Apply insertion sort only to this partition
                self.insertion_sort_partition(arr, low, high)
                continue

            pivot = self.partition(arr, low, high)

            if low < pivot - 1:
                stack.push((low, pivot - 1))
            if pivot + 1 < high:
                stack.push((pivot + 1, high))

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        while i <= j:
            if arr[j] > pivot:
                j -= 1
            elif arr[i] <= pivot:
                i += 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
                i += 1

        arr[low], arr[j] = arr[j], arr[low]

        return j

    def insertion_sort_partition(self, arr, low, high):
        """
        Sorting a specific partition of the array using insertion sort.
        """
        for i in range(low + 1, high + 1):
            # Insert arr[i] into sorted portion
            temp = arr[i]
            j = i - 1
            # Loop through the already sorted part of this partition
            while j >= low and arr[j] > temp:
                # Perform the swap and decrease j
                arr[j + 1] = arr[j]
                j -= 1
            # Insert the number we are sorting into the correct index
            arr[j + 1] = temp

    @staticmethod
    def save_data(t, data, prefix):
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
            file_name = f"{prefix}-random.csv"
        elif t == "a":
            file_name = f"{prefix}-asceding.csv"
        elif t == "d":
            file_name = f"{prefix}-descending.csv"
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
    def test_heap_sort():
        """
        Benchmark the Heap Sort implementation with various input sizes.

        Tests the algorithm with three different array arrangements:
            1. Random order arrays
            2. Ascending order arrays
            3. Descending order arrays

        For each arrangement, tests array sizes:
            [10, 100, 1000, 10000, 20000, 100000, 1000000]

        Performs 100 epochs of testing and saves timing data to CSV files.
        Each timing measurement is rounded to 4 decimal places.
        """
        sizes = [10, 100, 1000, 10000, 20000, 100000, 1000000]
        time_data = []
        epochs = 100

        for i in tqdm(range(epochs), desc="Processing"):
            time_data = []
            for s in sizes:
                arr = SortingArray(size=s, default=0)
                for i in range(s):
                    arr[i] = random.randint(0, 100)

                start = time.time()
                arr.heap_sort()
                end = time.time()

                time_data.append(round(end - start, 4))
            SortingArray.save_data("r", time_data, "heap")

            time_data = []
            for s in sizes:
                arr = SortingArray(size=s, default=0)
                for i in range(1, s):
                    arr[i] = i

                start = time.time()
                arr.heap_sort()
                end = time.time()
                time_data.append(round(end - start, 4))
            SortingArray.save_data("a", time_data, "heap")

            time_data = []
            for s in sizes:
                arr = SortingArray(size=s, default=0)
                temp = s
                for i in range(s):
                    arr[i] = temp
                    temp -= 1

                start = time.time()
                arr.heap_sort()
                end = time.time()
                time_data.append(round(end - start, 4))
            SortingArray.save_data("d", time_data, "heap")

    @staticmethod
    def test_itter_quick_sort():
        """
        Benchmark the Itterative Quick Sort implementation with various input sizes.

        Tests the algorithm with three different array arrangements:
            1. Random order arrays
            2. Ascending order arrays
            3. Descending order arrays

        For each arrangement, tests array sizes:
            [10, 100, 1000, 10000, 20000, 100000, 1000000]

        Performs 100 epochs of testing and saves timing data to CSV files.
        Each timing measurement is rounded to 4 decimal places.
        """
        sizes = [10, 100, 1000, 10000, 20000, 100000, 1000000]
        time_data = []
        epochs = 10

        for i in tqdm(range(epochs), desc="Processing"):
            time_data = []
            for s in sizes:
                arr = SortingArray(size=s, default=0)
                for i in range(s):
                    arr[i] = random.randint(0, 100)

                start = time.time()
                arr.itter_quick_sort(arr._data)  # , 0, len(arr) - 1
                end = time.time()

                time_data.append(round(end - start, 4))
            SortingArray.save_data("r", time_data, "itter-quick")

            time_data = []
            for s in sizes:
                arr = SortingArray(size=s, default=0)
                for i in range(1, s):
                    arr[i] = i

                start = time.time()
                arr.itter_quick_sort(arr._data)  # , 0, len(arr) - 1
                end = time.time()
                time_data.append(round(end - start, 4))
            SortingArray.save_data("a", time_data, "itter-quick")

            time_data = []
            for s in sizes:
                arr = SortingArray(size=s, default=0)
                temp = s
                for i in range(s):
                    arr[i] = temp
                    temp -= 1

                start = time.time()
                arr.itter_quick_sort(arr._data)  # , 0, len(arr) - 1
                end = time.time()
                time_data.append(round(end - start, 4))
            SortingArray.save_data("d", time_data, "itter-quick")

    @staticmethod
    def test_itter_insert_quick_sort():
        """
        Benchmark the Itterative Insert Quick Sort implementation with various input sizes.

        Tests the algorithm with three different array arrangements:
            1. Random order arrays
            2. Ascending order arrays
            3. Descending order arrays

        For each arrangement, tests array sizes:
            [10, 100, 1000, 10000, 20000, 100000, 1000000]

        Performs 100 epochs of testing and saves timing data to CSV files.
        Each timing measurement is rounded to 4 decimal places.
        """
        sizes = [10, 100, 1000, 10000, 20000, 100000, 1000000]
        time_data = []
        epochs = 10

        for i in tqdm(range(epochs), desc="Processing"):
            time_data = []
            for s in sizes:
                arr = SortingArray(size=s, default=0)
                for i in range(s):
                    arr[i] = random.randint(0, 100)

                start = time.time()
                arr.itter_insert_quick_sort(arr._data)  # , 0, len(arr) - 1
                end = time.time()

                time_data.append(round(end - start, 4))
            SortingArray.save_data("r", time_data, "itter-insert-quick")

            time_data = []
            for s in sizes:
                arr = SortingArray(size=s, default=0)
                for i in range(1, s):
                    arr[i] = i

                start = time.time()
                arr.itter_insert_quick_sort(arr._data)  # , 0, len(arr) - 1
                end = time.time()

                time_data.append(round(end - start, 4))
            SortingArray.save_data("a", time_data, "itter-insert-quick")

            time_data = []
            for s in sizes:
                arr = SortingArray(size=s, default=0)
                temp = s
                for i in range(s):
                    arr[i] = temp
                    temp -= 1

                start = time.time()
                arr.itter_insert_quick_sort(arr._data)  # , 0, len(arr) - 1
                end = time.time()

                time_data.append(round(end - start, 4))
            SortingArray.save_data("d", time_data, "itter-insert-quick")

    @staticmethod
    def test_recur_quick_sort():
        """
        Benchmark the Recursive Qucick Sort implementation with various input sizes.

        Tests the algorithm with three different array arrangements:
            1. Random order arrays
            2. Ascending order arrays
            3. Descending order arrays

        For each arrangement, tests array sizes:
            [10, 100, 1000, 10000, 20000, 100000, 1000000]

        Performs 10 epochs of testing and saves timing data to CSV files.
        Each timing measurement is rounded to 4 decimal places.
        """
        sizes = [10, 100, 1000, 10000, 20000, 100000, 1000000]
        time_data = []
        epochs = 10

        for i in tqdm(range(epochs), desc="Processing"):
            time_data = []
            for s in sizes:
                arr = SortingArray(size=s, default=0)
                for i in range(s):
                    arr[i] = random.randint(0, 100)

                start = time.time()
                arr.recur_quick_sort(arr._data, 0, len(arr) - 1)  # , 0, len(arr) - 1
                end = time.time()

                print(f"Random {s} sorted in {end - start}")

                time_data.append(round(end - start, 4))
            SortingArray.save_data("r", time_data, "recur-quick")

            time_data = []
            for s in sizes:
                arr = SortingArray(size=s, default=0)
                for i in range(1, s):
                    arr[i] = i

                start = time.time()
                arr.recur_quick_sort(arr._data, 0, len(arr) - 1)  # , 0, len(arr) - 1
                end = time.time()
                print(f"Ascending {s} sorted in {end - start}")


                time_data.append(round(end - start, 4))
            SortingArray.save_data("a", time_data, "recur-quick")

            time_data = []
            for s in sizes:
                arr = SortingArray(size=s, default=0)
                temp = s
                for i in range(s):
                    arr[i] = temp
                    temp -= 1

                start = time.time()
                arr.recur_quick_sort(arr._data, 0, len(arr) - 1)  
                end = time.time()
                print(f"Descending {s} sorted in {end - start}")


                time_data.append(round(end - start, 4))
            SortingArray.save_data("d", time_data, "recur-quick")

if __name__ == "__main__":
    SortingArray.test_recur_quick_sort()
