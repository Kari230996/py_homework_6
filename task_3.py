# 3) Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)

import random

arr = [random.randint(1, 50) for i in range(1, 11)]

res = [arr[index]*arr[-index-1] for index in range(len(arr)//2+len(arr)%2)]

print(arr)
print(res)