from collections import Counter


def find_person(persons):
    d = Counter(persons)
    return [k for k, v in d.items() if (v % 2) != 0]


if __name__ == '__main__':
    n = int(input())
    persons_list = list(map(int, input().split()))
    person = find_person(persons_list)
    print(*person)
