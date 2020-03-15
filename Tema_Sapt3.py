def add(a,b):
    return a+b
def remove(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if (b == 0):
        print("Operatie inutila")
    else:
        return a/b
def print_partial(value):
    print("Partial este: ")
    print(value)
operatie = 0
total = int(input('Numar: '))
while operatie != "=":
    operatie = input("Operatie:")
    if operatie != "=":
        alt_numar = int(input("Alt numar: "))
    if operatie == "+":
        total = add(total, alt_numar)
        print_partial(total)
    elif operatie == "-":
        total = remove(total, alt_numar)
        print_partial(total)
    elif operatie == "*":
        total = multiply(total, alt_numar)
        print_partial(total)
    elif operatie == "/":
        total = division(total, alt_numar)
        print_partial(total)
else:
    print("Final: ")
    print(total)