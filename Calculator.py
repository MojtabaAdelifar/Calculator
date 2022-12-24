import re

check = True
result = 0

def calculator():
    global check
    global result
    # input function inputs(reads) data from console
    if result == 0:
        equation = input("Enter the equation:")
    else:
        equation = input(str(result))

    if equation == 'exit':
        print("The end, bye.")
        check = False
    else:
        equation = re.sub('[a-zA-z,." "]', '', equation)
        # eval evaluates the equation and returns the value(int)

        if result == 0:
            result = eval(equation)
        else:
            result = eval(str(result) + equation)

while check:
    calculator()