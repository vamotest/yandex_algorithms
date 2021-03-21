"""
https://contest.yandex.ru/contest/18360/problems/D/

Реализуйте код алгоритма заполнения рюкзака, рассмотренного в лекции:
* Взять наиболее ценный предмет, который поместится в рюкзак.
* Выбрать следующий по стоимости товар с учётом того, что для него осталось
место в рюкзаке.

Формат ввода
В первой строке записано целое число с в диапазоне от 0 до 1000
— вместимость рюкзака.

Во второй — число n — количество предметов. Оно не больше 10000.

В следующих n строках записано по 2 числа, разделенные пробелом:
стоимость предмета и его вес. Оба числа не превосходят 1000

Формат вывода
Нужно в строке вывести в отсортированном порядке номера предметов,
которые будут выбраны. Номер предмета - это порядковый номер его появления
во входных данных. (Индексация начинается с нуля)
"""


def collect_backpack(capacity, n):
    
    array = []
    for i in range(n):
        value, weight = input().split()
        array.append((int(value), int(weight), i))
        
    array.sort(key=lambda elem: (-elem[0], elem[1], elem[2]))

    result = []
    for item in range(n):
        item_weight = array[item][1]
    
        if item_weight <= capacity:
            capacity -= item_weight
            
            item_index = array[item][2]
            result.append(item_index)
            
    result.sort()
    return result


if __name__ == "__main__":
    print(*collect_backpack(int(input()), int(input())))
