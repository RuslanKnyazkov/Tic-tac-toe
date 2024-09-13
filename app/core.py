WIN_WORLD = ['horizontally', 'vertically', 'diagonally']

matrix = [['*' for _ in range(3)] for j in range(3)]


def check_position(*args, character: str) -> bool:
    """
    Checks the entered column and row fields.

    :param args: Max length 2 items (column , row)
    :param character: X or O characters player
    :return: True if all items correct
    """
    if len(args) > 2:
        print(f'You entered the wrong number of parameters got {len(args)} , need 2')

    try:
        for i in args:
            if 1 <= i <= 4:
                ...
            else:
                print(f'Insert character not valid got {i}, need numbers range 1 - 3')

    except ValueError as e:
        print(f'{e} Values {args} outer range')

    column, row = args

    if matrix[column - 1][row - 1] == '*':

        matrix[column - 1][row - 1] = character
        return True
    else:
        print('This field not empty')
    return False


def find_winner_combine(array: list[list[str]], player: str) -> str:
    """
    Search win combine in game.

    :param array: Iterable object matrix 3x3.
    :param player: The symbol to insert into the table.
    :return: String who won in this game or draw.
    """

    if '*' not in ''.join(i for _ in matrix for i in _):
        return 'Draw'

    for i in range(len(array)):
        if '*' != array[i][i] == array[i][i - 2] == array[i][i - 1]:
            return f'Player {player} won horizontally'
        elif '*' != array[i - 2][i] == array[i - 1][i] == array[i][i]:
            return f'Player {player} won vertically'
        elif '*' != array[-2][-2] == array[-1][-1] == array[0][0]:
            return f'Player {player} won diagonally'
        elif '*' != array[0][2] == array[1][1] == array[2][0]:
            return f'Player {player} won diagonally'
        else:
            return 'The game continue'
