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

        # 提示玩家输入需要猜测的次数
        self.rounds.maxRounds = int(Input().get_user_input("Please enter the number of rounds you would like to play: "))
        print(f"Computer has generated a color grid consisting of {self.rounds.maxPegsPerRound} colors.")

    def play_game(self):

        for round_num in range(self.rounds.maxRounds):
            print(f"Beginning Round {round_num + 1}")
            player_score = 0

            # 计算机生成一个随机的彩钉顺序
            self.rounds.computerColorGrid = ColorGrid(random.sample(self.rounds.allColorGrid.pegs, self.rounds.maxPegsPerRound))

            # 玩家猜测阶段
            print(f"Player Score: {player_score}")
            print(f"The available colors which can be used are {', '.join(peg.color for peg in self.rounds.allColorGrid.pegs)}")

            # 玩家输入猜测
            for i in range(1, self.rounds.maxPegsPerRound + 1):
                guess_color = Input().get_user_input(f"Please enter your guess for the {i} color...")
                player_guess = ColorGrid([Peg(guess_color.strip(), 0)])

                # 检查猜测是否合规
                if Validation().is_valid_guess(player_guess, self.rounds.allColorGrid):
                    # 检查玩家猜测和计算机生成的颜色序列的匹配情况
                    correct_pegs = self.check_guess(player_guess)
                    player_score += correct_pegs
                else:
                    print("Invalid guess. Please enter a valid color.")
                    i -= 1  # 重新让玩家输入

            # 显示本轮得分
            print(f"Player Score for Round {round_num + 1}: {player_score}")

        # 游戏结束
        self.show_final_score()

    def check_guess(self, player_guess):
        # 检查玩家猜测和计算机生成的颜色序列的匹配情况
        correct_pegs = sum([1 for peg1, peg2 in zip(player_guess.pegs, self.rounds.computerColorGrid.pegs) if peg1.color == peg2.color])
        return correct_pegs


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

