import sys
import re
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Renames selected functions")
    parser.add_argument(dest="names", type=str, help="list of function names")
    parser.add_argument(dest="file", type=str, nargs='*', default=" ", help="python script name")
    parser.add_argument("--transform_comments", action="store_true", help="optional, for multiple lines comments")
    args = parser.parse_args()

    list_of_functions = re.split(r"\W+", args.names)

    if args.file != " ":
        for file in args.file:
            fin = open(file, "rt")
            data = fin.read()
            for i in range(0, len(list_of_functions), 2):   
                data = data.replace(list_of_functions[i] + "(", list_of_functions[i+1] + "(")
            fin.close()
            fin = open(file, "wt")
            fin.write(data)
            fin.close()

            if args.transform_comments:
                with open(file, "rt") as fh:
                    tab = []
                    for line in fh:
                        phoneNumRegex = re.compile(r'#.*\n')
                        tab.append(phoneNumRegex.findall(line))
                    fh.close()
                
                lista = [x for x in tab if x]

                comment = ""

                for element in lista:
                    comment += element[0]

                comment = comment.split("\n#")

                size = len(comment)

                i=0
                for element in comment:
                    comment[i] = element.replace("\n", "")
                    i+=1

                string = ""

                for element in comment:
                    string += element
                    
            fin = open(file, "rt")
            data = fin.read()
            for i in range(len(lista)):
                if i == 0:
                    data = re.sub(lista[i][0], string + "\n", data)
                else:
                    data = re.sub(lista[i][0], "\n", data)
            fin.close()
            fin = open(file, "wt")
            fin.write(data)
            fin.close()

    elif args.file == " ":
        args.file = input("Enter text: ")
        for i in range(0, len(list_of_functions), 2):   
            args.file = args.file.replace(list_of_functions[i], list_of_functions[i+1])
        print(args.file)