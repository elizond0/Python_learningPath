import wx
import os
import random
import copy


class Frame(wx.Frame):
    def __init__(self, title, rows=4, cols=4):
        super().__init__(
            None,
            -1,
            title=title,
            style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER,
        )

        self._rows = rows
        self._cols = cols
        # 数字背景色对应的rgb颜色
        self.colors = {
            0: (204, 192, 179),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 207, 114),
            512: (237, 207, 114),
            1024: (237, 207, 114),
            2048: (237, 207, 114),
            4096: (237, 207, 114),
            8192: (237, 207, 114),
            16384: (237, 207, 114),
            32768: (237, 207, 114),
            65536: (237, 207, 114),
            131072: (237, 207, 114),
            262144: (237, 207, 114),
            524288: (237, 207, 114),
            1048576: (237, 207, 114),
        }
        # 配置icon、初始化游戏和缓冲器，缓冲器用于绘制图形界面
        # self.setIcon()
        self.initGame()
        self.initBuffer()
        # 生成界面，绑定按键方法
        panel = wx.Panel(self)
        panel.SetFocus()
        panel.Bind(wx.EVT_CHAR_HOOK, self.onKeyDown)
        # 绑定改变边框、绘制、关闭方法
        self.Bind(wx.EVT_SIZE, self.onSize)
        self.Bind(wx.EVT_PAINT, self.onPaint)
        self.Bind(wx.EVT_CLOSE, self.onClose)
        # 配置默认界面的宽高，居中
        self.SetClientSize((505, 600))
        self.Center()
        self.Show()

    def setIcon(self):
        icon = wx.Icon("./icon.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

    def initGame(self):
        # 初始化字体样式 Font参数：尺寸，指定的字体，斜体，粗细
        self.bgFont = wx.Font(50, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.scFont = wx.Font(36, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.smFont = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL)
        # 初始化分数容器
        self.curScore = 0
        self.bstScore = 0
        self.loadScore()
        self.data = [([0] * self._cols) for i in range(self._rows)]
        count = 0
        # 生成2个新数字
        while count < 2:
            row = random.randint(0, len(self.data) - 1)
            col = random.randint(0, len(self.data[0]) - 1)
            # 单元格值为0时，重新随机，count数量不增加，依旧会生成2个新数字
            if self.data[row][col] != 0:
                continue
            self.data[row][col] = 2 if random.randint(0, 1) else 4
            count += 1

    def initBuffer(self):
        # 获取界面宽高并传入
        w, h = self.GetClientSize()
        self.buffer = wx.Bitmap(w, h)

    def onClose(self, event):
        self.saveScore()
        self.Destroy()

    def onSize(self, event):
        self.initBuffer()
        self.drawAll()

    def onPaint(self, evet):
        # 缓存绘画命令，直到命令完整并准备在屏幕上绘画
        dc = wx.BufferedPaintDC(self, self.buffer)

    def saveScore(self):
        # 打开分数文件并写入
        ff = open("bestscore.ini", "w")
        ff.write(str(self.bstScore))
        ff.close()

    def loadScore(self):
        # 读取本地分数文件
        if os.path.exists("bestscore.ini"):
            ff = open("bestscore.ini")
            self.bstScore = int(ff.read())
            ff.close()

    def drawAll(self):
        # 绘制背景、logo、标签、分数、单元格
        dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
        self.drawBg(dc)
        self.drawLogo(dc)
        self.drawLabel(dc)
        self.drawScore(dc)
        self.drawTiles(dc)

    def onKeyDown(self, event):
        # 获取键盘输入，根据上下左右进行操作
        keyCode = event.GetKeyCode()
        if keyCode == wx.WXK_UP:
            self.doMove(*self.slideUpDown(True))
        elif keyCode == wx.WXK_DOWN:
            self.doMove(*self.slideUpDown(False))
        elif keyCode == wx.WXK_LEFT:
            self.doMove(*self.slideLeftRight(True))
        elif keyCode == wx.WXK_RIGHT:
            self.doMove(*self.slideLeftRight(False))
        elif keyCode == wx.WXK_SPACE:
            self.restart()

    def doMove(self, isChanged, score):
        # 如果值改变:在0的位置上生成随机数字 -> 重绘更改的值 -> 判断是否游戏结束
        if isChanged:
            self.putTile(1)
            self.drawChange(score)
            if self.isGameOver():
                # 游戏结束后，如果用户点击确定，则保存最高分，重绘界面
                if (
                    wx.MessageBox(
                        u"游戏结束，是否重新开始？", u"哈哈", wx.YES_NO | wx.ICON_INFORMATION
                    )
                    == wx.YES
                ):
                    self.restart()

    def putTile(self, number):
        count = 0
        available = []
        while count < number:
            # 遍历，如果单元格为0，则将二维索引值保存到数组中，标记为可随机生成的空格
            for row in range(len(self.data)):
                for col in range(len(self.data[0])):
                    if self.data[row][col] == 0:
                        available.append((row, col))
            # 空格数不为0，则随机空格生成数字
            if available:
                row, col = available[random.randint(0, len(available) - 1)]
                self.data[row][col] = 2 if random.randint(0, 1) else 4

            count += 1

    def drawChange(self, score):
        # 当单元格变化时重新绘制，例如每次操作之后
        # 缓冲可将绘画命令单独发送到缓冲区，然后一次性的绘制到屏幕，防止闪烁
        # clientDC指窗口的" "主区域也称客户区(不包括边框、装饰、标题栏)。
        # 第一个参数指要绘制到的设备上下文，第二个参数则是一个位图，被作为一个临时的缓冲"
        dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
        if score:
            self.curScore += score
            if self.curScore > self.bstScore:
                self.bstScore = self.curScore
            self.drawScore(dc)
        self.drawTiles(dc)

    def slideUpDown(self, up):
        # 垂直移动
        score = 0
        numCols = len(self.data[0])
        numRows = len(self.data)
        # 深拷贝二维数组，避免引用地址同步修改
        oldData = copy.deepcopy(self.data)
        # 遍历每列，cvl为单列数组
        for col in range(numCols):
            # 取单元格值不为零，组成数组赋给cvl
            cvl = [
                self.data[row][col]
                for row in range(numRows)
                if self.data[row][col] != 0
            ]

            # 单列数据不为零的数至少2时，进入合并操作的判定
            if len(cvl) >= 2:
                score += self.update(cvl, up)
            # 不足的格数，用0填满
            for i in range(numRows - len(cvl)):
                if up:
                    cvl.append(0)
                else:
                    cvl.insert(0, 0)  # 在index为0处，插入一个0
            # 修改储存的二维数组单元格的值
            for row in range(numRows):
                self.data[row][col] = cvl[row]
        # 返回数据是否变化的bool值和分数
        return oldData != self.data, score

    def slideLeftRight(self, left):
        # 水平移动，与slideTopDown类似
        score = 0
        numCols = len(self.data[0])
        numRows = len(self.data)
        oldData = copy.deepcopy(self.data)
        for row in range(numRows):
            rvl = [
                self.data[row][col]
                for col in range(numCols)
                if self.data[row][col] != 0
            ]
            if len(rvl) >= 2:
                score += self.update(rvl, left)
            for i in range(numCols - len(rvl)):
                if left:
                    rvl.append(0)
                else:
                    rvl.insert(0, 0)
            for col in range(numRows):
                self.data[row][col] = rvl[col]
        return oldData != self.data, score

    def update(self, vlist, direct):
        score = 0
        # direct为true上或左，然后决定数组遍历的升降序
        # 此处vlist通过index直接修改值，由于内存地址不变，因此cvl/rvl值也会跟随改变
        if direct:
            i = 1
            while i < len(vlist):
                # 相等则合并，分数相加
                if vlist[i - 1] == vlist[i]:
                    del vlist[i]
                    vlist[i - 1] *= 2
                    score += vlist[i - 1]
                    i += 1
                i += 1
        else:
            i = len(vlist) - 1
            while i > 0:
                if vlist[i - 1] == vlist[i]:
                    del vlist[i]
                    vlist[i - 1] *= 2
                    score += vlist[i - 1]
                    i -= 1
                i -= 1
        return score

    def drawBg(self, dc):
        # 背景画刷当Clear被调用时使用
        dc.SetBackground(wx.Brush((250, 248, 239)))
        dc.Clear()
        # 用于填充绘制于设备上下文的形状，是一个wx.Brush对象
        dc.SetBrush(wx.Brush((187, 173, 160)))
        # 画笔是一个wx.Pen对象，用于所有绘制线条的操作
        dc.SetPen(wx.Pen((187, 173, 160)))
        # 圆角，x,y,w,h,r，r为正值，以像素为单位半径，反之矩形较小边的比例
        dc.DrawRoundedRectangle(15, 110, 475, 475, 5)

    def drawLogo(self, dc):
        # 文本的绘制
        dc.SetFont(self.bgFont)
        # 字体前景色
        dc.SetTextForeground((119, 110, 101))
        # 绘制的文本内容,开始绘制的坐标(x,y)，使用当前的字体前景背景色
        dc.DrawText("2048", 15, 10)

    def drawLabel(self, dc):
        # 标签字体、前景色
        dc.SetFont(self.smFont)
        dc.SetTextForeground((119, 110, 101))
        dc.DrawText("方向键移动，空格重置", 15, 80)

    def drawScore(self, dc):
        dc.SetFont(self.smFont)
        # 得到字符串将占用的矩形范围的尺寸，以元组的方式返回
        scoreLabelSize = dc.GetTextExtent("SCORE")
        bestLabelSize = dc.GetTextExtent("BEST")
        # 预先重设容纳字符的两个矩形的宽,15水平边距
        curScoreBoardMinW = 15 * 2 + scoreLabelSize[0]
        bstScoreBoardMinW = 15 * 2 + bestLabelSize[0]
        # 获取实际可变内容的尺寸，即分数文本
        curScoreSize = dc.GetTextExtent(str(self.curScore))
        bstScoreSize = dc.GetTextExtent(str(self.bstScore))
        # 预先重设可变内容的宽度，10水平边距
        curScoreBoardNedW = 10 + curScoreSize[0]
        bstScoreBoardNedW = 10 + bstScoreSize[0]
        # 以矩形与可变内容的比较，文本上下排列，获取最大值
        curScoreBoardW = max(curScoreBoardMinW, curScoreBoardNedW)
        bstScoreBoardW = max(bstScoreBoardMinW, bstScoreBoardNedW)

        dc.SetBrush(wx.Brush((187, 173, 160)))
        dc.SetPen(wx.Pen((187, 173, 160)))
        # 绘制两个圆角矩形，参数 起始点x、起始点y、宽度、高度、圆角radius
        dc.DrawRoundedRectangle(505 - 15 - bstScoreBoardW, 40, bstScoreBoardW, 50, 3)
        dc.DrawRoundedRectangle(
            505 - 15 - bstScoreBoardW - 5 - curScoreBoardW, 40, curScoreBoardW, 50, 3
        )
        dc.SetTextForeground((238, 228, 218))
        # 绘制字符串
        dc.DrawText(
            "BEST",
            505 - 15 - bstScoreBoardW + (bstScoreBoardW - bestLabelSize[0]) / 2,
            48,
        )
        dc.DrawText(
            "SCORE",
            505
            - 15
            - bstScoreBoardW
            - 5
            - curScoreBoardW
            + (curScoreBoardW - scoreLabelSize[0]) / 2,
            48,
        )
        dc.SetTextForeground((255, 255, 255))
        # 绘制可变内容字符串
        dc.DrawText(
            str(self.bstScore),
            505 - 15 - bstScoreBoardW + (bstScoreBoardW - bstScoreSize[0]) / 2,
            68,
        )
        dc.DrawText(
            str(self.curScore),
            505
            - 15
            - bstScoreBoardW
            - 5
            - curScoreBoardW
            + (curScoreBoardW - curScoreSize[0]) / 2,
            68,
        )

    def drawTiles(self, dc):
        dc.SetFont(self.scFont)
        for row in range(self._rows):
            for col in range(self._cols):
                value = self.data[row][col]
                # 设置背景色
                color = self.colors[value]
                # 若值为2或4则字体的颜色为棕色反之为白色
                if value == 2 or value == 4:
                    dc.SetTextForeground((119, 110, 101))
                else:
                    dc.SetTextForeground((255, 255, 255))

                # 绘制小方块
                dc.SetBrush(wx.Brush(color))
                dc.SetPen(wx.Pen(color))
                dc.DrawRoundedRectangle(30 + col * 115, 125 + row * 115, 100, 100, 2)
                size = dc.GetTextExtent(str(value))

                # 绘制方块中的数字，若数字的尺寸大于70像素(将要超过方块的尺寸)则重设数字字体的大小
                while size[0] > 100 - 15 * 2:
                    self.scFont = wx.Font(
                        self.scFont.GetPointSize() * 4 / 5, wx.SWISS, wx.NORMAL, wx.BOLD
                    )
                    dc.SetFont(self.scFont)
                    size = dc.GetTextExtent(str(value))
                if value != 0:
                    dc.DrawText(
                        str(value),
                        30 + col * 115 + (100 - size[0]) / 2,
                        125 + row * 115 + (100 - size[1]) / 2,
                    )

    def restart(self):
        bstScore = self.bstScore
        self.initGame()
        self.bstScore = bstScore
        self.drawAll()

    def isGameOver(self):
        # 判断4个方向是否可以移动,slide函数的第一个返回值为true就代表可移动
        copyData = copy.deepcopy(self.data)
        flag = False

        if (
            not self.slideLeftRight(True)[0]
            and not self.slideLeftRight(False)[0]
            and not self.slideUpDown(True)[0]
            and not self.slideUpDown(False)[0]
        ):
            flag = True
        # 由于slide方法会修改data二维数组的值，因此尝试是否可移动后，需要恢复成原来的值
        if not flag:
            self.data = copyData

        return flag


if __name__ == "__main__":
    app = wx.App()
    Frame(title="2048_with_GUI")
    # Frame(title="2048_with_GUI", rows=5, cols=5)
    app.MainLoop()

