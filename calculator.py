import argparse
import math


def calculate(x, operand, y=None):# y= none for the sqrt operation
    if operand == "+":
        return x + y
    elif operand == "-":
        return x - y
    elif operand == "*":
        return x * y
    elif operand == "/":
        # can't divide by zero
        if y == 0:
            return "Error: Division by zero"
        return x / y
    # not a operand
    ## these were made in feature
    elif operand == '^':
        return x ** y
    elif operand == 'sqrt':
        if x >= 0:
            return math.sqrt(x)
        else:
            return "Error: cannot sqrt negative numbers"
    else:
        return "Invalid operator"




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic Calculator")
    parser.add_argument("x", type=float, help="First number")
    parser.add_argument("op", choices=["+", "-", "*", "/","^", "sqrt"], help="Operator (+, -, *, /, ^, sqrt)")
    parser.add_argument("y", type=float, nargs= "?", help="Second number, but not needed for sqrt operation") # added nargs to omit y for sqrt

    args = parser.parse_args()
    result = calculate(args.x, args.op, args.y)
    print("Result:", result)