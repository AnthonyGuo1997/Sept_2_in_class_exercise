def test_point_on_line():
    from point_on_line import point_on_line
    y_coord = point_on_line((0,0),(1,1),3)
    expected = 3
    assert y_coord == expected

def test_get_slope():
    from point_on_line import get_slope
    calc_slope = get_slope((1,1), (2,3))
    expected = 2
    assert calc_slope = expected
