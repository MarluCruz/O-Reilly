from ex_0001 import distance_between_point
from ex_0002 import rectangle
class Circle:
    """ Represents a circle
        attributes: center, radius"""
class point:
    '''Represents a point in 2-D space.'''

def point_in_circle(circle, point):
     if distance_between_point(circle.center, point) <= 75:
         return True
     else:
         return False
def rect_in_circle(circle, point):
     if distance_between_point(circle.center, point) <= 75:
         return True
     else:
         return False

circle = Circle()
circle.center = point()
circle.center.x = 150.0
circle.center.y = 100.0
circle.radius = 75.0
pointrandom = point()
pointrandom.x = 0
pointrandom.y = 0
print(point_in_circle(circle, pointrandom))
