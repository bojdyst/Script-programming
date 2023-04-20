import sys
##################################
def color(id):
    return id%7+31
##################################
class Klasa(object):
    tab = [1,2,3]

    def __init__(self, tablica, _zmienna1, __zmienna2):
        print("Wywołano metodę '{}()' obiektu\t\t'\033[{}m{}\033[0m'".format(sys._getframe().f_code.co_name, color(id(self)), id(self)))
        self.tab = tablica
        self._zmienna1 = _zmienna1
        self.__zmienna2 = __zmienna2
        
    def __del__(self):
        print("Wywołano metodę '{}()' obiektu\t\t'\033[{}m{}\033[0m'".format(sys._getframe().f_code.co_name, color(id(self)), id(self)))

    def __str__(self):
        return "Wywołano metodę '{}()' obiektu\t\t'\033[{}m{}\033[0m'".format(sys._getframe().f_code.co_name, color(id(self)), id(self))

    def __repr__(self):
        return "Wywołano metodę '{}()' obiektu\t\t'\033[{}m{}\033[0m'".format(sys._getframe().f_code.co_name, color(id(self)), id(self))

    def metodaInstancyjna(self):
        print("Wywołano metodę '{}()' obiektu\t'\033[{}m{}\033[0m'".format(sys._getframe().f_code.co_name, color(id(self)), id(self)))
        print("\tZmienna statyczna:", Klasa.tab)
        print("\tZmienna instancyjna:", self.tab)

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę '{}()' klasy\t\t'{}'".format(sys._getframe().f_code.co_name, cls.__name__))

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę '{}()' klasy\t'{}'".format(sys._getframe().f_code.co_name, __class__.__name__))
        

print("Załadowano zawartość pliku '{}'".format(__file__))