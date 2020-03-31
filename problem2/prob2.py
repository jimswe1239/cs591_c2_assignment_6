import math

def p2(choice, length, breadth):
    """
    Assume user will put in correct character wanted everytime
    """
    shape = None
    if choice == "C":
        shape = "Circle"
    elif choice == "R":
        shape = "Rectangle"
    elif choice == "S":
        shape = "Square"

    area = None
    perimeter = None

    if choice == "C":
        area = math.pi * math.pow(length, 2)
        perimeter = math.pi * length * 2
    elif choice == "R":
        area = length * breadth
        perimeter = 2 * length + 2 * breadth
    elif choice == "S":
        area = length * length
        perimeter = length * 4

    return "Area: " + str(area) + " units and Perimeter: " + str(perimeter) + " units";
