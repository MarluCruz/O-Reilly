class Point:
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Point):
            return self.__add_Point(other)
        else:
            return self.__new_point(other)
        
    def __add_Point(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __new_point(self, other):
        return Point(self.x + other[0], self.y + other[1])
    
    def print_point(self):
        print('(%g, %g)' % (self.x, self.y))
    
if __name__ == '__main__':
    
    pointA = Point (1, 2)
    pointB = Point (2, 3)
    pointC = pointA + pointB
    pointD = pointC + (2, 3)
    pointA.print_point()
    pointB.print_point()
    pointC.print_point()
    pointD.print_point()