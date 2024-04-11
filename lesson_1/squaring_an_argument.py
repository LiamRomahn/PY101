def multiply(num1, num2):
    return num1 * num2
def square(number):
    return multiply(number, number)
def exponent(number, power):
    product = 1
    for _ in range(power):
        product *= multiply(number, 1)
    return product
print(exponent(5, 10))
