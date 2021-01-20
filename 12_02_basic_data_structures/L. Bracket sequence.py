
def is_correct_bracket_seq(string):
    while ('[]' in string) or ('()' in string) or ('{}' in string):
        string = string.replace('[]', '')
        string = string.replace('()', '')
        string = string.replace('{}', '')
    return not bool(string)


if __name__ == '__main__':
    print(is_correct_bracket_seq(input()))
