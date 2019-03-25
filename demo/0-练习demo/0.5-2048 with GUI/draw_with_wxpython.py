# 导入wxpyhon
import wx

# 数学计算模块
import math

# 抽象基类abc，ABCMeta用于定义抽象类，abstractmethod()可被用于声明特性属性和描述器的抽象方法。。
from abc import ABCMeta, abstractmethod


# 基类-点，调用DrawLines函数时需要点位置的元组形式，因此定义了属性xy
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 模拟数字类型，减法操作时触发，返回元组包含坐标差值
    # 例如 pointA - pointB ，返回(A.x-B.x , A.y-B.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # 模拟数字类型，加法操作时触发
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # @property 装饰器相当于在init声明了一个属性xy，不定义setter方法属性就是只读
    # @xy.setter 用于配合property装饰器，用于修改属性
    @property
    def xy(self):
        return (self.x, self.y)

    # __str__定义在类内部，必须返回一个字符串类型，print(实例)，会触发执行
    # 同时定义repr和st时，print会调用str，列表以及字典等容器总是会使用repr方法
    def __str__(self):
        return "x={0},y={1}".format(self.x, self.y)

    # __repr__定义在类内部，在控制台中输入 实例，即会触发执行，不需要print
    # repr和str可以通过repr(实例)/str(实例)调用
    def __repr__(self):
        return str(self.xy)

    # 通常情况下，在类中定义的所有函数都是对象的绑定方法，对象在调用绑定方法时会自动将自己作为参数传递给方法的第一个参数。
    # 静态方法不用传入self，不能访问类属性和实例属性，一般用于工具函数
    @staticmethod
    def dist(a, b):
        # 勾股定理计算2个坐标间的直线距离
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


# 基类-多边形，形状由点组成。
# area用来代表形状的面积，不同形状有不同算法，因此用抽象函数实现，形状默认是凸闭合的形状。
# 两个多边形的比较用面积来比较。不同形状可以用不同的颜色线来画，因此加了属性color。
class Polygon(object):
    # 继承抽象基类
    __metaclass__ = ABCMeta

    def __init__(self, points_list, **kwargs):
        print(points_list)
        for point in points_list:
            # 断言：遍历点阵列表中的对象是Point的实例
            assert isinstance(point, Point), "input must be Point type"
        self.points = points_list[:]  # [a:b] 截取列表a-b下标，[:]显示所有
        self.points.append(points_list[0])  # 一笔绘制封闭图形需要最终回到起点，因此添加起点坐标
        self.color = kwargs.get("color", "#000000")  # get获取参数列表中get的值，'#000000'为默认值

    def drawPoints(self):
        points_xy = []
        for point in self.points:
            points_xy.append(point.xy)
        # print(points_xy)
        return tuple(points_xy)

    # @abstractmethod用于申明抽象类
    # 多边形不计算面积，因此raise异常
    @abstractmethod
    def area(self):
        raise ("not implement")

    # lt,le,eq,ne,gt,ge富比较方法，x<y触发lt方法，x!=y调用ne，一般约定返回bool值，实际上可以是任意值
    # 如果指定的参数没有响应的实现,富比较方法可能会返回单例对象NotImplemented
    # 比较多边形面积
    def __lt__(self, other):
        # 断言：other是多边形的实例
        assert isinstance(other, Polygon)
        return self.area < other.area


# 子类矩形
# 指定宽高，以及初始点，startPoint + Point(w, 0)会自动调用Point类中__add__方法
class RectAngle(Polygon):
    def __init__(self, startPoint, w, h, **kwargs):
        self._w = w
        self._h = h
        Polygon.__init__(
            self,
            [
                startPoint,
                startPoint + Point(w, 0),
                startPoint + Point(w, h),
                startPoint + Point(0, h),
            ],
            **kwargs
        )

    def area(self):
        return self._w * self._h

    def __str__(self):
        return "矩形"


# 子类三角形
class TriAngle(Polygon):
    def __init__(self, point_a, point_b, point_c, **kwargs):
        # 边长
        self.length_ab = Point.dist(point_a, point_b)
        self.length_bc = Point.dist(point_c, point_b)
        self.length_ac = Point.dist(point_a, point_c)
        # 半周长
        self.half_perimeter = (self.length_ab + self.length_bc + self.length_ac) / 2

        # 三角形成立的条件判定，3个坐标不在同一条直线上，任意两条边相加大于第三条
        try:
            if (
                self.length_ab + self.length_ac > self.length_bc
                and self.length_ab + self.length_ab > self.length_ac
                and self.length_bc + self.length_ac > self.length_ab
            ):
                Polygon.__init__(self, [point_a, point_b, point_c], **kwargs)
            else:
                raise ValueError()  # 手动抛出异常到except
        except ValueError:
            raise ValueError("Three points must not be on the same line")

        Polygon.__init__(self, [point_a, point_b, point_c], **kwargs)

    def area(self):
        # 面积公式 S^2=p(p-a)(p-b)(p-c) abc为变长，p为半周长
        return math.sqrt(
            self.half_perimeter
            * (self.half_perimeter - self.length_ab)
            * (self.half_perimeter - self.length_ac)
            * (self.half_perimeter - self.length_bc)
        )

    def __str__(self):
        return "三角形"


# 子类圆
# 面积公式：S=pi*r^2 pi为圆周率，r为半径
class Circle(Polygon):
    def __init__(self, centerPoint, radius, points_num, **kwargs):
        # 半径
        self.radius = radius
        # 圆心
        self.center_x = centerPoint.xy[0]
        self.center_y = centerPoint.xy[1]
        # 圆形可以看作多边形，点阵足够多的时候，就成为了圆形，points_num用于生成点阵数组
        circle_list = []
        # 2pi 为360° 获得单个点的对应弧度
        point_radian = (math.pi * 2) / points_num
        # sin=y/r，可得y坐标；cos=x/r，可得x坐标
        for num in range(points_num):
            circle_list.append(
                Point(
                    self.center_x + radius * math.cos(point_radian * num),
                    self.center_y + radius * math.sin(point_radian * num),
                )
            )
        Polygon.__init__(self, circle_list, **kwargs)

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return "圆形"


class Example(wx.Frame):
    def __init__(
        self,
        shapes,
        parent=None,
        id=-1,
        title="Example",
        size=(500, 400),
        pos=(400, 300),
    ):
        # None: 当前窗口的父窗口parent，如果当前窗口是最顶层的话，则parent=None,如果不是顶层窗口，则它的值为所属frame的名字
        # -1: id值, -1的话程序会自动产生一个id
        # title：对话框文本
        # pos: 初始位置
        # size: 宽，高大小
        # style风格参数默认：wx.MAXIMIZE_BOX| wx.MINIMIZE_BOX| wx.RESIZE_BORDER|wx.SYSTEM_MENU| wx.CAPTION| wx.CLOSE_BOX
        super(Example, self).__init__(parent, id=id, title=title, size=size, pos=pos)

        # 根据形状实例化不同的类
        self.shapes = shapes

        # 绑定渲染窗口的动作到OnPaint，resize窗口时会重新调用该函数
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        # 在界面中居中显示
        self.Center()
        # 显示frame
        self.Show()

    # 使用PaintDC绘制线条
    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        # 利用point类画直线，参数是起点的xy坐标和终点的xy坐标
        # dc.DrawLine(50, 60, 190, 100)
        # dc.DrawLines(((20, 60), (100, 60), (100, 10), (20, 10), (20, 60)))

        for shape in self.shapes:
            dc.SetPen(wx.Pen(shape.color))
            dc.DrawLines(shape.drawPoints())


if __name__ == "__main__":
    # 需要画的数组列表
    draw_shapes = []
    # 矩形
    start_rectAngle = Point(50, 50)
    shape_rectAngle = RectAngle(start_rectAngle, 100, 80, color="red")
    draw_shapes.append(shape_rectAngle)
    # 三角形
    start_triAngle = Point(50, 50)
    shape_triAngle = TriAngle(
        start_triAngle, Point(180, 90), Point(100, 150), color="blue"
    )
    draw_shapes.append(shape_triAngle)
    # 圆形
    start_circle = Point(150, 150)
    shape_circle = Circle(start_circle, 100, 50, color="green")
    draw_shapes.append(shape_circle)

    # 计算并打印面积
    for shape in draw_shapes:
        print("%s%s面积：%s" % (shape.color, str(shape), shape.area()))

    # 每个wxpython的程序必须有一个wx.app对象
    app = wx.App()
    # 实例化一个frame
    Example(title="draw_with_wxpython", shapes=draw_shapes)
    app.MainLoop()
