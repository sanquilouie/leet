arr = [4, 5, 1, 9, 2, 3, 6, 8]


def mergesort(arr):
    if len(arr) == 1:
        return arr
    length = len(arr)
    mid = length // 2
    left = arr[:mid]
    right = arr[mid:]
    print('Left {}'.format(left))
    print('Right {}'.format(right))

    return merge(mergesort(left), mergesort(right))


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    # print(left, right)
    print(result + left[left_index:] + right[right_index:])
    return result + left[left_index:] + right[right_index:]


x = mergesort(arr)
