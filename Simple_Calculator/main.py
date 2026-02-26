import art


def add (a,b):
    return a + b

def sub (a,b):
    return a - b

def mul (a,b):
    return a * b

def dev (a,b):
    return a / b

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": dev,
}

def calculator():
    print(art.logo)
    stop_counting= True
    num1 = float(input("What's the first number?: "))
    while stop_counting:
        for symbol in operations:
            print(symbol)
        operation= input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        result = operations[operation](a = num1, b= num2)
        print ( f"{num1} {operation} {num2} = {result}")

        continue_count = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or : ")

        if continue_count == "y":
            num1 = result
        else:
            stop_counting = False
            print("\n"*20)
            calculator()
calculator()