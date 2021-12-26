with open('input.txt') as f:
    lines = [i.strip() for i in f.readlines()]

MAX_POSITION = 10
MAX_SCORE = 1000
NUM_ROLLS = 3
RESULT = None


def solution():

    global MAX_SCORE
    global NUM_ROLLS
    global RESULT

    dice_rolled = 0
    dice_value = 0

    players = [{'score': 0, 'position': int(line[-1])} for line in lines]

    while all(player['score'] <= MAX_SCORE for player in players):
        players, dice_value, dice_rolled = roll_dice(NUM_ROLLS, players, dice_value, dice_rolled)

    print(RESULT)


def roll_dice(times, players, dice_value, dice_rolled):

    global MAX_POSITION
    global RESULT

    game_over = False

    for (i, player) in enumerate(players):
        if game_over:
            break
        dice_rolls = []
        for _ in range(1, times+1):
            dice_roll = dice_value + 1 if dice_value < 100 else 1
            dice_value = dice_roll
            dice_rolls.append(dice_roll)
        dice_rolled += times
        move = sum(dice_rolls)
        curr_pos = players[i]['position']
        new_pos = (curr_pos + move) % MAX_POSITION
        if new_pos > MAX_POSITION:
            new_pos -= MAX_POSITION
        elif new_pos == 0:
            new_pos = MAX_POSITION
        players[i]['position'] = new_pos
        players[i]['score'] += new_pos
        if players[i]['score'] >= MAX_SCORE:
            RESULT = players[1-i]['score'] * dice_rolled
            game_over = True

    return players, dice_value, dice_rolled


solution()
