def BubbleSort(value):
    counter = 0
    while counter < len(value)-1:
        for i in range(len(value)-1):
            if value[i] > value[i+1]:
                value[i], value[i+1] = value[i+1], value[i]
        counter += 1
    return value


print(BubbleSort([3, 4, 6, 1, 2, 8, 7]))