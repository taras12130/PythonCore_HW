# Find The Distance Between Two Points

def distance(x1, y1, x2, y2):
    res = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return round(res, 2)
print(distance(1, 1, 0, 0))