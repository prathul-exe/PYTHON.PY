import math

while True:
    print("\n--- Scientific Calculator ---")
    print("""
1  -> Addition
2  -> Subtraction
3  -> Multiplication
4  -> Division
5  -> Power (x^y)
6  -> Square Root
7  -> Sin
8  -> Cos
9  -> Tan
10 -> Log10
11 -> Ln
0  -> Exit
""")

    choice = int(input("Enter your choice: "))

    match choice:
        case 0:
            print("Calculator Closed")
            break

        case 1 | 2 | 3 | 4 | 5:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            match choice:
                case 1:
                    print("Result:", a + b)
                case 2:
                    print("Result:", a - b)
                case 3:
                    print("Result:", a * b)
                case 4:
                    print("Result:", a / b if b != 0 else "Error: Division by zero")
                case 5:
                    print("Result:", math.pow(a, b))

        case 6 | 7 | 8 | 9 | 10 | 11:
            x = float(input("Enter number: "))

            match choice:
                case 6:
                    print("Result:", math.sqrt(x))
                case 7:
                    print("Result:", math.sin(math.radians(x)))
                case 8:
                    print("Result:", math.cos(math.radians(x)))
                case 9:
                    print("Result:", math.tan(math.radians(x)))
                case 10:
                    print("Result:", math.log10(x))
                case 11:
                    print("Result:", math.log(x))

        case _:
            print("Invalid choice")
