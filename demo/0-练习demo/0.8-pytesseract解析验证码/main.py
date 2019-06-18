# 0.8-pytesseract解析验证码

# 1.安装依赖库Pillow(图像处理库)
# $ pip3 install Pillow

# 2.安装tesseract-ocr(google的ocr识别引擎)
# https://github.com/tesseract-ocr/tesseract/wiki 下载windows安装包exe，如果需要识别汉字，在安装时勾选语言包
# 安装完之后，配置环境变量，$ tesseract -v 可查看版本号
# $ tesseract [目标图片] [输出文本] [-l 语言代码] 可在cmd中进行简单操作

# 3.安装py识别引擎pytesseract https://pypi.org/project/pytesseract/0.1/
# $ pip install pytesseract

# 引入pillow图形处理库
from PIL import Image
import pytesseract


# 打开测试图片
im = Image.open("./test.png")
vcode = pytesseract.image_to_string(im)
# vcode = pytesseract.image_to_string(im, lang="chi_sim") # lang 语言

print(vcode)
# 准确度很低，[优化方案](https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality):
# 图像处理:重新缩放;二值化;去噪;旋转/纠偏;边界;透明度/Alpha通道;工具/库
# 页面分割方法
# 字典，单词列表和模式

