# 解析规则

# 规则父类
class Rule(object):
    def __init__(self, type=None):
        self.type = type

    def action(self, block, handler):
        # 加标记,block-文本块，handler-处理函数
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class HeadingRule(Rule):
    # heading头部
    def __init__(self):
        self.type = "heading"

    # confition用于判断是否符合规则
    def condition(self, block):
        # 条件为：文本块中有换行符，文本长度小于等于70，且最后一个字符串不为‘：’
        return not "\n" in block and len(block) <= 70 and not block[-1] == ":"


class TitleRule(HeadingRule):
    # title标题
    def __init__(self):
        self.type = "title"
        self.first = True

    def condition(self, block):
        # 仅第一次进入时才进行条件判断，即第一个heading会被视为title
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self, block)


class ListRule(Rule):
    # 列表规则 在执行li规则之前添加ul标签
    def __init__(self):
        self.type = "list"
        self.inside = False  # 主要用于关联两个相连的标识符

    def condition(self, block):
        return True

    def action(self, block, handler):
        # inside==false且符合listItem，则添加开始标签。
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False


class ListItemRule(Rule):
    # 列表项规则
    def __init__(self):
        self.type = "listitem"

    def condition(self, block):
        # 文本块以"-"开头
        return block[0] == "-"

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())  # 截取-以后的内容，并去除空格换行
        handler.end(self.type)
        return True


class ParagraphRule(Rule):
    # 段落规则
    def __init__(self):
        self.type = "paragraph"

    def condition(self, block):
        return True
