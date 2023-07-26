import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, value):
        if value < 0:
            self.__radius = 0
        else:
            self.__radius = value

    def get_perimeter(self):
        return 2* math.pi * self.__radius

    radius = property(get_radius, set_radius)    # property(fget, fset, fdel, doc) 
    #fget, fset, fdel = by default None
    # p = Point(2, 10) fget = p.x   fset : p.x = 10 fel: del p
    perimeter = property(get_perimeter) 

def main():
     c = Circle(10)
     c.radius = 30
     print(c.radius)
     print("perimeter: ", c.perimeter)


if __name__ == '__main__':
    main()