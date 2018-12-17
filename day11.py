import math


def one_cell_power_level(x, y, serial):
    rack_id = x + 10
    power_level = (rack_id * y + serial) * rack_id

    hundreds_digit = int(str(power_level).rjust(3, '0')[-3])
    return hundreds_digit - 5


def compute_power_level(x, y, size, serial):

    cell_power_level = 0
    for i in range(x, x + size):
        for k in range(y, y + size):
            cell_power_level = cell_power_level + one_cell_power_level(
                i, k, serial)

    return cell_power_level


serial = 5719
max_fuel_cell = -math.inf
max_fuel_cell_coordinate = (1, 1)
size = 3

for x in range(1, 300 + 2 - size):
    for y in range(1, 300 + 2 - size):
        cell_power_level = compute_power_level(x, y, size, serial)
        if cell_power_level > max_fuel_cell:
            max_fuel_cell = cell_power_level
            max_fuel_cell_coordinate = x, y

print(f'The max power level is {max_fuel_cell} at {max_fuel_cell_coordinate}')


def power_knowing_previous_size(x, y, size, level_at_previous_size, serial):
    cell_power_level = level_at_previous_size
    for dy in range(y, y + size):
        cell_power_level = cell_power_level + one_cell_power_level(
            x + size - 1, dy, serial)
    for dx in range(x, x + size - 1):
        cell_power_level = cell_power_level + one_cell_power_level(
            dx, y + size - 1, serial)

    return cell_power_level


max_fuel_cell = -math.inf
max_fuel_cell_coordinate = (1, 1, 1)

for x in range(1, 300):
    print(f'{max_fuel_cell_coordinate}')
    for y in range(1, 300):
        power_level_at_previous_size = 0
        for size in range(1, 301):
            if (x + size <= 301 and y + size <= 301):
                cell_power_level = power_knowing_previous_size(
                    x, y, size, power_level_at_previous_size, serial)
                power_level_at_previous_size = cell_power_level
                if cell_power_level > max_fuel_cell:
                    max_fuel_cell = cell_power_level
                    max_fuel_cell_coordinate = x, y, size

print(f'The max power level is {max_fuel_cell} at {max_fuel_cell_coordinate}')
