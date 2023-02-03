"""
Ask the user to enter two numbers by keyboard and print
- The sum of both
- Subtraction (the first minus the second)
- The multiplication
- Integer division (assume that the second number is not zero).
- Division with decimals.
"""



def awnser(number_1,number_2):
    suma = number_1 + number_2
    resta = number_1 - number_2
    multi = number_1 * number_2
    div = number_1 // number_2
    div_decimal = number_1 / number_2

    return suma, resta, multi, div, div_decimal

def main():
    number_1 = int(input("please write a number: "))
    number_2 = int(input("please write other number: "))
    x,y,z,k,e = awnser(number_1,number_2)

    print("la suma de ambos numeros es: {}".format(x))
    print("la resta de ambos numeros es: {}".format(y))
    print("la multiplicacion de ambos numeros es: {}".format(z))
    print("la division de ambos numeros es: {}".format(k))
    print("la divison con decimal de ambos numeros es: %.3f" % e)

main()