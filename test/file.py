import os

curr_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(curr_dir)


def listtostr(list):
        return ''.join(list)


lista = [1, 2, 3]
print(listtostr(str(e) for e in lista))
