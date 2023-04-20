import sys

for number in sys.argv[1:]:
    try:
        if int(number) < 2:
            continue
        elif int(number) == 2:
            print(number)
        else:
            for i in range(2, int((int(number)/2)+1)):
                if int(number)%i == 0:
                    break
            else:
                print(number)
    except:
        continue