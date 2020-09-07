def point_on_line(point_1, point_2, x3):
    slope = (point_1(2)-point_2(2))/(point_1(1)-point_2(1))
    intercept = point_1(2)-slope*point_1(1)
    y3 = x3*slope + intercept
    return y3