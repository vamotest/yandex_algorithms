from itertools import zip_longest


def define_anagrams(first, second):
    li = list(zip_longest(first, second))
    
    for letter in li:
        
        if letter[0] != letter[1]:
            return letter[1]


if __name__ == '__main__':
    first_word = ''.join(sorted(list(str(input()))))
    second_word = ''.join(sorted(list(str(input()))))
    
    result = define_anagrams(first_word, second_word)
    print(result)
