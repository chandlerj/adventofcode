

testInput = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def read_data(file_path: str):
    with open(file_path) as file:
        data = file.read()
    return data

def sum_valid_games(data: str, red_tol: int, grn_tol: int, blu_tol:int) -> int:
    total = 0
    for line in data.splitlines():
       game_split = line.split(':')
       curr_game = game_split[0].split(' ')[1] 
#       print(curr_game)
       if determine_valid_game(line, red_tol, grn_tol, blu_tol):
            total += int(curr_game)
    return total


def determine_valid_game(line: str, red_tol: int, grn_tol: int, blu_tol: int) -> bool:
    """
    Read in data one line at a time. One line corresponds to one
    game being played. For every game, split the input by semicolon to
    get each round that occurred in a game. From there, subtract the
    amount of gems shown from the amount of gems allowed. if the 
    jewel counts are not zero by the end of the game, then return
    true; else, more gems were presented than the tolerated amount.
    """

    game_split = line.split(':')
    round_split = game_split[1].split(';')
    curr_game = game_split[0].split(' ')[1] 
    for round in round_split:
        red = red_tol
        blue = blu_tol
        green = grn_tol
        gem_split = round.strip().replace(',','').split(' ')
#        print(gem_split)
        for i in range(0, len(gem_split), 2):
            if gem_split[i + 1] == 'blue':
                blue -= int(gem_split[i])
            if gem_split[i + 1] == 'green':
                green -= int(gem_split[i])
            if gem_split[i + 1] == 'red':
                red -= int(gem_split[i])
        if red < 0 or blue < 0 or green < 0:
#            print(f"impossible game: {curr_game}")
            return False
    return True

def sum_gem_power(data: str):
    total = 0
    for line in data.splitlines():
        red_min = 1
        grn_min = 1
        blu_min = 1

        games = line.replace(',','').split(':')[1].split(';')
        for i in range(len(games)):
            games[i] = games[i].lstrip().split(' ')
        for play in games:
            for i in range(0, len(play), 2):
                if play[i + 1] == 'blue' and int(play[i]) > blu_min:
                    blu_min = int(play[i])
                if play[i + 1] == 'green' and int(play[i]) > grn_min:
                    grn_min = int(play[i])
                if play[i + 1] == 'red' and int(play[i]) > red_min:
                    red_min = int(play[i])
        game_power = red_min * grn_min * blu_min
        total += game_power
#        print(f"power: {game_power}; {games}")
    return total




data = read_data('/home/chandler/Documents/adventofcode/2023/day2/data.txt')
print(f'valid game sum: {sum_valid_games(data, 12, 13, 14)}')
print(f'gem power sum:  {sum_gem_power(data)}')
