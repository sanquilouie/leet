def insertionsort(arr):
    i = 1
    end = arr[0]
    while i < len(arr):
        if arr[i] < end:
            x = arr.pop(i)
            for j in range(0, i):
                if x < arr[j]:
                    arr.insert(j, x)
                    break
        end = arr[i]
        i += 1
    return arr


print(insertionsort([6,5,3,1,8,7,2,4]))



