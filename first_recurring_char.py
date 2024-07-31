def func(mylist):
    for i in range(0, len(mylist)):
        for j in range(i + 1, len(mylist)):
            if mylist[i] == mylist[j]:
                return mylist[i]
    return 0


def hashtable(mylist):
    mydict = {}
    for i in range(0, len(mylist)): # 0, 7
        if mylist[i] in mydict:
            return mylist[i]
        else:
            mydict[mylist[i]] = i
    return 0


mylist = [2, 3, 3, 2, 6, 5, 2]
x = func(mylist)
print(x)