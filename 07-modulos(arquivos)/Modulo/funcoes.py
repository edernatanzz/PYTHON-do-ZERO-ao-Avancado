

def somar():
    print('Esta funcao vai somar valores')


def multi():
    print('esta funcao vai multiplicar valores')

#procurar um item
def find_index(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return 'nao encontrado'

