
def anagram(f, d):
    n = 0
    for i in range(len(f)-len(d)+1):
        if sorted(d) == sorted(f[i:len(d)+i]):
            n += 1
    print(n)


if __name__ == '__main__':
    anagram(input(), input())
