import sys
import getopt

try:
    option, arguments = getopt.getopt(sys.argv[1:], "", ["moduł="])
except:
    print("Invalid input! Provide --moduł=lista/slownik")
    exit()

if option[0][1] == "lista":
    import lista
    lista.zapisz()
    lista.wypisz()
elif option[0][1] == "slownik":
    import slownik
    slownik.zapisz()
    slownik.wypisz()
else:
    print("Wrong input! Type --lista or --slownik and then arguments.")