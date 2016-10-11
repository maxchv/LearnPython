"""
Homework 18

Subject: Static methods, Class methods, Iterators
"""

class MathCls:
    """
    Задание 1

    >>> MathCls.add(2, 3)
    5
    >>> MathCls.sub(5, 2)
    3
    >>> MathCls.mult(5, 2)
    10
    >>> MathCls.div(10, 2)
    5.0
    """


# Write a simple Vehicle class that has fields for (at least) current speed, current direction in degrees, and owner name.
# class Vehicle {
#   int currentSpeed;
#   int currentDirection;
#   String owner;
# }
# Add a static field to your Vehicle class for the highest Vehicle Identification Number issued, and a non-static field that holds each vehicle's ID number.
# class Vehicle {
#   int currentSpeed;
#   int currentDirection;
#   String owner;
#   static int highestVIN;
#   int VIN;
# }
# Write a main method for your Vehicle class that creates a few vehicles and prints out their field values. Note that you can also write a separate tester program as well.
# class Vehicle {
#
#   int currentSpeed;
#   int currentDirection;
#   String owner;
#   static int highestVIN;
#   int VIN;
#
#   public static void main(String[] args) {
#
#     Vehicle a = new Vehicle();
#     a.VIN = highestVIN++;
#     a.owner = "Larry Bird";
#
#     Vehicle b = new Vehicle();
#     b.VIN = highestVIN++;
#     b.owner = "Mark Jackson";
#
#     System.out.println("VIN: " + a.VIN + " belongs to " + a.owner);
#
#     System.out.println("VIN: " + b.VIN + " belongs to " + b.owner);
#
#     // Note that both cars are stopped, and facing East.
#
#   }
# }

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)