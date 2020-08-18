arr = [4, 9, 7, 1, 2, 6]

# O(n)
def find_num(arr, target_num):
    for x in arr:
        if x == target_num:
            return x
    return -1

find_num(arr, 1)

arr = [1, 2, 3, 4, 5, 6, 97]
