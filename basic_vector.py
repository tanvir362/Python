import math

y_axis = (0, 1)
def val(V):
    return math.sqrt(sum(i**2 for i in V))

def dot_prod(V1, V2):
    return sum(a*b for a, b in zip(V1, V2))

def angle(A, B):
    a = val(A)
    b = val(B)

    ab = dot_prod(A, B)

    ang = math.degrees(math.acos(ab / (a * b)))

    return round(ang)

def angle2(A, B):
    (x1, y1), (x2, y2) = A, B
    dot = x1*x2 + y1*y2
    det = x1*y2 - y1*x2

    ag = math.atan2(det, dot)

    return round(math.degrees(ag))



