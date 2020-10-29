# bogosort algorithm
# O(n!) time complexity or something
# O(1) space complexity

from numpy import random

def bogosort(list, comp):
    sorted = False
    while (not sorted and (len(list) > 0)):
        random.shuffle(list)
        sorted = True

        for x in range(len(list) - 1):
            if (comp(list[x], list[x + 1]) > 0):
                sorted = False
                break
    
    return list
            
        
