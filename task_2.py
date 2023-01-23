# 2) Найти сумму чисел списка стоящих на нечетной позиции

import random

arr = [random.randint(1, 50) for i in range(1, 11)]
print(arr)
def Calculate(x):
    arr_ = [value for count, value in enumerate(x) if count % 2 == 1]
    print(arr_)
    return sum(arr_)


print(Calculate(arr))