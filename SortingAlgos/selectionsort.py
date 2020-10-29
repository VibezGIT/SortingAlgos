# selection sort algorithm
# time complexity O(n^2)
# space complexity O(1)

def selectionsort(list, comp):
    for x in range(len(list)):
        curr = x

        for y in range(x, len(list)):
            if (comp(list[curr], list[y]) > 0):
                curr = y
        
        swap = list[x]
        list[x] = list[curr]
        list[curr] = swap

    return list