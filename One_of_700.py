def find_one_of_700(arr: list[int]) -> int:
    """Given array of 700 integers in ascending order in the segment [0, 700]
    All the elements are unique
    With less or equal 10 look-ups find the missing number"""
    left, right = 0, 699
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == mid + 1:
            right = mid
        else:
            left = mid + 1
    return left if arr[-1] == 700 else left + 1


# testing
variants = [i for i in range(701)]
test_pool = []
for variant in variants:
    a = [i for i in range(variant)] + [i for i in range(variant + 1, 701)]
    test_pool.append(a)

for cur in range(701):
    print(cur, find_one_of_700(test_pool[cur]))

