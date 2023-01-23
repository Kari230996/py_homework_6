# 4) Сформировать список из N членов последовательности

N = int(input("Choose a number: "))

res = [(-3)**i for i in range(N+1)]
print(res)