import argparse


def calculate(x, operand, y):
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
    else:
        return "Invalid operator"




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic Calculator")
    parser.add_argument("x", type=float, help="First number")
    parser.add_argument("op", choices=["+", "-", "*", "/"], help="Operator (+, -, *, /)")
    parser.add_argument("y", type=float, help="Second number")

    args = parser.parse_args()
    result = calculate(args.x, args.op, args.y)
    print("Result:", result)