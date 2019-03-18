# 名片管理系统 工具集合
# 记录所有名片的列表容器
card_list = [{'name': 'a',
              'age': '16',
              'gender': '男',
              'phone': '150', }]


# 显示菜单
def show_menu():
    print("*" * 60)
    print('欢迎使用【名片管理系统】V 1.0')
    print('')
    print('1. 新增名片')
    print('2. 显示全部')
    print('3. 查询名片')
    print('')
    print('0. 退出系统')
    print("*" * 60)


# 新增名片
def create_card():
    print('- ' * 30)
    print('功能：新增名片')

    # 记录用户输入的个人信息
    name_str = input('请输入姓名：')
    age_str = input('请输入年龄：')
    gender_str = input('请输入性别：')
    phone_str = input('请输入电话：')

    card_dict = {
        'name': name_str,
        'age': age_str,
        'gender': gender_str,
        'phone': phone_str,
    }

    # 将数据添加到数据容器中
    card_list.append(card_dict)

    print('%s名片新建完成！' % name_str)


# 显示全部
def show_all():
    # 如果没有名片则返回
    if len(card_list) < 1:
        print('没有名片记录')
        return

    print('- ' * 30)
    print('功能：显示所有名片')
    for name in ['姓名', '年龄', '性别', '电话']:
        print(name, end='\t\t')
    print('')
    print('=' * 60)
    for card_dict in card_list:
        print(
            '%s\t\t%s\t\t%s\t\t%s' % (card_dict['name'], card_dict['age'], card_dict['gender'], card_dict['phone']))


# 查询名片
def search_card():
    print('- ' * 30)
    print('功能：查询名片')

    # 提示输入要搜索的姓名，遍历名片列表，查询要搜索的姓名
    find_name = input('请输入要搜索的姓名：')
    for card_dict in card_list:
        if card_dict['name'] == find_name:
            for name in ['姓名', '年龄', '性别', '电话']:
                print(name, end='\t\t')
            print('')
            print('=' * 60)
            print(
                '%s\t\t%s\t\t%s\t\t%s' % (
                    card_dict['name'], card_dict['age'], card_dict['gender'], card_dict['phone']))

            deal_card(card_dict)
            break

    else:  # else在此处表示等待所有for循环结束后没有查询到且没有break的情况
        print('抱歉，没有查询到%s名片' % find_name)


# 处理名片
def deal_card(fina_dict):
    action_str = input('请输入对名片的操作：【1】 修改，【2】 删除，【3】 返回上层菜单：')
    # 修改名片
    if action_str == '1':
        modify_card(fina_dict)
    # 删除名片
    elif action_str == '2':
        del_card(fina_dict)
    # 返回，默认返回上层，因此不需要判断。


# 删除名片
def del_card(find_dict):
    card_list.remove(find_dict)
    print('删除名片成功！')


# 修改名片
def modify_card(find_dict):
    find_dict['name'] = input_card_handler(find_dict['name'], '姓名：')
    find_dict['age'] = input_card_handler(find_dict['age'], '年龄：')
    find_dict['gender'] = input_card_handler(find_dict['gender'], '性别：')
    find_dict['phone'] = input_card_handler(find_dict['phone'], '电话：')
    print('修改名片成功！')


# 判断用户输入内容是否为空
def input_card_handler(dict_value, tip_message):
    result = input(tip_message)
    if len(result) > 0:
        return result
    else:
        return dict_value
