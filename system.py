import menu
import util
import archive
from time import sleep

arq = 'Userslist.txt'

if not archive.arcExist(arq): 
    archive.createArc(arq)


while True:
    option = menu.main(['View the list of registered users', 'Register a new user', 'Exit program'])
    if option == 1:
        archive.readArc(arq)
    elif option == 2:
        menu.text('NEW REGISTER')
        name = str(input('Name: '))
        age = util.inputInt('Age: ')
        archive.signIn(arq, name, age)
    elif option == 3:
        menu.text('Exiting the system...')
        break
    else:
        print('\033[31mERROR! Choose a valid option\033[m')
        sleep(2)