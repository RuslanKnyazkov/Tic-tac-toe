from time import sleep
from core import (check_position, matrix,
                  find_winner_combine, WIN_WORLD)

welcome = 'Hello, let`s play!!!\n\n'
running = True

for _ in welcome:
    sleep(0.1)
    print(_, end="")

print(*matrix, sep='\n')

player = input("\nInsert hwo be first start the game X or O\n").lower()

while True:
    if player != 'x' or 'o':
        print(f'An invalid character has been entered got {player}, must x or o')
        player = input("\nInsert hwo be first start the game X or O\n").lower()
    else:
        break


def main():
    """
    Function start the game
    """
    global player, running
    while running:

        if player == 'x':
            column = int(input(f"Player {player} insert column: \n"))
            row = int(input(f"Player {player} insert row: \n"))
            if check_position(column, row, character='X'):
                player = 'o'

        elif player == 'o':
            column = int(input(f"Player {player} insert column: \n"))
            row = int(input(f"Player {player} insert row: \n"))
            if check_position(column, row, character='O'):
                player = 'x'

        print(*matrix, sep='\n')

        test = find_winner_combine(matrix, player)
        for world in WIN_WORLD:
            if world in test:
                print(test)
                running = False
            else:
                print(test)


if __name__ == '__main__':
    main()
