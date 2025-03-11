while True:
    number1 = float(input("Enter first number: "))
    operator = input("Enter (+,-,*,/): ")
    number2 = float(input("Enter second number: "))
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        if number2 == 0:
            result = "Error!"
        else:
            result = number1 / number2
    else:
        result = "Unknown!"
    print("Result:", result)
    if input("Do you want to continue? Enter (yes/no): ").strip().lower() != "yes":
        break
