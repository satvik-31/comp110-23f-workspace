"""Running the River simulaton."""


__author__ = "730517765"


from exercises.ex08.river import River

my_river: River = River(10, 2)

my_river.view_river()

new_river = River(2, 5)
new_river.one_river_week