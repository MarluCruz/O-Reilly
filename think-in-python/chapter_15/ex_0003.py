from ex_0001 import distance_between_points
from ex_0002 import rectangle
class Circle:
    """ Represents a circle
        attributes: center, radius"""
class point:
    '''Represents a point in 2-D space.'''

def point_in_circle(circle, point):
     if distance_between_points(circle.center, point) <= 75:
         return True
     else:
         return False
def rect_in_circle(circle, rect):
     rect.corner2 = point()
     rect.corner2.x = rect.corner.x + rect.width
     rect.corner2.y = rect.corner.y
     rect.corner3 = point()
     rect.corner3.x = rect.corner.x
     rect.corner3.y = rect.corner.y + rect.height
     rect.corner4 = point()
     rect.corner4.x = rect.corner.x + rect.width
     rect.corner4.y = rect.corner.y + rect.height
     if (distance_between_points(circle.center, rect.corner) <= 75) and (distance_between_points(circle.center, rect.corner2) <= 75) and (distance_between_points(circle.center, rect.corner3) <= 75) and (distance_between_points(circle.center, rect.corner4) <= 75):
         return True
     else:
         return False
def rect_circle_overlap(circle, rect):
     rect.corner2 = point()
     rect.corner2.x = rect.corner.x + rect.width
     rect.corner2.y = rect.corner.y
     rect.corner3 = point()
     rect.corner3.x = rect.corner.x
     rect.corner3.y = rect.corner.y + rect.height
     rect.corner4 = point()
     rect.corner4.x = rect.corner.x + rect.width
     rect.corner4.y = rect.corner.y + rect.height
     if (distance_between_points(circle.center, rect.corner) <= 75) or (distance_between_points(circle.center, rect.corner2) <= 75) or (distance_between_points(circle.center, rect.corner3) <= 75) or (distance_between_points(circle.center, rect.corner4) <= 75):
         return True
     else:
         return False
circle = Circle()
circle.center = point()
circle.center.x = 150.0
circle.center.y = 100.0
circle.radius = 75.0
pointrandom = point()
pointrandom.x = 99.0
pointrandom.y = 99.0
box = rectangle()
box.width = 40.0
box.height = 20.0
box.corner = point()
box.corner.x = 110.0
box.corner.y = 80.0
print(point_in_circle(circle, pointrandom))
if rect_in_circle(circle, box):
    print("O retângulo está totalmente dentro ou no limite do círculo")
else:
    print("O retangulo não está completamente no interior do círculo")
