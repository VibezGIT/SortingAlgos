# bubble sort algorithm
# O(n^2) time complexity
# O(1) space complexity

def bubblesort(list, comp):
    for x in range(len(list) - 1):
        for y in range(len(list) - (x + 1)):
            curr = list[y]
            adj = list[y + 1]
            if (comp(curr, adj) > 0):
                list[y + 1] = curr
                list[y] = adj

    return list
