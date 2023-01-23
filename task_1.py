# 1) Напишите программу, которая принимает на вход координаты двух точек и находит
#    расстояние между ними в 2D пространстве.

a = [int(input(f"Choose {i} for coordinate a: ")) for i in "xy"]
b = [int(input(f"Choose {i} for coordinate a: ")) for i in "xy"]

c = list(zip(a, b))

res = sum([(arr[1] - arr[0])**2 for arr in zip(a, b)])**0.5

print(res)