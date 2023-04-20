from inspect import signature

def argumenty(argumenty):
    def inner(f):
        def wrapper(*args, **kwargs):
            f_args = len(signature(f).parameters)
            passed_args = list(args)
            k = f_args - len(passed_args)
            if k > len(argumenty):
                raise TypeError(f'{f.__name__}() takes exactly {f_args} arguments ({len(argumenty) + len(passed_args)} given)')
            global last_not_used
            last_not_used = 0
            if len(list(args)) == 0:
                last_not_used = argumenty[f_args]
            for i in range(0, k):
                passed_args.append(argumenty[i])
            return f(*passed_args)
        return wrapper
    return inner

class Operacje:
    argumentySuma=[4,5]
    argumentyRoznica=[4,5,6]

    def __init__(self):
        self.update()

    @argumenty(argumentySuma)
    def suma(self, a, b, c):
        pass

    def updated_suma(self, a, b, c):
        #print("%d+%d+%d=%d" % (a, b, c, a+b+c))
        if last_not_used != 0:
            return last_not_used
        else:
            return a+b+c

    @argumenty(argumentyRoznica)
    def roznica(self, x, y):
        pass
        
    def updated_roznica(self, x, y):
        #print("%d-%d=%d" % (x, y, x-y))
        if last_not_used != 0:
            return last_not_used
        else:
            return x-y
        
    def update(self):
        self.suma = (argumenty(Operacje.argumentySuma))(self.updated_suma)
        self.roznica = (argumenty(Operacje.argumentyRoznica))(self.updated_roznica)

    def __setitem__(self, key, value):
        for val in value:
            if type(val) != int:
                raise TypeError
        if key == 'suma':
            Operacje.argumentySuma = value
        elif key == 'roznica':
            Operacje.argumentyRoznica = value
        self.update()

# if __name__ == '__main__':
    # op=Operacje()
    # op.suma(1,2,3) #Wypisze: 1+2+3=6
    # op.suma(1,2) #Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
    # op.suma(1) #Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
    # #op.suma() #TypeError: suma() takes exactly 3 arguments (2 given)
    # op.roznica(2,1) #Wypisze: 2-1=1
    # op.roznica(2) #Wypisze: 2-4=-2
    # wynik=op.roznica() #Wypisze: 4-5=-1
    # print(wynik) #Wypisze: 6

    # #Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
    # op['suma']=[1,2,3]
    # #oznacza, że   argumentySuma=[1,2]

    # #Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
    # op['roznica']=[1,2,3,4,5]
    
    # op.suma(1)
    # op.roznica()
    # #oznacza, że   argumentyRoznica=[1,2,3]
