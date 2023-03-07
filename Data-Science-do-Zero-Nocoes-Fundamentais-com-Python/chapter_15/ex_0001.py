import math

def distance_between_point(point1, point2):
    if point1.x > point2.x:
        catetoX = point1.x - point2.x
    elif point1.x < point2.x:
        catetoX = point2.x - point1.x
    elif point1.x == point2.x:
        catetoX = 0
    
    if point1.y > point2.y:
        catetoY = point1.y - point2.y
    elif point1.y < point2.y:
        catetoY = point2.y - point1.y
    elif point1.y == point2.y:
        catetoY = 0
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
    print(distance_between_point(point1, point2))



