import re

def divide_text_on_str_int(text):
    str = re.findall("[a-ząćęłóśźż]+", text, re.I)
    num = re.findall("[0-9]+", text)
    return (str, num)


if __name__ == '__main__':
    while True:
        try:    
            text = input("Enter text: ")
            text_after_dividing = divide_text_on_str_int(text)
            
            if len(text_after_dividing[1]) != 0 and len(text_after_dividing[0]) == 0:
                print("Liczba:", *text_after_dividing[1])
            elif len(text_after_dividing[0]) != 0  and len(text_after_dividing[1]) == 0:
                print("Wyraz:", *text_after_dividing[0])
            elif len(text_after_dividing[1]) != 0 and len(text_after_dividing[0]) != 0:
                print("Wyraz:", *text_after_dividing[0], "\nLiczba:", *text_after_dividing[1])
        except KeyboardInterrupt:
            exit()