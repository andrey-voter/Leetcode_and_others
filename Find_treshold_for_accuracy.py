def find_threshold(probs: list[float], labels: list[int]) -> float:
    """Задача: Поиск оптимального порога для accuracy.
    На входе - вероятности и правильные метки классов для примеров из отложенной выборки.
    Решение о принадлежности объекта к классу 1 примиается так:
    prob > threshold, где prob - вероятность объекта принадлежности к классу 1."""
    probs.sort()
    labels.sort()

    TP = sum(labels)
    TN = threshold = 0
    accuracy = TP / len(labels)

    for i in range(len(probs)):
        if labels[i] == 0:
            TN += 1
        else:
            TP -= 1
        if i == len(probs) - 1 or probs[i] != probs[i + 1]:
            cur_accuracy = (TP + TN) / len(probs)
            if cur_accuracy >= accuracy:
                accuracy = cur_accuracy
                threshold = probs[i]

    return threshold


assert find_threshold([0.1, 0.2, 0.3, 0.4, 0.55, 0.7], [0, 0, 0, 1, 1, 1]) == 0.3
assert find_threshold([0.1, 0.99], [0, 1]) == 0.1
