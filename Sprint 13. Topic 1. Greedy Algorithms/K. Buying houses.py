"""
https://contest.yandex.ru/contest/18360/problems/K/

Тимофей решил купить несколько домов на знаменитом среди разработчиков
Алгосском архипелаге.
Он нашёл n объявлений о продаже, где указана стоимость
каждого дома в алгосских франках.
А у Тимофея есть k франков.

Помогите ему определить, какое наибольшее количество домов на Алгосах
он сможет приобрести за эти деньги.

Формат ввода
В первой строке через пробел записаны натуральные числа n и k.
n — количество домов, которые рассматривает Тимофей, оно не превосходит 1000;
k — общий бюджет, не превосходит 10000;
В следующей строке через пробел записано n стоимостей домов.
Каждое из чисел не превосходит 10000. Все стоимости — натуральные числа.

Формат вывода
Выведите одно число —– наибольшее количество домов,
которое может купить Тимофей.
"""

n, budget = input().split()
houses_value = list(map(int, input().split()))

result = 0
for value in sorted(houses_value):
    if value <= budget:
        result += 1
        budget -= value

print(result)
