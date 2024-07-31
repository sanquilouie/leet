def merge_sorted_arr(a, b):
    x = a + b
    x.sort()
    return x


a = [1, 2, 3, 4]
b = [3, 7, 9, 12]
qw = merge_sorted_arr(a, b)
print(qw)
