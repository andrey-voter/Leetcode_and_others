import random


def rand7():
    return random.randint(1, 7)


def rand10():
    """
    :rtype: int
    """
    def initialize():
        return rand7() - 1, rand7() - 1

    num1, num2 = initialize()
    while (comb := 7 * num1 + num2) > 39:
        num1, num2 = initialize()
    return comb // 4 + 1


for i in range(10):
    print(rand10())


