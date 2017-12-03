#!/usr/bin/python3

import numpy as np
import sys


GRID_SIZE = 13


def coord_generator():
	ring = 0
	x, y = 0, 0
	yield x, y

	while True:
		x += 1
		ring += 1
		side_length = 2 * ring + 1
		yield x, y

		for _ in range(side_length - 2): # go up
			y -= 1
			yield x, y
		for _ in range(side_length - 1): # go left
			x -= 1
			yield x, y
		for _ in range(side_length - 1): # go down
			y += 1
			yield x, y
		for _ in range(side_length - 1): # go right
			x += 1
			yield x, y


grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=np.int64)
center_x, center_y = GRID_SIZE // 2, GRID_SIZE // 2
grid[center_y, center_x] = 1


for x, y in coord_generator():
	x += center_x
	y += center_y

	if x == center_x and y == center_y:
		continue # Skip origin

	grid[y, x] = np.sum(grid[y-1:y+2, x-1:x+2])

	if grid[y, x] > 325489:
		print(grid[y, x])
		sys.exit()