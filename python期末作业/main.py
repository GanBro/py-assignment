import random

class Peg:
    def __init__(self, color, value):
        self.color = color
        self.value = value

class ColorGrid:
    def __init__(self, pegs):
        self.pegs = pegs
        self.noOfPegs = len(pegs)

class Rounds:
    def __init__(self, max_pegs_per_round, max_rounds, all_color_grid, computer_color_grid):
        self.maxPegsPerRound = max_pegs_per_round
        self.maxRounds = max_rounds
        self.allColorGrid = all_color_grid
        self.computerColorGrid = computer_color_grid
        self.roundGuesses = []

class Game:
    def __init__(self, rounds):
        self.rounds = rounds

    def welcome(self):
        print("+================================================================+")
        print("|                                                                |")
        print("|                 Welcome to MasterMind                          |")
        print("|                                                                |")
        print("+================================================================+")
        print("The game will use the colors defined in the settings file.")
        print(f"The maximum number of colored pegs in each round is set to {self.rounds.maxPegsPerRound}")

        available_colors = ', '.join(peg.color for peg in self.rounds.allColorGrid.pegs)
        print(f"The available colors which will be used are {available_colors}")
        input("Press the enter key to continue...")

    def play_game(self):
        print("Let's start the game!")
        for round_num in range(self.rounds.maxRounds):
            print(f"\nRound {round_num + 1}/{self.rounds.maxRounds}")

            # 玩家猜测阶段
            player_guess = self.get_player_guess()
            self.rounds.roundGuesses.append(player_guess)

            # 检查阶段
            correct_pegs = self.check_guess(player_guess)
            self.show_feedback(correct_pegs)

            # 判断是否猜对
            if correct_pegs == self.rounds.maxPegsPerRound:
                print("Congratulations! You guessed the correct sequence.")
                break

        # 游戏结束
        self.show_final_score()

    def get_player_guess(self):
        # 获取玩家猜测
        while True:
            guess_input = Input().get_user_input("Enter your guess (comma-separated colors): ")
            player_guess = ColorGrid([Peg(color.strip(), 0) for color in guess_input.split(',')])

            # 检查猜测是否合规
            if Validation().is_valid_guess(player_guess, self.rounds.allColorGrid):
                return player_guess
            else:
                print("Invalid guess. Please enter valid colors.")

    def check_guess(self, player_guess):
        # 检查玩家猜测和计算机生成的颜色序列的匹配情况
        correct_pegs = sum([1 for peg1, peg2 in zip(player_guess.pegs, self.rounds.computerColorGrid.pegs) if peg1.color == peg2.color])
        return correct_pegs

    def show_feedback(self, correct_pegs):
        # 显示反馈信息
        print(f"Correct pegs: {correct_pegs}/{self.rounds.maxPegsPerRound}")

    def show_final_score(self):
        # 显示最终分数和正确顺序
        print("\nGame Over!")
        print(f"Final score: {sum(peg.value for peg in self.rounds.roundGuesses[-1].pegs)}")
        print(f"Correct sequence: {[peg.color for peg in self.rounds.computerColorGrid.pegs]}")

class FileIO:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        # 读取文件操作
        with open(self.filename, 'r') as file:
            content = file.read()
        return content

    def write_file(self, content):
        # 写入文件操作
        with open(self.filename, 'w') as file:
            file.write(content)

class Input:
    def get_user_input(self, prompt):
        # 获取用户输入
        return input(prompt)

class Validation:
    def is_valid_guess(self, player_guess, all_color_grid):
        # 检查玩家猜测是否合规
        valid_colors = [peg.color for peg in all_color_grid.pegs]
        return all(peg.color in valid_colors for peg in player_guess.pegs)

if __name__ == "__main__":
    # 读取color.txt文件并初始化游戏设置
    file_io = FileIO("color.txt")
    content = file_io.read_file()

    # 解析color.txt文件内容
    lines = content.split('\n')
    max_pegs_per_round = int(lines[0])
    colors = lines[1:]

    # 初始化游戏设置
    all_color_grid = ColorGrid([Peg(color, i + 1) for i, color in enumerate(colors)])
    computer_color_grid = ColorGrid(random.sample(all_color_grid.pegs, max_pegs_per_round))
    rounds = Rounds(max_pegs_per_round, 5, all_color_grid, computer_color_grid)

    # 创建游戏对象并开始游戏
    game = Game(rounds)
    game.welcome()
    game.play_game()
