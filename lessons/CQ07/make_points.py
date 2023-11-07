"""Making points."""


from lessons.CQ07.point import Point

new_point: Point = Point(1.05, 2.05)
print(new_point.scale())


main_point: Point  = Point(9.2, 3.4)
print(main_point.scale_by())


next_point: Point = Point(3.5, 4.7)
print(next_point.scale())