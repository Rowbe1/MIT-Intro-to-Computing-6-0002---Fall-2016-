import math
import random

import ps3_visualize
import pylab

width = 5
height = 8
dirt_amount = 2

room = {}
for i in range(width):
    for j in range(height):
        print(i,j)
        room[(i,j)] = dirt_amount

print(room)
print(width*height)
print(len(room))

capacity = 0.7
pos_x = 4.3
pos_y = 7.4
tile_x = math.floor(pos_x)
print("tile x",tile_x)
tile_y = math.floor(pos_y)
print("tile y",tile_y)
dirt = room[(tile_x,tile_y)]

print(dirt)

cleaned = dirt - capacity

room[(tile_x,tile_y)] = cleaned

print(room[(tile_x,tile_y)])