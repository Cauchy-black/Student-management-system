#       在有组合，需要互相链接的情况下，其实若是一个东西，只需要两两连接起来就可以了，一个链接多个
# 的时候用组合，一个链接特别多个的时候可以写成文件，然后对象为一个指向文件的链接就好拉
import shelve
from collections import OrderedDict
from conf import config
from core import Manager


count = 0     # 定义全局变量，来防止login次数过多
# count_main = 0     # 定义全局变量，来防止main次数过多
count_slt_num = 0


def choice_continue(operating_object):
    letter_selected = input('进入选择操作项目请输入c，返回登陆界面请输入b，输入其它将直接退出！')
    if letter_selected == 'c':
        return select_number(operating_object)
    elif letter_selected == 'b':
        return main()  # 重新进入，注意将3次自动退出写上，否则迭代太多次，不太好
    else:
        exit("再见~已经退出~！")


def select_number(operating_object):
    global count_slt_num
    count_slt_num += 1

    if count_slt_num >= 30:
        exit('选择次数太多，再见！')

    menu_ordered = OrderedDict(operating_object.menu)
    list_transfer = []
    print(menu_ordered)
    for i, j in enumerate(menu_ordered):
        print(i+1, '、', j)
        list_transfer.append(j)
    number_selected = input("请选择你要进行的操作，输入序号！")
    if number_selected.isdigit():
        if 0 < int(number_selected) <= len(menu_ordered.items()):                  # 创建讲师账号

            return getattr(operating_object, menu_ordered[list_transfer[int(number_selected)-1]])()
        else:
            print('输入数字不存在！')
            return choice_continue(operating_object)
    else:
        print("请输入数字！")
        return choice_continue(operating_object)


def read_self_object(user_info):   # 将输入的姓名的 文件全部导出
    address = config.manager_address
    # print(address)
    address = address+'\\' + user_info[1] + '_' + 'object'      # 找到储存管理员对象的地址
    # print(address)

    file_object = shelve.open(address)   # 实例化对象的调用
    # print(operating_object[manager_info[1]+'_'+manager_info[0]].level)
    operating_object = file_object[user_info[1]+'_' + user_info[0]]     # 将对象 赋值
    file_object.close()
    return operating_object


def second_main(user_info):    # 提取出实例化对象
    operating_object = read_self_object(user_info)  # 读取该人的实例对象

    print('您的资料如下:')
    for i in operating_object.__dict__:
        print(i, ':', operating_object.__dict__[i])

    info = """
请选择你要进行的操作！输入序号~"""
    print(info)
    return operating_object  # 将实例对象往下传
                                            #


def continue_login():
    global count
    if count >= 3:
        exit("次数超过3次，你被拉黑，再见！")
    else:
        info = """
q：退出 任意键：继续"""
        a = input(info)
        if a == 'q':
            exit()
        else:
            return login()


def judge_user(user_info, name, password):
    if user_info[0] == name:
        if user_info[1] == password:
            print("用户名及密码正确！")
            return user_info[0], user_info[2]
        else:
            print("密码错误，请重新输入！")
            return 0
    else:
        return 1


def login():   # 返回值为元组（姓名，职业）
    """
    登陆函数，应该先到conf.config文件中读取userinfo的文件路径
    应该读取userinfo文件中的信息，对用户名和密码进行查验，
    登陆成功后，查看这个人的身份，来确定进入哪一个视图
    :return:
    """
    global count
    count += 1
    # print(count)
    name = input("请输入你的姓名：")
    password = input("请输入你的密码：")
    path = config.config
    with open(path, 'r', encoding='utf-8') as f1:
        for i in f1:
            user_info = i.strip().split('|')
            member = judge_user(user_info, name, password)
            if member == 0:
                return continue_login()
            elif member == 1:
                pass
            else:
                return member
        else:
            print("用户名不存在，请重新输入！")
            return continue_login()


def main():
    """
    打印欢迎信息，
    login   用上三次登陆什么的，三次不行就不让登陆了？？？？去前面找找
    login    得到返回值，用户的姓名和身份
    打印用户身份对应的功能菜单(并不是所有函数都要写在这儿，可以写到相应的类里面)
    #如果对象想要调用任何方法，应该通过角色对象调用.跳转到对应对象的方法里面了
    :return:
    """
    # global count_main
    # count_main += 1
    # if count_main >= 5:
    #     exit('重启次数过多，再见！')
    # print(login())
    user_info = login()     # 姓名和身份以元组的方式传递
    # print(user_info)

    print("恭喜%s %s登陆成功！" % (user_info[1], user_info[0]))
    operating_object = second_main(user_info)    # 开始以此身份（如管理员）登陆，进入类，并可选择函数
    # 返回值为登陆成员的实例化对象
    print(operating_object)
    while True:
        operating_object = choice_continue(operating_object)    # 返回值为各个对象的返回值，将
                                                  # 实例化的对象继续返回回来



