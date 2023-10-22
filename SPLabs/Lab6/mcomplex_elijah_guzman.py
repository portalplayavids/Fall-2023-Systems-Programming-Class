# Elijah Guzman - nze594 - 10/21/23
class MyComplex:
    """
    This class represents a complex number with real and imaginary parts.
    """
    def __init__(self, r: int, i: int):
        """
        Constructor for this complex object
        :param r: A int value representing the real part of this complex object
        :param i: A int value representing the imaginary part of this complex object
        :return: None
        """
        self.r = r
        self.i = i

    def __str__(self):
        """
        Defines the string representation of a complex object
        :return: A string representation of a complex object
        """
        return f"{self.r} + {self.i}i"

    def __add__(self, other) -> 'MyComplex':
        """
        Defines the behavior of the operator + with two complex objects
        according to the following math operation
            (a + bi) + (c + di) = (a + c) + (b + d)i
        :return: A new complex object as result from the operation above
        """
        a = self.r
        b = self.i
        c = other.r
        d = other.i

        result = MyComplex(a + c, b + d)
        return result

    def __sub__(self, other) -> 'MyComplex':
        """
        Defines the behavior of the operator - with two complex objects
        according to the following math operation
            (a + bi) - (c + di) = (a - c) + (b - d)i
        :return: A new complex object as result from the operation above
        """
        a = self.r
        b = self.i
        c = other.r
        d = other.i

        result = MyComplex(a - c, b - d)
        return result

    def __eq__(self, other) -> bool:
        """
        Defines the behavior of the operator == with two complex objects
        :return: A boolean value comparing the two complex objects
        """
        return self.r == other.r and self.i == other.i

    def __ne__(self, other) -> bool:
        """
        Defines the behavior of the operator != with two complex objects
        :return: A boolean value comparing the two complex objects
        """
        return self.r != other.r or self.i != other.i

    def __mul__(self, other) -> 'MyComplex':
        """
        Defines the behavior of the operator * with two complex objects
        according to the following math operation
            (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        :return: A new complex object as result from the operation above
        """
        a = self.r
        b = self.i
        c = other.r
        d = other.i

        result = MyComplex(a*c - b*d, a*d + b*c)
        return result

    def __truediv__(self, other) -> 'MyComplex':
        """
        Defines the behavior of the operator / with two complex objects
        according to the following math operation
            (a + bi) / (c + di) = ((ac + bd) + (bc - ad)i) / (c^2 + d^2)
        :return: A new complex object as result from the operation above
        """
        a = self.r
        b = self.i
        c = other.r
        d = other.i

        denominator = c**2 + d**2
        result = MyComplex((a*c + b*d)/denominator, (b*c - a*d)/denominator)
        return result

    def __lt__(self, other) -> bool:
        """
        Defines the behavior of the operator < with two complex objects
        according to the following logic operation
            distance of self < distance of other
        :return: A boolean value comparing the euclidean distance between
                 two complex objects
        """
        return (self.r**2 + self.i**2) < (other.r**2 + other.i**2)

    def __gt__(self, other) -> bool:
        """
        Defines the behavior of the operator > with two complex objects
        according to the following logic operation
            distance of self > distance of other
        :return: A boolean value comparing the euclidean distance between
                 two complex objects
        """
        return (self.r**2 + self.i**2) > (other.r**2 + other.i**2)

def test():
    """
    You can define any test case for complex objects
    """
    x = MyComplex(1, 2)
    y = MyComplex(2, 4)
    z = x + y
    print(z)
    z = x / y
    print(z)
    print(f"X complex is greater than Y complex: {x > y}")
    print(f"X complex is less than Y complex: {x < y}")


if __name__ == "__main__":
    test()
