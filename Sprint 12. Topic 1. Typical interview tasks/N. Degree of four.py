import math


def is_degree_of_four(number):
    result = math.modf(math.log(number, 4))[0]
    
    if result == 0.0:
        return True
    else:
        return False


if __name__ == '__main__':
    is_degree_of_four = is_degree_of_four(int(input()))
    print(is_degree_of_four)
