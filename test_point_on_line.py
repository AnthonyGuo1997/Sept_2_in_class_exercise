def test_point_on_line():
    from point_on_line import point_on_line
    y_coord = point_on_line(0,0,1,1,3)
    expected = 3
    assert answer == expected