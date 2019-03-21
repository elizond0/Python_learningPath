# 个性二维码 $ pip3 install MyQR
from MyQR import myqr

# 1. 生成标准二维码图片 qrcode.png
myqr.run("https://www.baidu.com")

# 附上myqr.run()方法参数
# 参数	含义	详细
# words	二维码指向链接	str，输入链接或者句子作为参数
# version	边长	int，控制边长，范围是1到40，数字越大边长越大,默认边长是取决于你输入的信息的长度和使用的纠错等级
# level	纠错等级	str，控制纠错水平，范围是L、M、Q、H，从左到右依次升高，默认纠错等级为'H'
# picture	结合图片	str，将QR二维码图像与一张同目录下的图片相结合，产生一张黑白图片
# colorized	颜色	bool，使产生的图片由黑白变为彩色的
# contrast	对比度	float，调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
# brightness	亮度	float，调节图片的亮度，其余用法和取值与 contrast 相同
# save_name	输出文件名	str，默认输出文件名是"qrcode.png"
# save_dir	存储位置	str，默认存储位置是当前目录

# 2. 带底色图片的二维码
myqr.run(
    words="https://www.baidu.com",
    picture="./test.jpg",
    colorized=True,
    save_name="qrcode_with_pic.png",
)

# 3. gif动态二维码
myqr.run(
    words="https://www.baidu.com",
    picture="./gakki.gif",
    colorized=True,
    save_name="qrcode_with_gif.gif",
)

# 4. myqr库简述  源码地址https://github.com/sylnsfar/qrcode/blob/master/README-cn.md
# 1 数据分析MyQR/mylibs/constan.py
# 确定编码的字符类型，按相应的字符集转换成符号字符。
# 2 数据编码MyQR/mylibs/data.py
# 将数据字符转换为位流，每8位一个码字，整体构成一个数据的码字序列。
# 3 纠错编码MyQR/mylibs/ECC.py
# 按需要将上面的码字序列分块，并根据纠错等级和分块的码字，产生纠错码字，并把纠错码字加入到数据码字序列后面，成为一个新的序列。
# 4 构造最终数据信息MyQR/mylibs/structure.py + matrix.py
# 在规格确定的条件下，将上面产生的序列按次序放入分块中，将数据转成能够画出二维码的矩阵。
# 5 生成二维码MyQR/mylibs/draw.py
# 6 合并自定义图片
# 调用了 Pillow 库读取图片操作，将新家的图片覆盖原有图片并生成

