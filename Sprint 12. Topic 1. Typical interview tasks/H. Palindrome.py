
def define_polindrome(first, second):
    if first == second:
        return True
    else:
        return False


if __name__ == '__main__':

    first_phrase = ''.join(
        letter for letter in (str(input())) if letter.isalpha()
    ).lower()
    
    second_phrase = ''.join(
        letter for letter in first_phrase[::-1] if letter.isalpha()
    ).lower()
    
    result = define_polindrome(first_phrase, second_phrase)
    print(result)
