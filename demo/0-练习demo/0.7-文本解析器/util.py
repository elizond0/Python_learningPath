# 拆分文本块
def lines(file):
    # yield会将函数变成生成器，调用lines函数会返回一个 iterable 对象
    # 如果没有 return，则默认执行至函数完毕;return则直接抛出 StopIteration 终止迭代。
    for line in file:
        yield line
    # 在文本最后加一空行
    yield "\n"


def blocks(file):
    # 调用生成器,生成单独的文本块
    block = []
    # 在 for 循环执行时，每次循环都会执行 lines 函数内部的代码，执行到 yield b 时，
    # lines 函数就返回一个迭代值，下次迭代时，代码从 yield line 的下一条语句继续执行
    # 而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield
    for line in lines(file):
        # strip() 函数可以去除一个字符串前后的空格以及换行符
        # 如果在strip()函数添加不同的参数，如strip("haha")，则可以去除字符串前后的"haha"字符。
        if line.strip():
            block.append(line)
        elif block:
            yield "".join(block).strip()
            block = []

