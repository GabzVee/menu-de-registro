def inputInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('ERROR! EXPECTED AN INT VALUE.')
            continue
        except (KeyboardInterrupt):
            print('Program has been shut down by the user.')
            return 0
        else:
            return num


def inputFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('ERROR! EXPECTED A FLOAT VALUE.')
            continue
        except (KeyboardInterrupt):
            print('Program has been shut down by the user.')
            return 0
        else:
            return num