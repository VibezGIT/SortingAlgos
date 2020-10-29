# a few test arrays for sorting algorithms

input1 = [1, 10, 8, 3, 6, 2, 4, 9, 5, 7]
expected1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
msg1 = "General test case failed"
input2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
expected2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
msg2 = "Reverse order case failed"
input3 = []
expected3 = []
msg3 = "Empty input case failed"
input4 = [5, 5, 5, 4, 4, 4, 3, 3, 3, 1, 1, 1, 2, 2, 2]
expected4 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
msg4 = "Duplicates case failed"
input5 = ["a", "b", "c", "d", "e", "f", "g"]
expected5 = ["a", "b", "c", "d", "e", "f", "g"]
msg5 = "String elements case failed"
input6 = ["g", "f", "e", "d", "c", "b", "a"]
expected6 = ["a", "b", "c", "d", "e", "f", "g"]
msg6 = "String unsorted case failed"

def intcomp(int1, int2):
    return 1 if (int1 > int2) else (-1 if (int1 < int2) else 0)

def stringcomp(str1, str2):
    return 1 if (str1 > str2) else (-1 if (str1 < str2) else 0)