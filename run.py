import random


def game_board(size, number_of_bombs):
    """
    creates the minesweeper board size and place mines at random
    neighbouring cells increase values to represent how many bombs nearby
    """
    board = [[0 for row in range(size)] for column in range(size)]

    for num in range(number_of_bombs):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        board[y][x] = '*'       # mine symbol

        if (x >= 1 and x <= size - 1) and (y >= 0 and y <= size - 1):
            if board[y][x - 1] != '*':
                board[y][x - 1] += 1        # center left

        if (x >= 0 and x <= size - 2) and (y >= 0 and y <= size - 1):
            if board[y][x + 1] != '*':
                board[y][x + 1] += 1        # center right

        if (x >= 1 and x <= size - 1) and (y >= 1 and y <= size - 1):
            if board[y - 1][x - 1] != '*':
                board[y - 1][x - 1] += 1        # top left

        if (x >= 0 and x <= size - 2) and (y >= 1 and y <= size - 1):
            if board[y - 1][x + 1] != '*':
                board[y - 1][x + 1] += 1        # top right

        if (x >= 1 and x <= size - 1) and (y >= 0 and y <= size - 2):
            if board[y + 1][x - 1] != '*':
                board[y + 1][x - 1] += 1        # bottom left

        if (x >= 0 and x <= size - 2) and (y >= 0 and y <= size - 2):
            if board[y + 1][x + 1] != '*':
                board[y + 1][x + 1] += 1        # bottom right

        if (x >= 0 and x <= size - 1) and (y >= 1 and y <= size - 1):
            if board[y - 1][x] != '*':
                board[y - 1][x] += 1        # top center

        if (x >= 0 and x <= size - 1) and (y >= 0 and y <= size - 2):
            if board[y + 1][x] != '*':
                board[y + 1][x] += 1        # bottom center

    return board


def player_board(size):
    """
    player board to display whilst playing the game hiding the mines
    """
    board = [['-' for row in range(size)] for column in range(size)]

    return board


def display_map(map):
    """
    tidies up the map displayed to the user
    """
    for row in map:
        print(" ".join(str(cell) for cell in row))
        print("")


def check_win(map):
    """
    check the map to either continue playing or if the player has won
    """
    for row in map:
        for cell in row:
            if cell == '-':
                return False
    return True


def continue_game(score):
    """
    user can choose to exit the program or start another game
    """
    print("Your Score:", score)
    to_continue = input("Do you want to try again? (y/n):\n")
    if to_continue.lower().strip() == 'n':
        print("Thanks for playing!")
        return False
    if to_continue.lower().strip() == 'y':
        print("Let's play again...")
    else:
        print("Please enter either y or n")
    return True


def welcome_message():
    """
    initial welcome message in the terminal
    """
    print("\n* Minesweeper *\n")
    print("The aim of the game is to dig up all cells")
    print("without hitting the mines,\nGOOD LUCK!\n ")


def mine_instructions():
    """
    user option to display the rules of minesweeper
    """
    instructions = input("Would you like to know the rules (y/n):\n")
    if instructions.lower().strip() == 'y':
        print("\n1.Aim of the game to dig all spaces without hitting a mine")
        print("2.If you hit a mine, you lose")
        print("3.If you uncover all locations without hitting a mine, you win")
    elif instructions.lower().strip() == 'n':
        print("\nLets being...")
    else:
        print("\nSorry, I dont understand, please enter y (yes) or n (no)\n")
        mine_instructions()


def play_game():
    """
    user to select the game difficulty and game logic
    """
    welcome_message()
    mine_instructions()

    status = True
    while status:

        difficulty = input("\nSelect your difficulty (easy, normal, hard):\n")
        if difficulty.lower().strip() == 'easy':
            size = 5
            number_of_bombs = 3
        elif difficulty.lower().strip() == 'normal':
            size = 6
            number_of_bombs = 8
        elif difficulty.lower().strip() == 'hard':
            size = 8
            number_of_bombs = 20
        else:
            print("\nPlease enter difficulty as either: easy, normal or hard")
            continue

        minesweeper_map = game_board(size, number_of_bombs)
        player_map = player_board(size)
        score = 0

        while True:
            if check_win(player_map) is False:
                print("\nEnter the location of your dig:")
                try:
                    x = int(input("\nColumn:\n")) - 1
                    y = int(input("Row:\n")) - 1
                except ValueError:
                    print("This is not a valid location, try again")

                if (x < 0 or y < 0 and x >= size or y >= size):
                    print("Invalid location, try again")
                    continue

                if (minesweeper_map[y][x] == '*'):
                    print("Game Over")
                    display_map(minesweeper_map)
                    status = continue_game(score)
                    break

                else:
                    player_map[y][x] = minesweeper_map[y][x]
                    display_map(player_map)
                    score += 1

            else:
                display_map(player_map)
                print("You Win!")
                status = continue_game(score)
                break


if __name__ == "__main__":
    """
    identifies this file as the main module and runs the game
    """
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nEnd of the game. Thanks for playing!")
