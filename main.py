import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)
    num1 = float(input("What is the first number?: "))
    calc = True

    while calc:
        print("+\n-\n*\n/")
        opt = input("Pick and operation: ")
        num2 = float(input("What is the next number?: "))
        result = operations[opt](num1, num2)
        print(f"{num1} {opt} {num2} = {result}")
        cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if cont == 'n':
            calc = False
            print("\n" * 20)
            calculator()
        elif cont == 'y':
            num1 = result


calculator()
