def point_on_line(point_1, point_2, x3):
    slope = get_slope(point_1, point_2)
    intercept = get_intercept(point_1, point_2)
    y3 = x3*slope + intercept
    return y3

def get_slope(point_1, point_2):
    slope = (point_1[1]-point_2[1])/(point_1[0]-point_2[0])
    return slope

def get_intercept(point_1, point_2):
    slope = get_slope(point_1, point_2)
    intercept = point_1[1]-slope*point_1[0]
    return intercept