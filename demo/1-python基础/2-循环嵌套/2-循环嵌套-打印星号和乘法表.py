# 1 打印5行星号，星号数量依次递增
def print_star():
    line = 1
    while line <= 5:
        print("*" * line)
        line += 1


print_star()


# 2 九九乘法表
def print_multiplication_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print(str(col) + ' * ' + str(row) + ' = ' + str(row * col) + '   ', end='\t')
            # 此处end用于避免print函数的自动换行,\t制表符在输出文本时，垂直方向保持对齐
            col += 1
        row += 1
        print('')  # 用于手动换行


print_multiplication_table()
