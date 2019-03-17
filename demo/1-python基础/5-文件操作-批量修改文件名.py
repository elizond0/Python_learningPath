# 批量重命名
import os


def file_name_handler():
    folder_path = 'testDir'
    # folder_path=input("请输入需要批量重命名的文件夹路径：")
    folder_list = os.listdir(folder_path)  # 获取文件列表
    custom_prefix = '文件前缀-'  # 自定义前缀
    custom_suffix = '.txt'  # 自定义后缀
    block_str = 'gitignore'
    # os.chdir(folder_path) # 更改操作路径
    # print(os.getcwd()) # 当前操作的绝对路径
    number = 0
    for name in folder_list:
        if name.find(custom_prefix) > -1:
            continue  # 如果要添加的前缀已经存在，则不进行追加
        # print(name.find(custom_prefix))
        if name.find(block_str) > -1:
            continue  # 如果是gitignore文件则不进行操作

        number += 1
        old_file_path = folder_path + '/' + name
        new_file_path = folder_path + '/' + custom_prefix + str(number) + name + custom_suffix

        # print(old_file_path,new_file_path)
        os.rename(old_file_path, new_file_path)


file_name_handler()
