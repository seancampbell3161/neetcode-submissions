from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    index = -1
    for i, n in enumerate(nums):
        if n == 7:
            return i
    return index


def get_dist_between_sevens(nums: List[int]) -> int:
    found = False
    distance = 0
    for i, n in enumerate(nums):
        if found == False:
            if n == 7:
                found = True
        else:
            if n == 7:
                distance += 1
                return distance
            else:
                distance += 1


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
