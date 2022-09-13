import menu

def arcExist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createArc(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print("ERROR! Archive couldn't be created")
    else:
        print('Archive created successfully')


def readArc(name):
    try:
        a = open(name, 'rt')
    except:
        print("ERROR! Couldn't read the archive")
    else:
        menu.text('USERS REGISTERED')
        for line in a:
            data = line.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} years old')
    finally:
        a.close()


def signIn(arq, name='unknown', age=0):
    try:
        a = open(arq, 'at')
    except:
        print("ERROR! Archive couldn't be open")
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('Error during the writing')
        else:
            print('New register added')
            a.close()
