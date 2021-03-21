"""
https://contest.yandex.ru/contest/18360/problems/H/

Во сне Гоша долго играл в игру Лампочка. Он то выигрывал, то проигрывал.
Ему стало интересно, сколько максимум партий подряд он получал большее
количество очков, чем в предыдущей.

Формат ввода
В первой строке записано число элементов массива n.
Оно не превосходит 100000

Далее в строку записаны n чисел, каждое из которых
по модулю не превосходит 1000

Формат вывода
Нужно вывести одно число, равное длине наибольшего возрастающего подмассива

Ввод
9
5 6 3 5 7 8 9 1 2

Вывод
5
"""


def get_subarray_length(array, array_elements, count=1):
    elem = []
    for i in range(1, array_elements):
        if array[i] > array[i - 1]:
            count += 1
        else:
            elem.append(count)
            count = 1
    elem.append(count)
    print(elem)
    return max(elem)


if __name__ == '__main__':
    elements = int(input())
    li = [int(score) for score in input().split()]
    print(get_subarray_length(li, elements))
