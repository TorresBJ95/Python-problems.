"""
Read two numbers A and B and exchange the value of their variables.
"""



def main():
    numer_1 = int(input("please write first number: "))
    number_2 = int(input("please write second number: "))
    number_3 = numer_1
    number_1 = number_2
    print("first value: {}, second value {}".format(number_1,number_3))

main()
