# quicksort algorithm
# O(n^2) time complexity
# O(n) space complexity

def quicksort(list, comp):
    if (len(list) > 1):
        left = []
        right = []
        pivot = list[0]

        for x in range(1, len(list)):
            if (comp(list[x], pivot) > 0):
                right.append(list[x])
            else:
                left.append(list[x])
        
        sortedL = quicksort(left, comp)
        sortedR = quicksort(right, comp)

        return sortedL + [pivot] + sortedR

    else:
        return list 