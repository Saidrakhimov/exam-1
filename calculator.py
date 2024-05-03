class calculator():
    def __str__(self):
        pass

    def plus(self, number1, number2):
        return number1 + number2

    def minus(self, number1, number2):
        return number1 - number2

    def multiply(self, number1, number2):
        return number1 * number2

    def divide(self, number1, number2):
        if number2 != 0:
            return number1 / number2


answers = calculator()
amal = input("qanday amal bajarasiz,+,-,*,/: ")
num1 = int(input("num1: "))
num2 = int(input("num2: "))
if amal == "+":
    print(answers.plus(num1, num2))
if amal == "-":
    print(answers.minus(num1, num2))
if amal == "*":
    print(answers.multiply(num1, num2))
if amal == "/":
    print(answers.divide(num1, num2))
