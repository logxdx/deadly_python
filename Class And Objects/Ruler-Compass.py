import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    
    def __str__(self):
        return f"<{self.x},{self.y}>"

class Line():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __getslope__(self):
        return (self.b.y - self.a.y) / (self.b.x - self.a.x)
    
    def __getintercept__(self,point):
        intercept = (point.y - Line.__getslope__(self)*point.x) 
        if intercept>0:
            return f'+ {intercept}'
        else:
            return intercept
        
    def __str__(self,point):
        return f"({self.a},{self.b}): y={Line.__getslope__(self)}*x {Line.__getintercept__(self,point)}"

    def draw_perpendicular(self, point):

        # Find the slope of the line
        slope = Line.__getslope__(self)

        # Find the slope of the perpendicular line
        perpendicular_slope = -1 / slope

        # Find the y-intercept of the perpendicular line
        y_intercept = point.y - perpendicular_slope * point.x

        # Create a new line perpendicular to the given line and passing through the given point
        perpendicular_line = f"point: {point} | slope: {perpendicular_slope}"
        perpendicular_line += f" | Equation: y={perpendicular_slope}*x + {y_intercept}"

        return perpendicular_line

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def square_root(self, num):
        return math.sqrt(num)

    def gcd(self, num1, num2):
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        return num1

def intersect_two_lines(line1, line2):
    # Implementation of intersectTwoLines(Line a, Line b)
    # Calculate the intersection point of two lines using the given line equations
    x = ((line1.b.x - line1.a.x) * (line2.b.x - line2.a.x) * (line2.a.y - line1.a.y) +
         line1.a.x * (line1.b.y - line1.a.y) * (line2.b.x - line2.a.x) -
         line2.a.x * (line2.b.y - line2.a.y) * (line1.b.x - line1.a.x)) / \
        ((line1.b.y - line1.a.y) * (line2.b.x - line2.a.x) - (line1.b.x - line1.a.x) * (line2.b.y - line2.a.y))

    y = line1.a.y + (line1.b.y - line1.a.y) * (x - line1.a.x) / (line1.b.x - line1.a.x)

    return Point(x, y)

def intersect_two_circles(circle1, circle2):
    # Implementation of intersectTwoCircles(Circle c1, Circle c2)
    # Calculate the intersection points of two circles using the given circle equations

    # Calculate the distance between the centers of the circles
    distance = math.sqrt((circle2.center.x - circle1.center.x) ** 2 + (circle2.center.y - circle1.center.y) ** 2)

    # Check if the circles are identical or one circle is contained within the other
    if distance == 0 and circle1.radius == circle2.radius:
        raise Exception("Infinite number of intersection points")

    if distance > circle1.radius + circle2.radius or distance < abs(circle1.radius - circle2.radius):
        raise Exception("No intersection points")

    # Calculate the intersection points using the circle equations
    dx = circle2.center.x - circle1.center.x
    dy = circle2.center.y - circle1.center.y
    d = math.sqrt(dx * dx + dy * dy)

    a = (circle1.radius * circle1.radius - circle2.radius * circle2.radius + d * d) / (2 * d)
    h = math.sqrt(circle1.radius * circle1.radius - a * a)

    x2 = circle1.center.x + (dx * a / d)
    y2 = circle1.center.y + (dy * a / d)

    x3 = x2 + (h * dy / d)
    y3 = y2 - (h * dx / d)

    x4 = x2 - (h * dy / d)
    y4 = y2 + (h * dx / d)

    # Sort the intersection points lexicographically
    if (x3, y3) > (x4, y4):
        return Point(x4, y4), Point(x3, y3)
    else:
        return Point(x3, y3), Point(x4, y4)

def intersect_line_circle(line, circle):
    # Implementation of intersectLineCircle(Line line, Circle circle)
    # Calculate the intersection points of a line and a circle

    # Find the slope and y-intercept of the line
    line_slope = (line.b.y - line.a.y) / (line.b.x - line.a.x)
    line_y_intercept = line.a.y - line_slope * line.a.x

    # Find the coefficients of the quadratic equation
    a = 1 + line_slope * line_slope
    b = 2 * (line_slope * line_y_intercept - line_slope * circle.center.y - circle.center.x)
    c = (circle.center.y ** 2) - (circle.radius ** 2) + (circle.center.x ** 2) - (2 * line_y_intercept * circle.center.y) + (line_y_intercept ** 2)

    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    # Check if there are any intersection points
    if discriminant < 0:
        raise Exception("No intersection points")

    # Calculate the x-coordinates of the intersection points
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)

    # Calculate the y-coordinates of the intersection points using the line equation
    y1 = line_slope * x1 + line_y_intercept
    y2 = line_slope * x2 + line_y_intercept

    # Sort the intersection points lexicographically
    if (x1, y1) > (x2, y2):
        return Point(x2, y2), Point(x1, y1)
    else:
        return Point(x1, y1), Point(x2, y2)

def get_length_with_compass(point1, point2):
    # Implementation of getLengthWithCompass(Point a, Point b)
    # Calculate the length between two points using the distance formula
    # distance = math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)
    distance = Point.distance(point1,point2)
    return distance

# Example usage
point_a = Point(1, 1)
point_b = Point(4, 4)
point_c = Point(2,3)

print(point_a)
print(point_b)

line_ab = Line(point_a, point_b)
print(line_ab.__str__(point_c))
perpendicular_line = line_ab.draw_perpendicular(point_c)

circle1 = Circle(Point(2, 2), 2)
circle2 = Circle(Point(), math.sqrt(2))

intersection_points = intersect_two_circles(circle1, circle2)

distance = get_length_with_compass(point_a, point_b)

print("Perpendicular Line:", perpendicular_line)
print("Intersection Points:", intersection_points[0].x, intersection_points[0].y, intersection_points[1].x, intersection_points[1].y)
print("Distance:", distance)
