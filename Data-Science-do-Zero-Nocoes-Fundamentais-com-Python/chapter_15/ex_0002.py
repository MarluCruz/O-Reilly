class point:
    '''Represents a point in 2-D space.'''
class rectangle:
    ''' Represents a rectangle
        attributes:width, height, corner
        '''
def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))
    
def move_rectangle(rectangle, dx, dy):
    rectangle.corner.x += dx
    rectangle.corner.y += dy
if __name__ == '__main__':
    box = rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = point()
    box.corner.x = 0.0
    box.corner.y = 0.0
    move_rectangle(box, 2.0, 2.0)
    print(box.corner.x)
    print(box.corner.y)

