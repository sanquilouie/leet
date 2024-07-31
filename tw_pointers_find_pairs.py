def find_pairs_with_sum(arr, target):
    left = 0
    right = len(arr) - 1
    pairs = []

    while left < right:
        current_sum = arr[left] + arr[right] # current_sum = 1 + 7
        if current_sum == target: # if 8 == 8
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target: # 7 < 8
            left += 1 # 9 < 8
        else:
            right -= 1 # 7 < 8

    return pairs

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7]
target = 8
print(find_pairs_with_sum(arr, target))  # Output: [(1, 7), (2, 6), (3, 5)]
