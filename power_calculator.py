def main():
    try:
        number = float(input("Enter number: "))
    except ValueError:
        print("Invalid number input.")
        exit()

    try:
        exponent = int(input("Enter exponent: "))
    except ValueError:
        print("Invalid exponent input.")
        exit()

    result = 1
    for _ in range(exponent):
        result = result * number

    print("Result:", result)

if __name__ == "__main__":
    main()
