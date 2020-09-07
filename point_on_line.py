def point_on_line(point_1, point_2, x3):
    slope = (point_1[1]-point_2[1])/(point_1[0]-point_2[0])
    intercept = point_1[1]-slope*point_1[0]
    y3 = x3*slope + intercept
    return y3