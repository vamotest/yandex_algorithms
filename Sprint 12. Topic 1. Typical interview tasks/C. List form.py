
def make_new_form(len_form, form, k):
    form = int(form[:len_form])
    new_form = ' '.join(str(form + k))
    return new_form


def main():
    len_form = int(input())
    form = input().replace(' ', '')
    k = int(input())
    new_form = make_new_form(len_form, form, k)
    print(new_form)


if __name__ == '__main__':
    main()
