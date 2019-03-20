import curses  # windows下需要安装 pip3 install windows-curses
from random import randrange, choice  # 随机数生成
from collections import defaultdict

# ord 返回 WASDRQwasdrq 对应的unicode
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
# zip返回列表，列表项是一个元组，例如 (20,'Up)，因为有大小写，所以actions需要*2匹配长度
actions_dict = dict(zip(letter_codes, actions * 2))
print(actions_dict)


# 获取用户输入
def get_user_action(keyboard):
    char = "N"
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]


# 矩阵转置
def transpose(field):
    return [list(row) for row in zip(*field)]


# 矩阵逆转
def invert(field):
    return [row[::-1] for row in field]


# 创建棋盘
class GameField(object):
    # 初始化棋盘宽高、单格胜利分数
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.highscore = 0
        self.field = None
        self.reset()

    # 生成随机数2或4
    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2  # 随机数90以上则出4
        (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    # 重置方法
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score  # 记录最高分
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()

    # 移动操作
    def move(self, direction):
        # 单行向左移动
        def move_row_left(row):
            def tighten(row):  # 把单元格挤到一起
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):  # 合并单元格
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:  # 成对则合并
                        new_row.append(2 * row[i])  # 数组内添加双倍分数
                        self.score += 2 * row[i]  # 加分
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:  # 如果右侧的格子小于单元格数并且 数值相等，则说明成对
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)  # 如果为真则继续,否则抛出异常
                return new_row

            return tighten(merge(tighten(row)))  # 整理合并后的单元格,然后再合并+整理递归

        # 通过对矩阵进行转置与逆转，可以直接从左移得到其余三个方向的移动操作
        moves = {}
        # 此处 \ 用于多行语句，在(){}[]中不需要
        moves['Left'] = lambda field: \
            [move_row_left(row) for row in field]
        moves['Right'] = lambda field: \
            invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field: \
            transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field: \
            transpose(moves['Right'](transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):  # 判断是否可移动
                self.field = moves[direction](self.field)  # 执行move操作，传入field棋盘
                self.spawn()  # 移动之后生成新随机数
                return True
            else:
                return False

    # 检测是否移动
    def move_is_possible(self, direction):
        def row_is_left_movable(row):
            def change(i):  # true if there'll be change in i-th tile
                if row[i] == 0 and row[i + 1] != 0:  # 有空格可移动
                    return True
                if row[i] != 0 and row[i + 1] == row[i]:  # 相等可合并
                    return True
                return False

            return any(change(i) for i in range(len(row) - 1))  # 检测每行是否有可移动的

        check = {}
        check['Left'] = lambda field: \
            any(row_is_left_movable(row) for row in field)

        check['Right'] = lambda field: \
            check['Left'](invert(field))

        check['Up'] = lambda field: \
            check['Left'](transpose(field))

        check['Down'] = lambda field: \
            check['Right'](transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False

    # 绘制棋盘
    def draw(self, screen):
        # 提示文本
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '     (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '          YOU WIN!'

        def cast(string):
            screen.addstr(string + '\n')

        # 水平分隔线
        def draw_hor_separator():
            line = '+' + ('+------' * self.width + '+')[1:]
            separator = defaultdict(lambda: line)
            if not hasattr(draw_hor_separator, "counter"):
                draw_hor_separator.counter = 0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1

        # 行
        def draw_row(row):
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')

        screen.clear()
        cast('SCORE: ' + str(self.score))
        if 0 != self.highscore:
            cast('HIGHSCORE: ' + str(self.highscore))
        for row in self.field:
            draw_hor_separator()
            draw_row(row)
        draw_hor_separator()
        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string1)
        cast(help_string2)

    # 判断胜利 检测所有单元格分数大于win分数
    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)

    # 判断失败 所有动作都无法移动
    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)


def main(stdscr):
    def init():
        # 重置游戏棋盘
        game_field.reset()
        return 'Game'

    def not_game(state):
        # 画出 GameOver 或者 Win 的界面
        game_field.draw(stdscr)
        # 读取用户输入得到action，判断是重启游戏还是结束游戏
        action = get_user_action(stdscr)
        responses = defaultdict(lambda: state)  # 默认是当前状态，没有行为就会一直在当前界面循环
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'  # 对应不同的行为转换到不同的状态
        return responses[action]

    def game():
        # 画出当前棋盘状态
        game_field.draw(stdscr)
        # 读取用户输入得到action
        action = get_user_action(stdscr)

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action):  # move successful
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'

    state_actions = {
        'Init': init,
        'Win': lambda: not_game('Win'),
        'Gameover': lambda: not_game('Gameover'),
        'Game': game
    }

    # curses 控制台绘制
    curses.use_default_colors()

    # 设置终结状态最大数值为
    game_field = GameField()

    state = 'Init'

    # 状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()


curses.wrapper(main)
