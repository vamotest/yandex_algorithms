
def define_anagrams(first, second):

    if first == second:
        return True
    else:
        return False


if __name__ == '__main__':

    first_word = ''.join(sorted(list(str(input()))))
    second_word = ''.join(sorted(list(str(input()))))
    
    result = define_anagrams(first_word, second_word)
    print(result)
