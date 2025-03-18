def path_sum(tree: list, target: int, i=0, current_sum=0):
    # make sure that we dont get an out of bounds error
    if i >= len(tree):
        return False

    # update the sum
    current_sum += tree[i]

    # Check if we're at a leaf node (no children) and sum matches the target
    left = 2 * i + 1
    right = 2 * i + 2

    if current_sum == target and left >= len(tree) and right >= len(tree):
        return True

    # Recursively check left and right children
    right_result = path_sum(tree, target, right, current_sum)
    if right_result:
        return True

    left_result = path_sum(tree, target, left, current_sum)
    if left_result:
        return True

    # If neither path works, return False
    return False


if __name__ == "__main__":
    tree1 = [3, 8, 7]
    target1 = 10

    tree2 = [5, 4, 7, 1, 2, 8, 6]
    target2 = 9

    tree3 = [5, 4, 7, 1, 2, 8, 6, 0, 4, 7, 3, 9, 5, 7, 8]
    target3 = 14

    outcome = path_sum(tree1, target1)
    print(outcome)

    outcome = path_sum(tree2, target2)
    print(outcome)

    outcome = path_sum(tree3, target3)
    print(outcome)
