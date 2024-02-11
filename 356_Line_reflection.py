class Solution:
    def isReflected(self, points: list[list[int]]) -> bool:
        left_point = min(points, key=lambda x: x[0])
        right_point = max(points, key=lambda x: x[0])
        doubled_mid = left_point[0] + right_point[0]

        points_dict = {}
        for x, y in points:
            if (x, y) in points_dict:
                points_dict[(x, y)] += 1
            else:
                points_dict[(x, y)] = 1

        for point in points:
            reflected = (doubled_mid - point[0], point[1])
            if reflected in points_dict:
                points_dict[reflected] -= 1
                if points_dict[reflected] < 0:
                    return False
            else:
                return False
        return True


s = Solution()
print(s.isReflected([[1, 1], [-1, 1], [-1, 1]]))
