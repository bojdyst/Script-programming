import sys

print('Ładowanie modułu "{0}"'.format(__name__))
############################################

lista = []
result = []

def zapisz():
    for element in sys.argv[1:]:
        if element == "--lista" or element == "--moduł=lista":
            continue
        else:
            try:
                lista.append(int(element))
            except:
                continue

    for i in sorted(lista, key = int):
        result.append(str(i) + ":" + str(lista.count(i)))
    
    lista.clear()

    for i in result:
       if i not in lista:
          lista.append(i)

def wypisz():
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    ############################################

    string = ""
    for i in lista:
        if i == lista[-1]:
            string += i
        else:
            string += i + ","

    print(string)

############################################
print('Załadowano moduł "{0}"'.format(__name__))