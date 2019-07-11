import random
import time

class Board:
    def __init__(self):
        self.column_one = random.sample(range(1,16), 5)
        self.column_two = random.sample(range(16,31), 5)
        self.column_three = random.sample(range(31,46), 5)
        self.column_three[2] = "X "
        self.column_four = random.sample(range(46,61), 5)
        self.column_five = random.sample(range(61,76), 5)

    def render_board(self):
        print(f"""
              ----------------
              |B |I |N |G |O |
              ----------------
              |{self.column_one[0] if isinstance(self.column_one[0], str) else self.column_one[0] if self.column_one[0] >= 10 else str(self.column_one[0]) + " "}|{self.column_two[0]}|{self.column_three[0]}|{self.column_four[0]}|{self.column_five[0]}| 
              ----------------
              |{self.column_one[1] if isinstance(self.column_one[1], str) else self.column_one[1] if self.column_one[1] >= 10 else str(self.column_one[1]) + " "}|{self.column_two[1]}|{self.column_three[1]}|{self.column_four[1]}|{self.column_five[1]}| 
              ----------------
              |{self.column_one[2] if isinstance(self.column_one[2], str) else self.column_one[2] if self.column_one[2] >= 10 else str(self.column_one[2]) + " "}|{self.column_two[2]}|{self.column_three[2]}|{self.column_four[2]}|{self.column_five[2]}| 
              ----------------
              |{self.column_one[3] if isinstance(self.column_one[3], str) else self.column_one[3] if self.column_one[3] >= 10 else str(self.column_one[3]) + " "}|{self.column_two[3]}|{self.column_three[3]}|{self.column_four[3]}|{self.column_five[3]}| 
              ----------------
              |{self.column_one[4] if isinstance(self.column_one[4], str) else self.column_one[4] if self.column_one[4] >= 10 else str(self.column_one[4]) + " "}|{self.column_two[4]}|{self.column_three[4]}|{self.column_four[4]}|{self.column_five[4]}| 
              ---------------- 
              """)

    def update_board(self, space):
        for index, num in enumerate(self.column_one):
            if num == space:
                self.column_one[index] = "X "
        for index, num in enumerate(self.column_two):
            if num == space:
                self.column_two[index] = "X "
        for index, num in enumerate(self.column_three):
            if num == space:
                self.column_three[index] = "X "
        for index, num in enumerate(self.column_four):
            if num == space:
                self.column_four[index] = "X "
        for index, num in enumerate(self.column_five):
            if num == space:
                self.column_five[index] = "X "

    @staticmethod
    def check(board):
        # Column Check
        if len(list(filter(lambda space: space == "X ", board.column_one))) == 5:
            return True
        if len(list(filter(lambda space: space == "X ", board.column_two))) == 5:
            return True
        if len(list(filter(lambda space: space == "X ", board.column_three))) == 5:
            return True
        if len(list(filter(lambda space: space == "X ", board.column_four))) == 5:
            return True
        if len(list(filter(lambda space: space == "X ", board.column_five))) == 5:
            return True

        # Row Check
        if len(list(filter(lambda space: space == "X ", [board.column_one[0], board.column_two[0], board.column_three[0], board.column_four[0], board.column_five[0]]))) == 5:
            return True
        if len(list(filter(lambda space: space == "X ", [board.column_one[1], board.column_two[1], board.column_three[1], board.column_four[1], board.column_five[1]]))) == 5:
            return True
        if len(list(filter(lambda space: space == "X ", [board.column_one[2], board.column_two[2], board.column_three[2], board.column_four[2], board.column_five[2]]))) == 5:
            return True
        if len(list(filter(lambda space: space == "X ", [board.column_one[3], board.column_two[3], board.column_three[3], board.column_four[3], board.column_five[3]]))) == 5:
            return True
        if len(list(filter(lambda space: space == "X ", [board.column_one[4], board.column_two[4], board.column_three[4], board.column_four[4], board.column_five[4]]))) == 5:
            return True

        # Diagonal Check
        if len(list(filter(lambda space: space == "X ", [board.column_one[0], board.column_two[1], board.column_three[2], board.column_four[3], board.column_five[4]]))) == 5:
            return True
        if len(list(filter(lambda space: space == "X ", [board.column_one[4], board.column_two[3], board.column_three[2], board.column_four[1], board.column_five[0]]))) == 5:
            return True
        
        return False


class Player:
    def __init__(self, num_boards=1):
        self.boards = [Board() for _ in range(num_boards)]
        self.wallet = 100

    def update_board_number(self, num_boards):
        self.boards = [Board() for _ in range(num_boards)]

    def render_boards(self):
        print("==============================================\n")
        print("              Current Board(s)")
        for board in self.boards:
            board.render_board()
        print("==============================================")  

    def update_boards(self, space):
        for board in self.boards:
            board.update_board(space)      

    def check_boards(self):
        for board in self.boards:
            if Board.check(board):
                return True
        return False


class Game:
    def __init__(self, player):
        self.player = player
        self.num_opponents = random.randint(3, 10)
        self.opponents = [Player() for _ in range(self.num_opponents)]
        self.jackpot = random.randrange(self.num_opponents * 5, self.num_opponents * 50, 5)
        self.picked_spaces = []

    def description(self):
        print(f"You will be playing against {self.num_opponents} opponents, with a total jackpot of ${self.jackpot}!\n")

    def initialize(self):
        while True:
            player_boards = input("How many boards would you like to purchase?\nBoards are $5 each:\n\n")
            if not player_boards.isnumeric() or player_boards == "0":
                print("\nI'm sorry, I didn't catch that...\n")
                time.sleep(1.5)
            else:
                player_boards = int(player_boards)
                cost = player_boards * 5
                if cost > self.player.wallet:
                    print(f"\nI'm sorry, but you can't afford that...\nYou only have ${self.player.wallet}\n")
                    time.sleep(1.5)
                else:
                    self.player.wallet = self.player.wallet - cost
                    print(f"\nGroovy, that will be ${cost}! You have ${self.player.wallet} left.\n")
                    break

        self.player.update_board_number(player_boards)
        for opponent in self.opponents:
            opponent.update_board_number(random.randint(1, player_boards))

    def pick_space(self):
        space = random.randint(1, 75)
        while space in self.picked_spaces:
            space = random.randint(1, 75)

        self.picked_spaces.append(space)

        if space <= 15:
            print(f"B{space}!")
        elif space <= 30:
            print(f"I{space}!")
        elif space <= 45:
            print(f"N{space}!")
        elif space <= 60:
            print(f"G{space}!")
        else:
            print(f"O{space}!")

        self.player.update_boards(space)
        for opponent in self.opponents:
            opponent.update_boards(space)
            if opponent.check_boards():
                return True

        return False

    def win(self):
        print(f"\nCONGRATULATIONS!!! You win today's jackpot of ${self.jackpot}!\n")
        self.player.wallet = self.player.wallet + self.jackpot
        time.sleep(1.5)

        print(f"You now have ${self.player.wallet}!\n")
        time.sleep(1.5)

    def lose(self):
        print("\nSuddenly, Sally stands up and yells 'BINGO!'\n")
        time.sleep(1.5)

        print("That's too bad... looks like they beat you to the win...\n")
        time.sleep(1.5)


def start(player):
    game = Game(player)

    print("\nA new Bingo game is about to start!\n")
    time.sleep(1.5)

    game.description()
    time.sleep(1.5)

    print(f"You currently have ${player.wallet}.\n")
    time.sleep(1.5)

    game.initialize()
    time.sleep(1.5)

    print("Let's take a look at your boards!\n")
    time.sleep(1.5)

    player.render_boards()
    input("Press return when ready...")

    print("\nOk, here comes the first space...\n")
    time.sleep(1.5)

    game.pick_space()
    time.sleep(1.5)

    print("\nLet's see how you did!\n")
    time.sleep(1.5)

    player.render_boards()
    user_input = input("Press return when ready... Or yell 'BINGO' if you have 5 in a row!\n\n")

    if user_input == "BINGO":
        print("\nI'm sorry, but I don't see any 5 in a rows on any of your boards...\n")
        time.sleep(1.5)

        print("Let's take another look...\n")
        time.sleep(1.5)

        player.render_boards()
        input("Press return when ready...")

    while True:
        print("\nOk, next space...\n")
        time.sleep(1)

        check = game.pick_space()
        time.sleep(1)

        if check:
            game.lose()
            break

        print("\nLet's see how you're doing!\n")
        time.sleep(1)

        player.render_boards()
        user_input = input("Press return when ready... Or yell 'BINGO' if you have 5 in a row!\n\n")

        if user_input == "BINGO":
            if player.check_boards():
                game.win()
                break
            else:
                print("\nI'm sorry, but I don't see any 5 in a rows on any of your boards...\n")
                time.sleep(1)

                print("Let's take another look...\n")
                time.sleep(1)

                player.render_boards()
                input("Press return when ready...")
    
    again = input("Want to play again? (Y/N)\n\n")
    if again == "Y":
        print("\nAwesome!\n")
        time.sleep(1.5)

        start(player)

    else:
        print("\nOk, See you next time!")

player = Player()
start(player)