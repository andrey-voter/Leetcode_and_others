def rle_dot_product(v1: list[str], v2: list[str]) -> int:
    """
    given two vectors in rle format, return dot product
    example:
    v1 = ['1-3', '3', '5-2'] // [1, 1, 1, 3, 5, 5]
    v2 = ['1', '2', '3', '4-3'] // [1, 2, 3, 4, 4, 4]
    rle_dot_product(v1, v2) = 58
    """
    def process_frame(frame: str) -> (int, int):
        if '-' not in frame:
            return int(frame), 1
        return int(frame.split('-')[0]), int(frame.split('-')[1])

    res = 0
    p1 = p2 = 0
    cnt1 = cnt2 = num1 = num2 = 0
    while p1 < len(v1) and p2 < len(v2):
        if not cnt1:
            num1, cnt1 = process_frame(v1[p1])
        if not cnt2:
            num2, cnt2 = process_frame(v2[p2])

        if cnt1 > cnt2:
            while cnt2:
                res += num1 * num2
                cnt1 -= 1
                cnt2 -= 1
            p2 += 1
        elif cnt1 < cnt2:
            while cnt1:
                res += num1 * num2
                cnt1 -= 1
                cnt2 -= 1
            p1 += 1
        else:
            # cnt1 == cnt2
            pass
    # now we need to check if which pointer reached end
    return res




