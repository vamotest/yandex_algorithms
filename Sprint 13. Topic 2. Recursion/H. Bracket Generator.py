
def make_bs(number, co=0, cc=0, ans=''):
    if co + cc == 2 * number:
        print(ans)
        return
    if co < number:
        make_bs(number, co + 1, cc, ans+'(')
    if co > cc:
        make_bs(number, co, cc + 1, ans+')')


if __name__ == '__main__':
    make_bs(int(input()))
