testInput = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def read_data(file_path: str):
    with open(file_path) as file:
        data = file.read()
    return data

def find_adjacent_parts(data: str, y_pos: int, x_range: list, curr_number: str) -> bool:
    """
    take in a y position and the range of x_values a given number
    overlaps with. From there, search the perimeter around the number and
    try to find any symbols that are not periods. if a symbol is found,
    return True; return False if no symbols are adjacent to a number.

    Example: 
        y = 4
        x_range = [3, 7]

        - determine if number is against any boundary.
        - search y = 3 between x = [2,8]
        - search y = 5 between x = [2,8]
        - search y = 4 at x = 2 and y = 4 at x = 8
    """

    # split data into individual lines to make traversing easier
    data_h = len(data)
    data_w = len(data[0])

    left_bound = max(0, x_range[0] - 1)
    right_bound = min(data_w - 1, x_range[1] + 1)
    upper_bound = max(0, y_pos - 1)
    lower_bound = min(data_h - 1, y_pos + 1)
    print(f'evaluating number: {curr_number}') 
    print(f'number position: {x_range}, {y_pos}')
    print(f'data size: {data_h}, {data_w}')
    print(f'bounds - left: {left_bound}, right: {right_bound}, up: {upper_bound}, down: {lower_bound}')

    # search to left of number
    if left_bound != x_range[0]:
        search_point = data[y_pos][left_bound]
        if not search_point.isdigit() and search_point != '.':
            return True
    # search to the right of number
    if right_bound != x_range[1]:
        search_point = data[y_pos][right_bound]
        if not search_point.isdigit() and search_point != '.':
            return True
    # search above number
    if upper_bound != y_pos:
        for i in range(left_bound, right_bound + 1):
            search_point = data[upper_bound][i]
            if not search_point.isdigit() and search_point != '.':
                return True
    # search below number
    if lower_bound != y_pos:
        for i in range(left_bound, right_bound + 1):
            search_point = data[lower_bound][i]
            if not search_point.isdigit() and search_point != '.':
                return True

    return False

def sum_part_numbers(data: str):
    data = data.splitlines()
    data_h = len(data)
    data_w = len(data[0])

    total = 0
    for height in range(data_h):
        element = 0
        while element < data_w:
            # if not digit then continue
            if not data[height][element].isdigit():
                element += 1
            else:
                # determine how many elements the number takes up
                number = data[height][element]
                last_elm = element
                while last_elm + 1 < data_w and \
                        data[height][last_elm + 1].isdigit():
                      last_elm += 1
                      number += data[height][last_elm]
                if find_adjacent_parts(data, height, [element, last_elm], number):
                      total += int(number)

                element = last_elm + 1
    return total
data = read_data('/home/chandler/Documents/adventofcode/2023/day3/data.txt')

print(sum_part_numbers(data))
