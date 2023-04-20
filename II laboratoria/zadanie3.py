import sys

if sys.argv[1] == "--lista":
    import lista
    lista.zapisz()
    lista.wypisz()
elif sys.argv[1] == "--slownik":
    import slownik
    slownik.zapisz()
    slownik.wypisz()
else:
    print("Wrong input! Type --lista or --slownik and then arguments.")