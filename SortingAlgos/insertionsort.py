# insertion sort algorithm
# O(n^2) time complexity
# O(1) space complexity

def insertionsort(list, comp):
    for x in range(len(list)):
        for y in range(x, 0, -1):
            curr = list[y]
            adj = list[y-1]

            if (comp(curr, adj) < 1):
                list[y-1] = curr
                list[y] = adj
            else:
                break

    return list
            