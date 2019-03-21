# 图片转字符画
# 原理：利用灰度值公式将像素的RGB值映射到灰度值 gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b
# 调用方法：python pic2str.py [目标图片文件名，包括后缀] -o [输出文件名] --width [宽度] --height [高度]


# 引入图像处理库pillow(PIL) $ pip3 install Pillow
from PIL import Image

# 用于管理命令行参数输入
import argparse

# 命令行输入参数处理 ArgumentParser 实例
parser = argparse.ArgumentParser()

# 定义输入文件、输出文件、输出字符画的宽高
parser.add_argument("file")
parser.add_argument("-o", "--output")
parser.add_argument("--width", type=int, default=80)
parser.add_argument("--height", type=int, default=80)

# 解析并获取参数
args = parser.parse_args()

# 输入的图片路径
IMG = args.file

# 输出字符画的宽高
HEIGHT = args.height
WIDTH = args.width

# 输出字符画的路径
OUTPUT = args.output

# 灰度字符集
ascii_char = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
)


# RGBA值映射成灰度值
def get_char(r, g, b, alpha=256):
    # 判断alpha值,为0时表示图片中该位置为空白
    if alpha == 0:
        return " "

    # 获取字符集的长度
    length = len(ascii_char)

    # 将rgb值转为灰度值，范围0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    # 字符集与灰度值范围有差距，需要计算映射
    unit = (256.0 + 1) / length

    # 返回灰度值对应的字符集
    return ascii_char[int(gray / unit)]


# 处理图片
if __name__ == "__main__":  # 表示此py文件被作为模块import引入时，这部分代码不会被执行
    # 初始化输出的字符串值
    txt = ""

    # 使用PIL的Image.open获取图片对象
    im = Image.open(IMG)

    # 通过PIL的resize调整图片大小，对应输出到字符画的宽高，第二个参数使用Image.NEAREST，表示输出低质量的图片
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    # 遍历提取图片中每行像素的RGB值，调用get_char转成对应字符
    for row in range(HEIGHT):
        for col in range(WIDTH):
            # 将所有像素对应的字符串拼接成一个字符串txt
            # im.getpixel((col.row))获取到坐标未知的RGB像素值，返回一个元组，使用*将元组拆包作为参数传递给函数
            txt += get_char(*im.getpixel((col, row)))
        # 换行
        txt += "\n"

    # 打印输出字符串txt
    print(txt)

    # 如果执行时配置了输出文件，将打开文件并把txt输出到指定文件中，如果没有则默认输出到output.txt
    if OUTPUT:
        with open(OUTPUT, "w") as f:
            f.write(txt)
    else:
        with open("output.txt", "w") as f:
            f.write(txt)

# 附录 ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type]
# [, choices][, required][, help][, metavar][, dest])的参数集合
# name or flags - 选项字符串的名字或者列表，例如foo 或者-f, --foo，-表示是可选项
# action - 在命令行遇到该参数时采取的基本动作类型。
# nargs - 应该读取的命令行参数数目。
# const - 某些action和nargs选项要求的常数值。
# default - 如果命令行中没有出现该参数时的默认值。
# type - 命令行参数应该被转换成的类型。
# choices - 参数可允许的值的一个容器。
# required - 该命令行选项是否可以省略（只针对可选参数）。
# help - 参数的简短描述。
# metavar - 参数在帮助信息中的名字。
# dest - 给parse_args()返回的对象要添加的属性名称。
