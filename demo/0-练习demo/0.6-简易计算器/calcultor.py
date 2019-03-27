import wx
from math import pi

# todo 平方，开方，sin，cos
class CalculatorFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, title="计算器", pos=(0, 0), size=(400, 250)):
        super(CalculatorFrame, self).__init__(
            parent, id=id, title=title, pos=pos, size=size
        )
        self.result = ""
        self.InitUI()
        self.Center()
        self.Show()

    def InitUI(self):
        # 存储计算结果
        self.result = ""
        # BoxSizer允许以行或列放置控件。
        vbox = wx.BoxSizer(wx.VERTICAL)
        # 添加 textprint 结果显示
        self.textprint = wx.TextCtrl(self, style=wx.TE_RIGHT | wx.TE_READONLY)
        vbox.Add(self.textprint, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
        # 添加gridsizer 二维布局防止按钮控件 参数依次为:rows-行数,cols列数,vgap-单元格垂直间距,hgap-水平间距
        gridBox = wx.GridSizer(5, 4, 5, 5)
        labels = [
            "AC",
            "DEL",
            "pi",
            "CLOSE",
            "7",
            "8",
            "9",
            "/",
            "4",
            "5",
            "6",
            "*",
            "1",
            "2",
            "3",
            "-",
            "0",
            ".",
            "=",
            "+",
        ]
        for label in labels:
            # 绑定函数,添加按钮
            buttonItem = wx.Button(self, label=label)
            self.createHandler(buttonItem, label)
            gridBox.Add(buttonItem, 1, wx.EXPAND)

        vbox.Add(gridBox, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)

    def createHandler(self, buttonItem, label):
        # 根据类型不同绑定函数
        item = "DEL AC = CLOSE"
        if label not in item:
            self.Bind(wx.EVT_BUTTON, self.OnAppend, buttonItem)
        elif label == "DEL":
            self.Bind(wx.EVT_BUTTON, self.OnDel, buttonItem)
        elif label == "AC":
            self.Bind(wx.EVT_BUTTON, self.OnAc, buttonItem)
        elif label == "=":
            self.Bind(wx.EVT_BUTTON, self.OnTarget, buttonItem)
        elif label == "CLOSE":
            self.Bind(wx.EVT_BUTTON, self.OnExit, buttonItem)

    def OnAppend(self, event):
        # 运算表达式追加
        eventbutton = event.GetEventObject()
        label = eventbutton.GetLabel()
        self.result += label
        self.textprint.SetValue(self.result)

    def OnDel(self, event):
        # 删除最后一位
        self.result = self.result[:-1]
        self.textprint.SetValue(self.result)

    def OnAc(self, event):
        # 清空
        self.textprint.Clear()
        self.result = ""

    def OnTarget(self, event):
        # 计算结果
        string = self.result
        # pi = math.pi
        try:
            if "/0" in string:  # 避免数字被零除
                raise SyntaxError
            else:
                target = eval(string)
                self.result = str(target)
                self.textprint.SetValue(self.result)
        except SyntaxError:
            dlg = wx.MessageDialog(  # 参数依次为 消息框内容，消息框标题
                self, u"格式错误，请输入正确的等式!", u"请注意", wx.OK | wx.ICON_INFORMATION
            )
            dlg.ShowModal()
            dlg.Destroy()

    def OnExit(self, event):
        # 退出
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    CalculatorFrame(title="简易计算器")
    app.MainLoop()
