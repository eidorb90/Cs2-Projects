# p2.py
# Brodie Rogers
# 2025.01.22
# Checks to see if there are duplicate numbers(numbers) 
# within a given range from said number (k) 
# also makes sure the dict used to store seen numbers
# doesnt take too much memory by removing the oldest entry.

# Useage
#       numbers = [3, 7, 0, 3]
#       k = 3
#       output = has_nearby_duplicate(numbers, k)

def has_nearby_duplicate(numbers, k):
    """
    Determines if the array contains nearby duplicate elements such that 
    numbers[i] == numbers[j] and 0 < j - i <= k.

    Args:
        numbers (list): List of integers.
        k (int): Maximum distance threshold for duplicate indices.

    Returns:
        bool: True if nearby duplicates exist, False otherwise.
    """
    last_seen = {}
    for i, num in enumerate(numbers):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        
        last_seen[num] = i
        # ensure that the dictionary isn't getting too large
        if len(last_seen) > k:
            oldest_key = min(last_seen, key=last_seen.get)
            del last_seen[oldest_key]

    return False


if __name__ == "__main__":
    numbers = [3, 7, 0, 3]
    k = 2   
    print(has_nearby_duplicate(numbers, k))
