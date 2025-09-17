
from calculator import calculate

def main():
   
    sum = calculate(5, "+", 3)
    print(f"The answer should be 8. Operation output {sum}.\n")

    division_by_zero = calculate(5, "/", 0)
    print(f"The answer should Error: division by zero. Operation output {division_by_zero}.\n")

    sqrt_test = calculate(16, "sqrt")
    print(f"The answer should be 4. Operation output {sqrt_test}.\n")

    negative_sqrt = calculate(-16, "sqrt")
    print(f"The answer should be Error: cannot sqrt negative numbers. Operation output {negative_sqrt}.\n")

    wrong_operand = calculate(5 , "%", 2)
    print(f"The answer should be Invalid operator. Operation output {wrong_operand}.\n")




if __name__ == "__main__":
    main()
