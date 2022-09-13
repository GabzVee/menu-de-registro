import util

def line(leng =  42):
    return '-' * leng


def text(txt):
    print(line())
    print(txt.center(42))
    print(line())


def main(list):
    text('MAIN MENU')
    c = 1
    for item in list:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(line())
    option = util.inputInt('\033[33mYour option:\033[m ')
    return option