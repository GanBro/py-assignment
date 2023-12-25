import random

class Peg:
    def __init__(self, color, value):
        self.color = color  # 彩钉的颜色
        self.value = value  # 彩钉的值

class ColorGrid:
    def __init__(self, pegs):
        self.pegs = pegs  # 彩钉列表
        self.noOfPegs = len(pegs)  # 彩钉的数量

class Rounds:
    def __init__(self, max_pegs_per_round, max_rounds, all_color_grid, computer_color_grid):
        self.maxPegsPerRound = max_pegs_per_round  # 每回合的最大彩钉数
        self.maxRounds = max_rounds  # 最大回合数
        self.allColorGrid = all_color_grid  # 所有可用彩钉
        self.computerColorGrid = computer_color_grid  # 计算机生成的彩钉序列
        self.roundGuesses = []  # 每轮猜测得分的列表

class Game:
    def __init__(self, rounds):
        self.rounds = rounds

    @staticmethod
    def get_user_input(prompt):
        # 获取用户输入
        return input(prompt)

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
        self.rounds.maxRounds = int(Game.get_user_input("Please enter the number of rounds you would like to play: "))
        print(f"Computer has generated a color grid consisting of {self.rounds.maxPegsPerRound} colors.")

    def validate_input(self, player_guess, sensitive_words):
        # 检查玩家猜测是否合规，且不包含敏感词汇
        valid_colors = [peg.color for peg in self.rounds.allColorGrid.pegs]
        if not all(peg.color in valid_colors for peg in player_guess.pegs):
            return False
        for word in sensitive_words:
            if word in player_guess.pegs[0].color:
                return False
        return True

    def check_guess(self, player_guess): # ColorGrid对象
        # 检查玩家猜测和计算机生成的颜色序列的匹配情况
        correct_pegs = 0
        for peg1, peg2 in zip(player_guess.pegs, self.rounds.computerColorGrid.pegs):
            if peg1.color == peg2.color and peg1.value == peg2.value:
                correct_pegs += 1
        return correct_pegs

    def output_incorrect_guess_message(self, num_correct_colors):
        print(f"Unfortunately, you only managed to guess # {num_correct_colors} colors correctly!")
        print("Still another round. Try again!")
        input("Press the enter key to continue...")

    def check_guesses(self, player_guesses):
        """
        判断玩家猜测是否与计算机生成的彩钉序列完全相同
        """
        if player_guesses.noOfPegs != len(self.rounds.computerColorGrid.pegs):
            return 0

        match_count = 0  # 计数器，用于记录匹配的彩钉数量

        for i in range(player_guesses.noOfPegs):
            if player_guesses.pegs[i].color == self.rounds.computerColorGrid.pegs[i].color:
                match_count = match_count + 1
        return match_count

    def play_game(self):
        sensitive_words = ["文化大革命", "六四事件", "政治敏感"]
        for round_num in range(self.rounds.maxRounds):
            print(f"Beginning Round {round_num + 1}")
            player_score = 0

            # 计算机生成一个随机的彩钉顺序
            # self.rounds.computerColorGrid = ColorGrid(
            #     random.sample(self.rounds.allColorGrid.pegs, self.rounds.maxPegsPerRound))

            # 玩家猜测阶段
            print(f"Player Score: {player_score}")
            print(f"The available colors which can be used are {', '.join(peg.color for peg in self.rounds.allColorGrid.pegs)}")

            # 玩家输入猜测
            pegs_list = []  # 存储玩家所有的猜测
            i = 1  # 设置初始的下标为1
            while len(pegs_list) < self.rounds.maxPegsPerRound:  # 只有当玩家猜测未达到最大彩钉数时才继续循环
                guess_color = Game.get_user_input(f"Please enter your guess for the {i} color...")
                if guess_color.strip() in [peg.color for peg in self.rounds.allColorGrid.pegs]:
                    pegs_list.append(Peg(guess_color.strip(), i)) # 将玩家猜测添加到列表中
                    i += 1  # 下标加1
                else:
                    print("Please enter a color from the provided list only.")
            player_guesses = ColorGrid(pegs_list)
            player_score += self.check_guesses(player_guesses)
            # 假设secret_code是正确的答案，player_guess是玩家的猜测
            if player_score == player_guesses.noOfPegs: # 完全匹配才算成功
                print("猜测成功!")
                break
            else:
                self.output_incorrect_guess_message(player_score)
                continue


            # 显示本轮得分
            print(f"Player Score for Round {round_num + 1}: {player_score}")
            self.rounds.roundGuesses.append(player_score)

        # 游戏结束
        self.show_final_score()

    def show_final_score(self):
        total_score = sum(self.rounds.roundGuesses)
        print(f"Game Over!\nTotal Score: {total_score}")

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

if __name__ == "__main__":
    # 读取color.txt文件并初始化游戏设置
    file_io = FileIO("color.txt")  # 创建一个FileIO对象，用于读取文件
    content = file_io.read_file()  # 读取文件内容

    # 解析color.txt文件内容
    lines = content.split('\n')  # 将文件内容按行分割
    max_pegs_per_round = int(lines[0])  # 获取每轮游戏中的最大彩钉数
    colors = lines[1:]  # 获取可用的颜色列表

    # 初始化游戏设置
    all_color_grid = ColorGrid([Peg(color, random.randint(1, 10)) for i, color in enumerate(colors)])  # 创建包含所有颜色的ColorGrid对象
    computer_color_grid = ColorGrid(random.sample(all_color_grid.pegs, max_pegs_per_round))  # 创建计算机生成的彩钉序列
    rounds = Rounds(max_pegs_per_round, 5, all_color_grid, computer_color_grid)  # 创建Rounds对象，用于跟踪游戏的回合信息

    # 正确序列
    for peg in computer_color_grid.pegs:
        print(str(peg.color))

    # 创建游戏对象并开始游戏
    game = Game(rounds)  # 创建Game对象，传入Rounds对象
    game.welcome()  # 显示游戏欢迎信息
    game.play_game()  # 开始游戏逻辑的执行