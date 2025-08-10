try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Choose operation:")
    print("press + for addition")
    print("press - for subtraction")
    print("press * for multiplication")
    print("press / for division")
    o = input("Enter operation: ")
    match o:
        case "+":
            print(f"The result is {a + b}")
        case "-":
            print(f"The result is {a - b}")
        case "*":
            print(f"The result is {a * b}")
        case "/":
            if b != 0:
                print(f"The result is {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation selected.")
except Exception as e:
    print("Enter a valid value of a and b ")