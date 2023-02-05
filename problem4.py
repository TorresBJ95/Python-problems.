"""
Given the radius R of a sphere, calculate and print its surface area and its volume.
"""
import math


def vol_sup_sphere(radio):
    sup = 4 * math.pi * radio ** 2
    vol = (4 * math.pi * radio ** 3) // 3

    return sup, vol


def main():
    radio = int(input("please write the radius of a sphere: "))
    superficie, volumen = vol_sup_sphere(radio)

    print("the surface of the sphere is: %.2f" % superficie)
    print("the volume of the sphere is: %.2f" % volumen)

main()
