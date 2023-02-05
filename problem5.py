"""
Read the base and the height of a rectangle, calculate the perimeter and the surface.
"""
def rectangle(base,height):
    sup = base*height
    perimeter = 2*base + 2*height

    return sup, perimeter

def main():
    base = int(input("please write the base of a rectangle: "))
    height = int(input("please write the height of a rectangle: "))
    sup, perimeter = rectangle(base,height)

    print("the perimeter is : %.1f" % perimeter)
    print("the surface is : %.1f" % sup)
main()