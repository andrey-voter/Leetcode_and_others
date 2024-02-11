from itertools import groupby


class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        ans = seats.index(1)
        ans = max(ans, seats[::-1].index(1))
        for seat, group in groupby(seats):
            if seat == 0:
                ans = max(ans, (len(list(group)) + 1) // 2)
        return ans


class Solution2:
    def maxDistToClosest(self, seats: list[int]) -> int:
        if len(seats) == 2:
            return 1

        before_len = seats.index(1)
        after_len = seats[::-1].index(1)
        inner_len = 0
        cur_len = 0
        for el in seats[before_len: len(seats) - after_len]:
            if el == 0:
                cur_len += 1
            else:
                inner_len = max(inner_len, cur_len)
                cur_len = 0
        inner_len = max(inner_len, cur_len)
        if inner_len % 2:
            to_compare = (inner_len - 1) // 2 + 1
        else:
            to_compare = inner_len // 2
        return max(before_len, after_len, to_compare)
