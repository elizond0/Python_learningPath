# 图形化ui界面 $ pip install wxPython==4.0.4
import wx
import telnetlib
from time import sleep
import _thread as thread

# 登录窗口
class LoginFrame(wx.Frame):
    def __init__(self, parent, id, title, size):
        # 初始化，添加控件并绑定事件
        wx.Frame.__init__(self, parent, id, title)
        self.SetSize(size)
        self.Center()
        self.serverAddressLabel = wx.StaticText(
            self, label="服务器地址", pos=(10, 50), size=(120, 25)
        )
        self.userNameLabel = wx.StaticText(
            self, label="用户名", pos=(40, 100), size=(120, 25)
        )
        self.serverAddress = wx.TextCtrl(self, pos=(120, 47), size=(150, 25))
        self.userName = wx.TextCtrl(self, pos=(120, 97), size=(150, 25))
        self.loginButton = wx.Button(self, label="登录", pos=(80, 145), size=(130, 30))
        # 绑定登录方法
        self.loginButton.Bind(wx.EVT_BUTTON, self.login)
        self.Show()

    def login(self, event):
        # 登录处理
        try:
            serverAddress = self.serverAddress.GetLineText(0).split(":")
            con.open(serverAddress[0], port=int(serverAddress[1]), timeout=10)  # 打开端口
            response = con.read_some()
            if response != b"Connect Success":
                self.showDialog("Error", "连接失败!", (200, 100))
                return
            con.write(
                ("login " + str(self.userName.GetLineText(0)) + "\n").encode("utf-8")
            )
            response = con.read_some()
            if response == b"UserName Empty":
                self.showDialog("Error", "用户名为空!", (200, 100))
            elif response == b"UserName Exist":
                self.showDialog("Error", "用户名已存在!", (200, 100))
            else:
                self.Close()
                ChatFrame(None, 2, title="文字聊天室", size=(520, 400))
        except Exception:
            self.showDialog("Error", "连接失败!", (95, 20))

    def showDialog(self, title, content, size):
        # 显示错误信息对话框
        dialog = wx.Dialog(self, title=title, size=size)
        dialog.Center()
        wx.StaticText(dialog, label=content)
        dialog.ShowModal()


# 聊天室窗口
class ChatFrame(wx.Frame):
    def __init__(self, parent, id, title, size):
        # 初始化，添加控件并绑定事件
        wx.Frame.__init__(self, parent, id, title)
        self.SetSize(size)
        self.Center()
        self.chatFrame = wx.TextCtrl(
            self, pos=(5, 5), size=(490, 310), style=wx.TE_MULTILINE | wx.TE_READONLY
        )
        self.message = wx.TextCtrl(self, pos=(5, 320), size=(300, 25))
        self.sendButton = wx.Button(self, label="发送", pos=(310, 320), size=(58, 25))
        self.usersButton = wx.Button(self, label="在线用户", pos=(373, 320), size=(58, 25))
        self.closeButton = wx.Button(self, label="关闭", pos=(436, 320), size=(58, 25))
        # 发送按钮绑定发送消息方法
        self.sendButton.Bind(wx.EVT_BUTTON, self.send)
        # Users按钮绑定获取在线用户数量方法
        self.usersButton.Bind(wx.EVT_BUTTON, self.lookUsers)
        # 关闭按钮绑定关闭方法
        self.closeButton.Bind(wx.EVT_BUTTON, self.close)
        thread.start_new_thread(self.receive, ())
        self.Show()

    def send(self, event):
        # 发送消息
        message = str(self.message.GetLineText(0)).strip()
        if message != "":
            con.write(("say " + message + "\n").encode("utf-8"))
            self.message.Clear()

    def lookUsers(self, event):
        # 查看当前在线用户
        con.write(b"look\n")

    def close(self, event):
        # 关闭窗口
        con.write(b"logout\n")
        con.close()
        self.Close()

    def receive(self):
        # 接受服务器的消息
        while True:
            sleep(0.6)
            result = con.read_very_eager()
            if result != "":
                self.chatFrame.AppendText(result)


if __name__ == "__main__":
    app = wx.App()
    con = telnetlib.Telnet()
    LoginFrame(None, -1, title="登录", size=(320, 250))
    app.MainLoop()
