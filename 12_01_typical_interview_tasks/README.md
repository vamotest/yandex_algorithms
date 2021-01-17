

## Index
* [A. Значения функции](#a-значения-функции)
* [B. Любители конференций](#b-любители-конференций)
* [C. Списочная форма](#c-списочная-форма)
* [D. Убрать очки](#d-убрать-очки)
* [E. Работа из дома](#e-работа-из-дома)
* [F. База данных](#f-база-данных)
* [G. Анаграммы](#g-анаграммы)
* [H. Палиндром](#h-палиндром)
* [I. Двоичная система](#i-двоичная-система)
* [J. Обеды](#j-обеды)
* [K. Единицы](#k-единицы)
* [L. Лишняя буква](#l-лишняя-буква)
* [M. Частоты](#m-частоты)
* [N. Степень четырех](#n-степень-четырех)
* [O. И снова Вася](#-и-снова-вася)
* [P. Комбинации](#p-комбинации)
* [Q. Статистика](#q-статистика)

**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## A. Значения функции

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/A/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/A.%20Function%20values.py)
```
Write the function code y = ax^2 + bx + c.
At the input through a space are given numbers a, x, b, c.
```

### Input format
```
На вход через пробел подаются числа a, x, b, c.
```

### Output format
```
Выведите одно число - значение функции в точке x.
```

### Examples

**Example №1**
|    Input   | Output |
|:----------:|:------:|
| -8 -5 -2 7 |  -183  |

**Example №2**
|   Input   | Output |
|:---------:|:------:|
| 8 2 9 -10 |   -40  |


**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## B. Любители конференций

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/B/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/B.%20Conference%20fans.py)
```
На IT-конференции присутствовали студенты из разных вузов со всей страны. 
Для каждого студента известен ID университета, в котором он учится.

Тимофей предложил Рите выяснить, из каких k вузов на конференцию пришло 
больше всего учащихся.
```

### Input format
```
1) Количество студентов в списке —– n (1 ≤ n ≤ 15 000).
2) Через пробел записаны n целых чисел —– ID вуза каждого студента. 
Каждое из чисел находится в диапазоне от 0 до 10 000.
3) Записано одно число k.
```

### Output format
```
Выведите через пробел k ID вузов с максимальным числом участников.
Они должны быть отсортированы по убыванию популярности 
(по количеству гостей от конкретного вуза). 

Если более одного вуза имеет одно и то же количество учащихся, 
то выводить их ID нужно в порядке возрастания.
```

### Examples

**Example №1**
|     Input     | Output |
|:-------------:|:------:|
| 7             |  1 2 3 |
| 1 2 3 1 2 3 4 |        |
| 3             |        |

**Example №2**
|    Input    | Output |
|:-----------:|:------:|
| 6           |    1   |
| 1 1 1 2 2 3 |        |
| 1           |        |


**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## C. Списочная форма

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/C/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/C.%20List%20form.py)
```
Вася просил Аллу помочь решить задачу. На этот раз по информатике.

Для неотрицательного целого числа X списочная форма — это массив его цифр
слева направо. К примеру, для 1231 списочная форма будет [1,2,3,1]. 
На вход подается количество цифр числа Х, списочная форма неотрицательного 
числа Х и число K. Числа К и Х не превосходят 10000.

Нужно вернуть списочную форму числа X + K.
```

### Input format
```
В первой строке - длина списочной формы числа X. На следующей строке - сама 
списочная форма с цифрами записанными через пробел. 
В последней строке записано число K.
```

### Output format
```
Выведите списочную форму числа X+K.
```

### Examples

**Example №1**
|  Input  |  Output |
|:-------:|:-------:|
| 4       | 1 2 3 4 |
| 1 2 0 0 |         |
| 34      |         |


**Example №2**
| Input | Output |
|:-----:|:------:|
| 2     |  1 1 2 |
| 9 5   |        |
| 17    |        |


**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## D. Убрать очки

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/D/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/D.%20Remove%20points.py)
```
Гоша решил убрать из статистики дни, когда ничего в «Черепашеньке» 
не заработал и не проиграл. Дан список заработанных очков. 
Нужно удалить из него нули. 

Дополнительную память больше O(1) использовать нельзя.
```

### Input format
```
В первой строке - одно число n. Во второй - n целых чисел через пробел.
```

### Output format
```
Напечатайте очки за все дни, где выигрыш был отличен от нуля.
```

### Examples

**Example №1**
|        Input       |    Output    |
|:------------------:|:------------:|
| 8                  | -1 1 2 -1 -4 |
| -1 0 0 1 2 -1 -4 0 |              |


**Example №2**
|     Input    |    Output    |
|:------------:|:------------:|
| 5            | -1 1 2 -1 -4 |
| -1 1 2 -1 -4 |              |


**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## E. Работа из дома

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/E/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/E.%20Convert%20to%20binary%20system.py)
```
Алла осталась работать из дома. Во время её рабочего видеозвонка с Тимофеем 
и Гошей подошёл Вася. Он решил показать им написанный им недавно код функции,
переводящей целое число из десятичной системы в двоичную. 
Ему было интересно, смогут ли ребята написать более короткую, 
или более эффективную программу.

Не используйте встроенные средства языка по переводу чисел 
в бинарное представление.
```

### Input format
```
На вход подается целое число в диапазоне от 0 до 10000.
```

### Output format
```
Выведите двоичное представление этого числа.
```

### Examples

**Example №1**
| Input | Output |
|:-----:|:------:|
| 5     |   101  |

**Example №2**
| Input | Output |
|:-----:|:------:|
| 14    |  1110  |

**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## F. База данных

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/F/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/F.%20Find%20duplicate.py)
```
Алла писала код, добавляющий запись в новую таблицу базы данных. 
И вдруг получила ошибку duplicate foreign key constraint. 
В тот же момент её отвлекла Рита. Алла случайно закрыла окно терминала 
с информацией о том, какое именно значение стало причиной ошибки. 
Зато у неё сохранился список id, использованных при запросе. 
Помогите ей выяснить, какой id стал причиной ошибки.

Дан массив чисел, состоящий  из n целых чисел. Одно число встречается более
одного раза. Нужно определить это число.
```

### Input format
```
В первой строке записано число n, которое не превосходит 1000. 
В следующей строке через пробел записаны n целых чисел, каждое из которых 
также не превосходит 10000.
```

### Output format
```
Выведите одно число.
```

### Examples

**Example №1**
|   Input   | Output |
|:---------:|:------:|
| 5         |    3   |
| 3 1 3 4 2 |        |

**Example №2**
| Input | Output |
|:-----:|:------:|
| 3     |    8   |
| 2 8 8 |        |


**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## G. Анаграммы

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/G/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/G.%20Anagrams.py)
```
Вася вернулся домой под вечер и вспомнил, что ещё не сделал домашнее задание
по русскому языку. Чтобы понять разницу между анаграммой и палиндромом, 
Вася снова обратился к Алле. Она объяснила брату, что два слова — анаграммы, 
если одно можно получить из другого перестановкой букв. 
А палиндром — это слово или фраза, которая читается одинаково, если читать 
слева направо и справа налево. Теперь Васе интересно: как закодить функцию, 
определяющую, анаграммы слова или нет.
```

### Input format
```
Два слова - каждое на отдельной строке.
Слова состоят из строчных букв латинского и русского алфавитов.
```

### Output format
```
Слово True, если слова являются анаграммами друг друга, 
слово False - если не являются.
```

### Examples

**Example №1**
|  Input  | Output |
|:-------:|:------:|
| мошкара |  True  |
| ромашка |        |

**Example №2**
| Input | Output |
|:-----:|:------:|
| кошка |  False |
| лошка |        |

## Примечания
```
Решение должно работать за O(N) и использовать O(1) дополнительной памяти,
где N - максимум из длин строк на входе.
```


**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## H. Палиндром

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/H/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/H.%20Palindrome.py)
```
А теперь помогите Васе понять, будет ли фраза палиндромом. 
Учитываются только буквы и цифры, заглавные и строчные буквы 
считаются одинаковыми.

Решение должно работать за O(N), где N - длина строки на входе.
```

### Input format
```
В единственной строке записана фраза или слово. 
Буквы могут быть только латинские.
```

### Output format
```
Выведите True, если фраза является палиндромом и False, если не является.
```

### Examples

**Example №1**
|              Input             | Output |
|:------------------------------:|:------:|
| A man, a plan, a canal: Panama |  True  |

**Example №2**
| Input | Output |
|:-----:|:------:|
| zo    |  False |


**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## I. Двоичная система

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/I/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/I.%20Binary%20system.py)
```
Тимофей спросил у студента Саши, умеет ли тот работать с числами 
в двоичной системе счисления. Он ответил, что проходил это на одной 
из первых лекций по информатике. Тимофей предложил Саше решить задачку. 
Два числа записаны в двоичной системе счисления. 
Нужно вывести их сумму, также в двоичной системе. 
Встроенную в язык программирования возможность сложения двоичных 
чисел применять нельзя.

Решение должно работать за O(N),
где N - количество разрядов максимального числа на входе.
```

### Input format
```
Два числа в двоичной системе счисления, каждое на отдельной строке. 
Длина каждого числа не превосходит 10000 цифр.
```

### Output format
```
Одно число в двоичной системе счисления.
```

### Examples

**Example №1**
| Input | Output |
|:-----:|:------:|
| 1010  |  10101 |
| 1011  |        |

**Example №2**
| Input | Output |
|:-----:|:------:|
| 1     |   10   |
| 1     |        |


**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## J. Обеды

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/J/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/J.%20Lunches.py)
```
Руководство компании, где работают Гоша с друзьями, подарило каждому сотруднику
два талона на обед в близлежащем ресторане. Сотрудники могли взять талоны 
и записать номер своего бейджика на каждом из них. 
Талон с записанным на нём номером обменивается на обед в ресторане. 
Все сотрудники, кроме одного, сходили в ресторан по талонам дважды. 
Отличившийся сотрудник сходил в ресторан только один раз. 
Нужно вычислить, кто же это такой. По списку номеров на сданных в ресторан
талонах найдите номер отличившегося сотрудника.
```

### Input format
```
На вход подаётся число номеров в списке — n (3 ≤ n ≤ 10^4),
и n натуральных чисел, не превышающих M=10^4, — сам список номеров сотрудников.
Все числа, кроме одного, встречаются в списке дважды.
```

### Output format
```
Выведите номер сотрудника, который сходил на обед всего один раз.
```

### Examples

**Example №1**
|        Input        | Output |
|:-------------------:|:------:|
| 5                   |   456  |
| 678 123 456 123 678 |        |

**Example №2**
| Input | Output |
|:-----:|:------:|
| 3     |    2   |
| 1 1 2 |        |

## Примечания
```
Эту задачу можно решить за O(n) времени и O(1) дополнительной памяти
— подумайте, как это сделать!
```


**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## K. Единицы

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/K/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/K.%20One%20in%20a%20binary%20number.py)
```
Пока Вася писал программу про степени четверки, погода на улице ухудшилась.
Он долго не расстраивался и придумал новую задачку! 
Ему нравится работать с системами счисления. 

И вот что на этот раз получилось: Дано целое положительное число. 
Нужно посчитать, сколько 1 встречается в двоичной записи этого числа.
```

### Input format
```
На вход подается число в диапазоне от 1 до 10000
```

### Output format
```
Выведите одно число - количество единиц.
```

### Examples

**Example №1**
| Input | Output |
|:-----:|:------:|
| 5     |    2   |

**Example №2**
| Input | Output |
|:-----:|:------:|
| 12    |    2   |


**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## L. Лишняя буква

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/L/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/L.%20Extra%20letter.py)
```
Васе очень понравилась задача про анаграммы и он придумал к ней модификацию. 
Есть 2 строки s и t, состоящие только из строчных букв. 
Строка t получена перемешиванием букв строки s и добавлением 1 буквы
в случайную позицию. Нужно найти добавленную букву.
```

### Input format
```
На вход подаются строки s и t, разделенные переносом строки.
```

### Output format
```
Выведите лишнюю букву.
```

### Examples

**Example №1**
| Input | Output |
|:-----:|:------:|
| abcd  |    e   |
| abcde |        |

**Example №2**
| Input | Output |
|:-----:|:------:|
| go    |    g   |
| ogg   |        |

**Example №3**
|  Input | Output |
|:------:|:------:|
| xtkpx  |    c   |
| xkctpx |        |


**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## M. Частоты

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/M/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/M.%20Frequencies.py)
```
На вход подается строка длиной от 1 до 10000 символов. 
Нужно отсортировать её в порядке частот букв по встречаемости. 
Заглавные и строчные буквы считаются разными. 
Если частота одинаковая, нужно применить вторичную сортировку лексикографически.
```

### Input format
```
Одна строка длиной не более 10000 символов.
```

### Output format
```
Строка, в которой символы отсортированы в порядке убывания частотности.
```

### Examples

**Example №1**
| Input | Output |
|:-----:|:------:|
| tree  |  eert  |

**Example №2**
|   Input  |  Output  |
|:--------:|:--------:|
| ztwidhfk | dfhiktwz |


**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## N. Степень четырех

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/N/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/N.%20Degree%20of%20four.py)
```
Вася на уроке математики проходил степени. Он хочет написать программу,
которая определяет, будет ли положительное целое число степенью четверки.
```

### Input format
```
На вход подается целое число в диапазоне от 1 до 10000.
```

### Output format
```
True, если число является степенью четырех, False - в обратном случае.
```

### Examples

**Example №1**
| Input | Output |
|:-----:|:------:|
| 15    |  False |

**Example №2**
| Input | Output |
|:-----:|:------:|
| 16    |  True  |


**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## O. И снова Вася

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/O/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/O.%20User%20visits.py)
```
Вы думали, что эта задача про Васю, но она про Тимофея.

Тимофей собирает метрики посещаемости сайта за последний месяц с двух серверов.
На каждой машине имеется список id пользователей, отсортированный в порядке
от минимального количества посещений к максимальному, вам известно число
посещений каждого пользователя. 

Пользователи, не посещавшие сайт в последний месяц, не учитываются. 
Вам нужно сделать общий список числа посещений для двух серверов так, 
чтобы в нем тоже числа шли по возрастанию. 

Так как сайт Тимофея очень популярен, то данных о пользователях много, 
поэтому Тимофей может позволить себе только линейное время работы алгоритма.
```

### Input format
```
1) Записаны количества посещений пользователей с первого сервера через пробел,
в конце - k нулей. 
2) Записано число m - количество пользователей, пришедших с первого сервера 
(без учета нулей в конце списка). 
3) Число k - которое, помимо количества нулей, также является длиной 
списка пользователей со второго сервера. 
4) Список посещений со второго сервера (k штук).

Количество посещений каждого пользователя не превосходит 10000, 
числа m и k также не превосходят 10000
```

### Output format
```
В одной строке через пробел выведите элементы получившегося списка 
в отсортированном порядке.
```

### Examples

**Example №1**
|    Input    |    Output   |
|:-----------:|:-----------:|
| 1 2 3 0 0 0 | 1 2 2 3 5 6 |
| 3           |             |
| 3           |             |
| 2 5 6       |             |

**Example №2**
|  Input |  Output |
|:------:|:-------:|
| 8 98 0 | 8 65 98 |
| 2      |         |
| 1      |         |
| 65     |         |


**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## P. Комбинации

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/P/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/P.%20Combinations.py)
```
На клавиатуре старых мобильных телефонов каждой цифре
соответствовало несколько букв. 

Примерно так:
characters = {
    2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
    6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'
}

Вам известно в каком порядке были нажаты кнопки телефона, 
без учета повторов. Напечатайте все комбинации букв, которые можно набрать
такой последовательностью нажатий.
```

### Input format
```
На вход подается строка, состоящая из цифр 2-9 включительно. 
Длина строки не превосходит 10 символов.
```

### Output format
```
Выведите все возможные комбинации букв через пробел.
```

### Examples

**Example №1**
| Input |           Output           |
|:-----:|:--------------------------:|
| 23    | ad ae af bd be bf cd ce cf |

**Example №2**
| Input |                Output               |
|:-----:|:-----------------------------------:|
| 92    | wa wb wc xa xb xc ya yb yc za zb zc |


**[⬆ Back to Global Index](https://github.com/vamotest/yandex_algorithms#index)**
**[⬆ Back to Index](#index)**
## Q. Статистика

### Task 
[Contest](https://contest.yandex.ru/contest/18338/problems/Q/) | [Solution](https://github.com/vamotest/yandex_algorithms/blob/master/12_01_typical_interview_tasks/Q.%20Statistics.py)
```
В метро Гоша обычно играет в мобильную игру «Черепашенька». 
Он долго собирал данные о том, сколько очков зарабатывает и проигрывает в день.

Гоша собирает необычную статистику. 
Нужно определить максимальное произведение заработанных очков среди троек дней,
в которые сумма очков равна нулю, и произведение является положительным числом.
```

### Input format
```
1) Записано число n (1 ≤ n ≤ 2000). 
2) Через пробел записаны n целых чисел. 
Числа находятся в диапазоне от -100000 до 100000.
```

### Output format
```
Выведите максимальное положительное произведение заработанных за три дня очков
среди троек дней, в которые их сумма равна нулю. 
Если троек, удовлетворяющих условиям, нет, нужно вывести -1.
```

### Examples

**Example №1**
|     Input     | Output |
|:-------------:|:------:|
| 5             |    6   |
| -2 -1 3 -1 -2 |        |

**Example №2**
|     Input    | Output |
|:------------:|:------:|
| 5            |   -1   |
| -2 1 1 -1 -2 |        |

## Примечания
```
Решение должно использовать O(1) дополнительной памяти 
(помимо массива, в который считаны входные данные).
```