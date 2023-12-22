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

def find_gear_neighbors(data: str, x_pos: int, y_pos: int) -> int:
    """
    This function will take in the x & y position of a gear and find all
    adjacent number neighbors to the gear. Returns ratio of gear.

    .245. In this example, the gear neighbors would be two. We keep track
    .*... of if the last element traversed was a number or not. if it was
    ..13. we have only found a single number, but if the last traversed
          element was not a number then we know we found a new number and
          need to increase the counter for number of neighbors.
    ....25
    234*..
    ......
    """
    adjacent_numbers = [] 
    data = data.splitlines()
    data_h = len(data)
    data_w = len(data[0])

    left_bound = max(0, x_pos - 1)
    right_bound = min(data_w - 1, x_pos + 1)
    upper_bound = max(0, y_pos - 1)
    lower_bound = min(data_h - 1, y_pos + 1)
    print(f'gear position: {x_pos}, {y_pos}')
    print(f'data size: {data_h}, {data_w}')
    print(f'bounds - left: {left_bound}, right: {right_bound}, up: {upper_bound}, down: {lower_bound}')

    # search to left of number
    if left_bound != x_pos:
        curr_number = ''
        search_point = data[y_pos][left_bound]
        if search_point.isdigit():
           curr_pos = left_bound
           while curr_pos >= 0 and search_point.isdigit():
               curr_number = search_point + curr_number
               curr_pos -= 1
               if curr_pos >= 0:
                   search_point = data[y_pos][curr_pos]
           adjacent_numbers.append(int(curr_number))
    # search to the right of number
    if right_bound != x_pos:
        curr_number = ''
        search_point = data[y_pos][right_bound]
        if search_point.isdigit():
           curr_pos = right_bound
           while curr_pos <= data_w - 1 and search_point.isdigit():
               curr_number += search_point
               curr_pos += 1
               if curr_pos <= data_w - 1:
                   search_point = data[y_pos][curr_pos]
           adjacent_numbers.append(int(curr_number))

    # search above number
    if upper_bound != y_pos:
        curr_number = ''
        curr_pos = left_bound
        #for i in range(left_bound, right_bound + 1):
        while curr_pos <= right_bound:
            search_point = data[upper_bound][curr_pos]
            print(f'upper search value: {search_point}')
            if search_point.isdigit():
                left_point = data[upper_bound][max(0, curr_pos - 1)]
                right_point = data[upper_bound][min(data_w - 1, curr_pos + 1)]
                
                if right_point.isdigit:
                    while curr_pos <= data_w - 1 and search_point.isdigit():
                        curr_number += search_point
                        curr_pos += 1
                        if curr_pos <= data_w - 1:
                            search_point = data[upper_bound][curr_pos]
                if left_point.isdigit:
                    while curr_pos <= data_w - 1 and search_point.isdigit():
                        curr_number += search_point
                        curr_pos += 1
                        if curr_pos <= data_w - 1:
                            search_point = data[upper_bound][curr_pos]
                else:
                    pass
                adjacent_numbers.append(int(curr_number))
                curr_pos += 1


    # search below number
    if lower_bound != y_pos:
        for i in range(left_bound, right_bound + 1):
            search_point = data[lower_bound][i]
            if not search_point.isdigit() and search_point != '.':
                return True


    if len(adjacent_numbers) == 2:
        total = 1
        for num in adjacent_numbers:
            total *= num 
        return total
    else:
        return 0
#.10.25
#...*..
#......
test2 = """.10.25
...*..
......"""
data = read_data('/home/chandler/Documents/adventofcode/2023/day3/data.txt')
#print(sum_part_numbers(data))
print(find_gear_neighbors(test2, 3, 1))
