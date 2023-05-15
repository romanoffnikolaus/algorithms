def BinarySearch(list_, value):
    first = 0
    last = len(list_)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if list_[mid] == value:
            index = mid
        else:
            if value<list_[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

print(BinarySearch([10,20,30,40,50], 20))