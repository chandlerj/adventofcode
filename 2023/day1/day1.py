
"""
- keep list of nums(str, int) pairs
- if a given nums[i] is in the array, find the position where that word starts
    - store value and position where number starts as another tuple (int, int).
- if isdigit, store location of digit and value in array
"""
testInput2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

numbers = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        }

conf_vals = []

def read_data(file_path: str):
    with open(file_path) as file:
        data = file.read()
    return data


def find_calibration_keys(file: str):
    # Stores tuples (index, item @ index)
    digits=[]
    for line in file.splitlines():
        for item in numbers: # find all numbers that are spelled out
            if item in line:
                occurances = [i for i in range(len(line)) if line.startswith(item, i)]
                print(occurances)
                for instance in occurances:
                    digits.append((instance, numbers[item]))
        for i, character in enumerate(line): # find all numeric characters
            if character.isdigit():
                digits.append((i, int(character)))

        # sort list by indicies in tuple (digits[n][0])
        digits.sort(key=lambda a: a[0])
        print(digits) 
        # grab number at first and last index of digits
        # list and append to conf_vals list.
        new_val = (digits[0][1] * 10) + digits[-1][1]
        print(new_val)
        conf_vals.append(new_val)
        # clear digits at the end of every line
        digits.clear()

data = read_data('/home/chandler/Documents/adventofcode/2023/data.txt')
find_calibration_keys(data)
print(sum(conf_vals))


