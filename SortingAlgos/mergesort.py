# mergesort algorithm
# O(nlogn) time complexity
# O(n) space complexity

def mergesort(list, comp):
    return partition(list, 0, len(list) - 1, comp)

def partition(list, start, end, comp):
    if (start < end):
        mid = start + (end - start)//2
        left = partition(list, start, mid, comp)
        right = partition(list, mid + 1, end, comp)
        return merge(left, right, comp)
    if (start < len(list)):
        return [list[start]]
    else:
        return []

def merge(left, right, comp):
    sorted = []
    idxL = 0
    idxR = 0
    while (idxL < len(left) and idxR < len(right)):
        if (comp(left[idxL], right[idxR]) > 0):
            sorted.append(right[idxR])
            idxR += 1
        else:
            sorted.append(left[idxL])
            idxL += 1
    
    while (idxL < len(left)):
        sorted.append(left[idxL])
        idxL += 1
    while (idxR < len(right)):
        sorted.append(right[idxR])
        idxR += 1

    return sorted


