import math

def distance_between_points(point1, point2):
    catetoX = point1.x - point2.x
    catetoY = point1.y - point2.y
    distance = math.sqrt(catetoX**2 + catetoY**2)
    return distance
class point:
    '''Represents a point in 2-D space.'''
if __name__ == '__main__':
    point1 = point()
    point2 = point()
    point1.x = 1.0
    point1.y = 1.0
    point2.x = 4.0
    point2.y = 4.0
    print(distance_between_points(point1, point2))



