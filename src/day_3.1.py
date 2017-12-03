#!/usr/bin/python3


def get_xy(address):
	ring = 0
	while (2*ring+1)**2 < address:
		ring += 1
	side_length = 2 * ring + 1

	if ring == 0:
		return 0, 0

	current_address = (2*ring-1)**2 + 1
	x = ring
	y = 0 if ring == 0 else -1 * (ring - 1)

	# go up
	up_space = side_length - 2
	if address - current_address <= up_space:
		y += address - current_address
		return x, y
	else:
		y += up_space
		current_address += up_space

	# go left
	left_space = side_length - 1
	if address - current_address <= left_space:
		x -= address - current_address
		return x, y
	else:
		x -= left_space
		current_address += left_space

	# go down
	down_space = side_length - 1
	if address - current_address <= down_space:
		y -= address - current_address
		return x, y
	else:
		y -= down_space
		current_address += down_space

	# go right
	x += address - current_address
	return x, y


x, y = get_xy(325489)
manhattan_distance = abs(x) + abs(y)
print(manhattan_distance)