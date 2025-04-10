from matrixcopilot import *


# Main program
a = [[0, 0], [-1, -1], [0, 1], [-3, 1], [-1, -2], [0, 1], [0, 0], [0, 0], [0, 0]]
b = [[0, 1], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 1], [1, -1]]
c = [[1, -1], [0, 1], [0, 0], [0, -1], [0, 0], [0, 1], [0, -1, 1], [0, 0], [0, 1]]
d = [[0, 0], [0, -1], [0, 1], [0, 0], [0, -1], [0, 0], [1, -1], [0, -1, 1], [0, 0]]
v = [[0, "2a+3b", "a+2c"], [0, "2a+3b", "a+2c"], [2, "-2a-3b", "d"]]

answer = []
while True:
    ask = input("Enter which matrix you want to multiply (a, b, c, d, or x to exit): ")
    match ask:
        case "a":
            for i in range(3):
                firstmul = symbolicPolynomialMultiplication(v[0], a[i])
                secondmul = symbolicPolynomialMultiplication(v[1], a[i + 3])
                thirdmul = symbolicPolynomialMultiplication(v[2], a[i + 6])
                answer.append(addSymbolicPolynomials(addSymbolicPolynomials(firstmul, secondmul), thirdmul))
            v = answer
            answer = []
        case "b":
            for i in range(3):
                firstmul = symbolicPolynomialMultiplication(v[0], b[i])
                secondmul = symbolicPolynomialMultiplication(v[1], b[i + 3])
                thirdmul = symbolicPolynomialMultiplication(v[2], b[i + 6])
                answer.append(addSymbolicPolynomials(addSymbolicPolynomials(firstmul, secondmul), thirdmul))
            v = answer
            answer = []
        case "c":
            for i in range(3):
                firstmul = symbolicPolynomialMultiplication(v[0], c[i])
                secondmul = symbolicPolynomialMultiplication(v[1], c[i + 3])
                thirdmul = symbolicPolynomialMultiplication(v[2], c[i + 6])
                answer.append(addSymbolicPolynomials(addSymbolicPolynomials(firstmul, secondmul), thirdmul))
            v = answer
            answer = []
        case "d":
            for i in range(3):
                firstmul = symbolicPolynomialMultiplication(v[0], d[i])
                secondmul = symbolicPolynomialMultiplication(v[1], d[i + 3])
                thirdmul = symbolicPolynomialMultiplication(v[2], d[i + 6])
                answer.append(addSymbolicPolynomials(addSymbolicPolynomials(firstmul, secondmul), thirdmul))
            v = answer
            answer = []
        case "x":
            print(f"Final answer is {v}")
            print("Exit")
            break
        case _:
            print("Invalid input. Please enter a valid option (a, b, c, d, or x).")

    # Clean the polynomial vector by removing 0s between power and real coefficients

    for poly in v:
        print(clean_polynomial([poly]))
    



    