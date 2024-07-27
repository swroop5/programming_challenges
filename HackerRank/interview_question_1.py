
import math

def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    # Write your code here
    ab = calculate_distance(x1, y1, x2, y2)
    bc = calculate_distance(x2, y2, x3, y3)
    ac = calculate_distance(x1, y1, x3, y3)

    if ab + bc > ac and bc + ac > ab and ab + ac > ac:
        p_point = is_point_in_triangle(x1, y1, x2, y2, x3, y3, xp, yp)
        q_point = is_point_in_triangle(x1, y1, x2, y2, x3, y3, xq, yq)
        if p_point and q_point:
            return 3
        elif p_point and not q_point:
            return 1
        elif not p_point and q_point:
            return 2
        else:
            return 4
    else:
        return 0


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

def is_point_in_triangle(x1, y1, x2, y2, x3, y3, x, y):
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)
    
    return A == A1 + A2 + A3

print(pointsBelong(2,2,7,2,5,4,4,3,7,4))
print(pointsBelong(0,0,2,0,4,0,2,0,4,0))
print(pointsBelong(3,1,7,1,5,5,1,1,4,3))
print(pointsBelong(3,1,7,1,5,5,5,2,6,3))
print(pointsBelong(3,1,7,1,5,5,1,1,2,2))
