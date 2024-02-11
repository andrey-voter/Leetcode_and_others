class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])

        i = 0
        ans = []
        while i < len(intervals):
            start_i, end_i = intervals[i]
            j = i + 1
            while j < len(intervals):
                start_j, end_j = intervals[j]
                if start_j > end_i:
                    i = j
                    break
                if end_j <= end_i:
                    j += 1
                    continue
                end_i = end_j
                j += 1
            ans.append([start_i, end_i])
            i = j
        return ans
