# Python 是一门带 GIL 的语言，所以在 Python 中使用多线程处理IO操作过多的任务并不是很好的选择。
# gil:全局解析器锁,作用:单核的情况下可以实现多任务(并发)
# 同时聊天服务器将同多个 socket 进行通信，所以基于 asyncore 模块实现聊天服务器。
# aysncore 模块是一个异步的 socket 处理器，通过使用该模块将大大简化异步编程的难度。
# asynchat 模块在 asyncore 模块的基础上做了进一步封装，简化了基于文本协议的通信任务的开发难度。
import asynchat
import asyncore

# 定义端口
PORT = 2333

# 定义连接断开异常类
class EndSession(Exception):
    pass


# 附录：python 常见的异常类型
# BaseException	所有异常的基类
# SystemExit	解释器请求退出
# KeyboardInterrupt	用户中断执行(通常是输入^C)
# Exception	常规错误的基类
# StopIteration	迭代器没有更多的值
# GeneratorExit	生成器(generator)发生异常来通知退出
# StandardError	所有的内建标准异常的基类
# ArithmeticError	所有数值计算错误的基类
# FloatingPointError	浮点计算错误
# OverflowError	数值运算超出最大限制
# ZeroDivisionError	除(或取模)零 (所有数据类型)
# AssertionError	断言语句失败
# AttributeError	对象没有这个属性
# EOFError	没有内建输入,到达EOF 标记
# EnvironmentError	操作系统错误的基类
# IOError	输入/输出操作失败
# OSError	操作系统错误
# WindowsError	系统调用失败
# ImportError	导入模块/对象失败
# LookupError	无效数据查询的基类
# IndexError	序列中没有此索引(index)
# KeyError	映射中没有这个键
# MemoryError	内存溢出错误(对于Python 解释器不是致命的)
# NameError	未声明/初始化对象 (没有属性)
# UnboundLocalError	访问未初始化的本地变量
# ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
# RuntimeError	一般的运行时错误
# NotImplementedError	尚未实现的方法
# SyntaxError	Python 语法错误
# IndentationError	缩进错误
# TabError	Tab 和空格混用
# SystemError	一般的解释器系统错误
# TypeError	对类型无效的操作
# ValueError	传入无效的参数
# UnicodeError	Unicode 相关的错误
# UnicodeDecodeError	Unicode 解码时的错误
# UnicodeEncodeError	Unicode 编码时错误
# UnicodeTranslateError	Unicode 转换时错误
# Warning	警告的基类
# DeprecationWarning	关于被弃用的特征的警告
# FutureWarning	关于构造将来语义会有改变的警告
# OverflowWarning	旧的关于自动提升为长整型(long)的警告
# PendingDeprecationWarning	关于特性将会被废弃的警告
# RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
# SyntaxWarning	可疑的语法的警告
# UserWarning	用户代码生成的警告


# 聊天服务器
class ChatServer(asyncore.dispatcher):
    def __init__(self, port):
        asyncore.dispatcher.__init__(self)
        # 创建socket
        self.create_socket()
        # 设置socket可重用
        self.set_reuse_addr()
        # 监听端口
        self.bind(("", port))
        self.listen(5)
        self.users = {}
        self.main_room = ChatRoom(self)

    def handle_accept(self):
        conn, addr = self.accept()
        ChatSession(self, conn)


# 客户端通信类
class ChatSession(asynchat.async_chat):
    def __init__(self, server, sock):
        asynchat.async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator(b"\n")
        self.data = []
        self.name = None
        self.enter(LoginRoom(server))

    # 进入其他房间的同时，退出当前房间
    def enter(self, room):
        try:
            cur = self.room
        except AttributeError:
            pass
        else:
            cur.remove(self)
        self.room = room
        room.add(self)

    # 接收客户端数据并收集
    def collect_incoming_data(self, data):
        self.data.append(data.decode("utf-8"))

    # 接收客戶端数据结束时
    def found_terminator(self):
        line = "".join(self.data)
        self.data = []
        try:
            self.room.handle(self, line.encode("utf-8"))
        except EndSession:
            self.handle_close()

    # session关闭时，进入logoutRoom
    def handle_close(self):
        asynchat.async_chat.handle_close(self)
        self.enter(LogoutRoom(self.server))


# 协议命令处理类
class CommandHandler(object):
    # 响应未知命令，通过asynchat.async_chat.push方法发送消息
    def unknown(self, session, cmd):
        session.push(("未知命令 {} \n".format(cmd).encode("utf-8")))

    # 命令处理
    def handle(self, session, line):
        line = line.decode()
        if not line.strip():
            return
        parts = line.split(" ", 1)
        cmd = parts[0]

        try:
            line = parts[1].strip()
        except IndexError:
            line = ""

        # 通过协议代码处理相应的方法
        method = getattr(self, "do_" + cmd, None)
        try:
            method(session, line)
        except TypeError:
            self.unknown(session, cmd)


# 房间类，继承自CommandHandler，负责处理基本的命令和广播
# 下分三种房间放置用户：登录中、聊天时、退出后
class Room(CommandHandler):
    def __init__(self, server):
        self.server = server
        self.sessions = []

    # 添加用户
    def add(self, session):
        self.sessions.append(session)

    # 移除用户
    def remove(self, session):
        self.sessions.remove(session)

    # 广播
    def broadcast(self, line):
        for session in self.sessions:
            session.push(line)

    # 退出登录
    def do_logout(self, session, line):
        raise EndSession  # 手动抛出异常


# 登录中的用户
class LoginRoom(Room):
    # 连接成功
    def add(self, session):
        Room.add(self, session)
        session.push(b"Connect Success")

    # 用户登录
    def do_login(self, session, line):
        name = line.strip()
        if not name:  # name为空
            session.push(b"UserName Empty")
        elif name in self.server.users:  # name已存在
            session.push(b"UserName Exist")
        else:
            session.name = name
            session.enter(self.server.main_room)


# 退出登录的用户
class LogoutRoom(Room):
    def add(self, session):
        try:
            del self.server.users[session.name]
        except KeyError:
            pass


# 聊天的房间
class ChatRoom(Room):
    # 广播新用户进入
    def add(self, session):
        # b"Login Success" sesssion会推送名为Login Susscess的消息给客户端，客户端接收到之后进行相应操作
        session.push(b"Login Success")
        self.broadcast((session.name + " 进入房间.\n").encode("utf-8"))
        self.server.users[session.name] = session
        Room.add(self, session)

    # 广播用户离开
    def remove(self, session):
        Room.remove(self, session)
        self.broadcast((session.name + " 离开房间.\n").encode("utf-8"))

    # 客户端发送消息
    def do_say(self, session, line):
        self.broadcast((session.name + ": " + line + "\n").encode("utf-8"))

    # 查看在线用户
    def do_look(self, session, line):
        session.push(b"Online Users:\n")
        for other in self.sessions:
            session.push((other.name + "\n").encode("utf-8"))


if __name__ == "__main__":
    s = ChatServer(PORT)
    try:
        print('服务运行于 "127.0.0.1:{0}"'.format(PORT))
        asyncore.loop()
    except KeyboardInterrupt:
        print("服务关闭")

