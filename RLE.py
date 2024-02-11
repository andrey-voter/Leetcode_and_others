# Дан список чисел, требуется представить его в виде строки, "сжимая" подряд идущие одинаковые числа,
# в формате <число:количество_повторов>.
# Если число не повторяется, то единицу выводить не нужно.
# Пример: [1,1,1,3,5,5] -> "1-3;3;5-2"

def compress_list(nums: list[int]) -> str:
    if not nums:
        return ''

    compressed = []
    p = 0
    cur_cnt = 1
    while p < len(nums) - 1:
        if nums[p] == nums[p + 1]:
            cur_cnt += 1
        else:
            compressed.append(f"{nums[p]}-{cur_cnt}") if cur_cnt != 1 else compressed.append(f"{nums[p]}")
            cur_cnt = 1
        p += 1
    compressed.append(f"{nums[p]}-{cur_cnt}") if cur_cnt != 1 else compressed.append(f"{nums[p]}")
    return ';'.join(compressed)


a = [1, 1, 1, 3, 5, 5, 1, 111]
print(compress_list(a))
