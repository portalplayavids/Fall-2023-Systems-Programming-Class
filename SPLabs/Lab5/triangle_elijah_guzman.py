#Elijah Guzman - nze594 - 10/06/2023
# Design a python3 class that models an isosceles triangle and is updateable without stopping the process. 
# The API should be implemented using the following attributes and methods:
# Attributes:
# Base - Only modifiable by _init_,set_base(int or float)
# Height - Only modifiable by _init_,set_height(int or float)
# Side - The length of each lateral side of the triangle.(float)
# Area - The area of the triangle.(float)
# Alpha - Angle between each side and the base(degrees in float)
# Beta - Angle between the two sides of the triangle(degrees in float)
# Methods:
# __init__ - Takes two parameters, width and height. To build a new triangle. This method automatically updates all the triangle's data attributes.
# set_base - Change the current length value. New length must be greater than 0. This method automatically updates all the triangle's data attributes.
# set_height - Change the current height value. New height must be greater than 0. This method automatically updates all the triangle's data attributes.
# calc_side - Compute and return the current value of each of the two lateral sides of the triangle (only return one value)
# calc_perimeter - Compute and return the current value of the perimeter of the triangle
# calc_area - Compute and return the current value of the area of the triangle
# calc_alpha - Compute and return the current value of the angle of Alpha
# calc_beta - Compute and return the current value of the angle of Beta

import math

# math.sqrt(): returns the square root of a number
# math.atan(): returns the arc tangent of a number in radians
# math.degrees(): converts angle x from radians to degrees
# y = x ** 2: returns the square of x

class Triangle:
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height
        self.side = self.calc_side()
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()
        self.alpha = self.calc_alpha()
        self.beta = self.calc_beta()

    def set_base(self, base: float) -> None:
        self.base = base
        self.side = self.calc_side()
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()
        self.alpha = self.calc_alpha()
        self.beta = self.calc_beta()

    def set_height(self, height: float) -> None:
        self.height = height
        self.side = self.calc_side()
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()
        self.alpha = self.calc_alpha()
        self.beta = self.calc_beta()

    def calc_side(self) -> float:
        return math.sqrt((self.base / 2) ** 2 + self.height ** 2)

    def calc_perimeter(self) -> float:
        return 2 * self.side + self.base

    def calc_area(self) -> float:
        return (self.base * self.height) / 2

    def calc_alpha(self) -> float:
        return math.degrees(math.atan(self.height / (self.base / 2)))

    def calc_beta(self) -> float:
        return 180 - (2 * self.calc_alpha())
    


#print function for testing:
def print_all(self) -> None:
    print(f"------------------------------")
    print(f"base : {self.base}")
    print(f"height : {self.height}")
    print(f"side : {self.side}")
    print(f"perimeter: {self.perimeter}")
    print(f"area : {self.area}")
    print(f"alpha : {self.alpha}")
    print(f"beta : {self.beta}")
    print(f"------------------------------")

#User input for testing:
def main():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    triangle = Triangle(base, height)
    print_all(triangle)
    while True:
        print("1. Update base")
        print("2. Update height")
        print("3. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            base = float(input("Enter base: "))
            triangle.set_base(base)
            print_all(triangle)
        elif choice == 2:
            height = float(input("Enter height: "))
            triangle.set_height(height)
            print_all(triangle)
        elif choice == 3:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()