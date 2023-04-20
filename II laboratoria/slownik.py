import sys

print('Ładowanie modułu "{0}"'.format(__name__))
############################################

slownik = {}

def zapisz():
    for element in sys.argv[1:]:
        if element == "--slownik" or element == "--moduł=slownik":
            continue
        else:
            try:
                element = int(element)   
                slownik[element] = slownik.get(element, 0) + 1
            except:
                continue

def wypisz():
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    ############################################

    string = ""

    sorted_slownik = sorted(slownik.keys(), key = int)

    for key in sorted_slownik:
        if key == sorted_slownik[-1]:
            string += (str(key) + ":" + str(slownik[key]))
        else:
            string += (str(key) + ":" + str(slownik[key]) + ",")
    
    print(string)

############################################
print('Załadowano moduł "{0}"'.format(__name__))