# 文本解析
import sys, re  # sys-系统相关　　　re-正则
from handlers import *
from util import *
from rules import *

# todo 添加标签 匹配md语法 样式修正


class Parser:
    # 解析器父类
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        # 添加规则
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        # 添加过滤器
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)

        self.filters.append(filter)

    def parse(self, file):
        # 解析
        self.handler.start("document")
        for block in blocks(file):
            # 遍历过滤器
            for filter in self.filters:
                block = filter(block, self.handler)
            # 遍历匹配规则
            for rule in self.rules:
                if rule.condition(block):
                    # 匹配成功，则执行操作(添加开闭标签)，部分标签，需要多层匹配，根据action返回值判断
                    last = rule.action(block, self.handler)
                    if last:
                        break
        self.handler.end("document")


class BasicTextParser(Parser):
    # 纯文本解析器
    def __init__(self, handler):
        Parser.__init__(self, handler)
        # 解析顺序很重要
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        # r表示不转义，常用于正则表达式以及系统路径
        # u表示unicodestring，默认byte string ASCII编码，指定编码方式，可在文件顶部加入 # -*- coding: utf-8 -*-
        self.addFilter(r"\*(.+?)\*", "emphasis")
        self.addFilter(r"(http://[\.a-zA-Z/]+)", "url")
        self.addFilter(r"([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)", "mail")


# handler = HTMLRenderer()
# parser = BasicTextParser(handler)

# 1.控制台调用方法参数  @输入内容文件名 @输出内容文件名 例如：python markup.py <test.txt> test.html
# 实例化html渲染器、解析器，sys.stdin
parser.parse(sys.stdin)

# 2.py文件内定义文件名
txt_name = "./test.txt"
# try:
#     file = open(txt_name, "r", encoding="utf-8")  # r-文本文件，rb-二进制文件，默认r
#     print(file)
# finally:
#     if file:
#         file.close()

# 读写文件可能出现IOError，在finally中调用close，保证关闭
# 通过with方法可以实现同样效果
# with open(txt_name, "r", encoding="utf-8") as file:
#     print(file)
