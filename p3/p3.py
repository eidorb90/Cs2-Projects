def majority_element(numbers):
    num_dict = {}
    n = len(numbers)

    for num in numbers:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1

    if num_dict[num] > n/2:
        return num


if __name__ == "__main__":
    numbers = [3, 7, 3]
    print(majority_element(numbers))
