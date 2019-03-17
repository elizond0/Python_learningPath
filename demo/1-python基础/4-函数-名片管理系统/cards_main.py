# 名片管理系统 主界面
import cards_tools

while True:
    # 显示功能菜单
    cards_tools.show_menu()

    # 用户输入操作代码
    action_str = input('请选择希望执行的操作:')
    print('您选择的操作是【%s】' % action_str)

    # 1,2,3 针对名片的操作；0 退出系统
    # 其他内容提示输入错误
    if action_str in ['1', '2', '3']:
        # 新增名片
        if action_str == '1':
            cards_tools.create_card()
            pass
        # 显示全部
        elif action_str == '2':
            cards_tools.show_all()
            pass
        # 查询名片
        elif action_str == '3':
            cards_tools.search_card()
            pass

        pass
    elif action_str == '0':
        print('欢迎再次使用【名片管理系统1】，再见！')
        break
    else:
        print('您输入的不正确，请重新选择')
