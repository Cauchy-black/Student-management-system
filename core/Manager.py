# 创建管理员类
from collections import OrderedDict
from core import main
import shelve
from conf import config
from core import Teacher
from core import Student

count_num = 0
count_num2 = 0
#
# def choiced_continue(listofdel):  # 所有需要选择的函数的控制
#     letter_selected = input('进入选择删除项请输入c，进入选择操作项目请输入b，输入其它将直接退出！')
#     if letter_selected == 'c':
#         return select_number(listofdel)
#     elif letter_selected == 'b':
#         pass
#     else:
#         exit("再见~已经退出~！")
#
#
# def selected_number(listofdel):  # 所有函数的选择函数
#     global count_num
#     count_num += 1
#
#     if count_num >= 20:
#         exit('选择次数太多，再见！')
#
#     list_transfer = []
#     print(listofdel)
#     for i, j in enumerate(listofdel):
#         print(i + 1, '、', j)
#         list_transfer.append(j)
#     number_selected = input("请选择你要进行的操作，输入序号！")
#     if number_selected.isdigit():
#         if 0 < int(number_selected) <= len(listofdel.items()):  # 创建讲师账号
#             # print(listofdel[list_transfer[int(number_selected) - 1]])
#             del_name = input("请输入你要删除的人的名称！")
#             if del_name == self.name:
#                 print("无法删除本人！")
#                 return choice_continue(listofdel)
#             else:
#                 del_stored_obj(listofdel[list_transfer[int(number_selected) - 1]], del_name)  # 传递，要删除的字符（如class）
#                 del_user_info(del_name)  # 删除user_info里面的东西
#
#         else:
#             print('输入数字不存在！')
#             return choice_continue(listofdel)
#     else:
#         print("请输入数字！")
#         return choice_continue(listofdel)


# def ins_object(user_info):   # 将输入的姓名的 文件全部导出
# #     # 首先进行实例化
# #     teacher_object = Teacher.Teacher(user_info[0])
# #
# #     # 对实例化对象进行储存
# #     address = config.manager_address
# #     # print(address)
# #     address = address+'\\' + user_info[1] + '_' + 'object'      # 找到储存管理员对象的地址
# #     # print(address)
# #     file_object = shelve.open(address)   # 实例化对象的调用
# #     # print(operating_object[manager_info[1]+'_'+manager_info[0]].level)
# #     file_object[user_info[1]+'_' + user_info[0]] = teacher_object   # 储存成功
# #     file_object.close()

# count_slt_num = 0
#
#
# def read_self_object(manager_info):   # 将输入的姓名的 文件全部导出
#     address = config.manager_address
#     # print(address)
#     address = address+'\\' + manager_info[1] + '_' + 'object'      # 找到储存管理员对象的地址
#     # print(address)
#     operating_object = shelve.open(address)
#     # print(operating_object[manager_info[1]+'_'+manager_info[0]].level)
#     manager_object = operating_object[manager_info[1]+'_'+manager_info[0]]     # 将对象 赋值
#     operating_object.close()
#     return manager_object
#
#
# def choice_continue(manager_object):
#     letter_selected = input('重新选择请输入c，返回登陆界面请输入b，输入其它将直接退出！')
#     if letter_selected == 'c':
#         return select_number(manager_object)
#     elif letter_selected == 'b':
#         return main.main()  # 重新进入，注意将3次自动退出写上，否则迭代太多次，不太好
#     else:
#         exit("再见~已经退出~！")
#
#
# def select_number(manager_object):
#     global count_slt_num
#     count_slt_num += 1
#
#     if count_slt_num >= 4:
#         exit('选择次数太多，再见！')
#
#     menu_ordered = OrderedDict(Manager.menu)
#     for i, j in menu_ordered.items():
#         print(j, '、', i)
#     number_selected = input("请选择你要进行的操作，输入序号！")
#     if number_selected.isdigit():
#         if int(number_selected) == 1:                  # 创建讲师账号
#             return manager_object.creatTeacher()
#         elif int(number_selected) == 2:
#             pass
#         elif int(number_selected) == 3:
#             pass
#         elif int(number_selected) == 4:
#             pass
#         elif int(number_selected) == 5:
#             pass
#         elif int(number_selected) == 6:
#             pass
#         else:
#             print('输入数字不存在！')
#             return choice_continue(manager_object)
#     else:
#         print("请输入数字！")
#         return choice_continue(manager_object)
#
#
# def manager_main(manager_info):     # 进入到管理员界面
#     # print(manager_info)
#     manager_object = read_self_object(manager_info)     # 读取该人的实例对象
#
#     print('您的资料如下:')
#     for i in manager_object.__dict__:
#         print(i, ':', manager_object.__dict__[i])
#
#     info = """
# 请选择你要进行的操作！输入序号~"""
#     print(info)
#     return select_number(manager_object)     # 将实例对象往下传


class Manager:
    """
    在属性的创建时，不仅仅只是管理员自己的属性，如姓名什么的，还应该有对于操作有帮助的
    也可以作为属性放在类中，如操作菜单，每个管理员都通用所以以静态属性的方式放在类中。
    """
    menu = {    # 一般的菜单用字典来储存
        '创建讲师账号': "creatTeacher",
        '创建学生账号': "creatStudent",
        '创建新管理员账号': "creatManager",
        '创建课程': "creatCourse",
        '创建班级': "creatClasses",
        '为班级添加课程': "bound_cour_clas",
        '为班级添加老师': "bound_teac_clas",
        '删除对象': 'del_obj',
        '展示学校信息': 'showSchool'
    }

    def __init__(self, name, level, gender):
        self.name = name
        self.level = level     # 管理员的级别，分为 high medium low
        self.gender = gender   # 管理员的性别

    def check(self, shuxing, list_element):       # 对对应的shelve文件进行查重，排除掉已经删除的地方
        if isinstance(list_element, list):
            file_object = self.open_shelve(shuxing)
            list_presense = []
            for i in file_object:
                list_presense.append(i.split('_')[1])
            for j in list_element:
                if j in list_presense:
                    pass
                else:
                    list_element.remove(j)
            file_object.close()
        else:
            pass
        return list_element

    def extract_view(self, file_object, attrib):    # 输入要选择的文件，以及文件中储存的对象的某一个属性，将其展示
             # 并且返回要选择的这个值,并且关掉要文件。
        list_file = []
        u = 0
        for i in file_object:
            u += 1
            print(u, '、', getattr(file_object[i], attrib))
            list_file.append(getattr(file_object[i], attrib))
        number_selected = input("请选择你要进行的操作，输入序号！")
        if number_selected.isdigit():
            if 0 < int(number_selected) <= len(list_file):  # 创建讲师账号
                file_object.close()
                return list_file[int(number_selected)-1]
            else:
                print('输入数字不存在！')
                return self.extract_view(file_object, attrib)
        else:
            print("请输入数字！")
            return self.extract_view(file_object, attrib)

    def choiced_continue(self, dict_object):  # 所有需要选择的函数的控制
        letter_selected = input('进入选择项请输入c，进入选择操作项目请输入b，输入其它将直接退出！')
        if letter_selected == 'c':
            return self.selected_number(dict_object)
        elif letter_selected == 'b':
            pass
        else:
            exit("再见~已经退出~！")

    def selected_number(self, dict_object):  # 所有函数的选择函数
        # dict_object需要时 有序字典  在传入时要搞好
        global count_num2
        count_num2 += 1

        if count_num2 >= 20:
            exit('选择次数太多，再见！')

        list_transfer = []
        print(dict_object)
        for i, j in enumerate(dict_object):
            print(i + 1, '、', j)
            list_transfer.append(j)
        number_selected = input("请选择你要进行的操作，输入序号！")
        if number_selected.isdigit():
            if 0 < int(number_selected) <= len(dict_object.items()):
                # print(listofdel[list_transfer[int(number_selected) - 1]])
                del_name = input("请输入你要删除的人的名称！")
            else:
                print('输入数字不存在！')
                return self.choiced_continue(dict_object)
        else:
            print("请输入数字！")
            return self.choiced_continue(dict_object)

    def add_shelve(self, userinfo, file_object, career_object):         # 添加进shelve
        file_object[userinfo[1] + '_' + userinfo[0]] = career_object  # 储存成功
        print("添加成功！")
        file_object.close()

    # def delete_shelve(self):    # 在后面统一写了删除，这里不写
    #     pass

    def modify_shelve(self):      # 修改shelve
        pass

    def view_shelve(self):         # 查看shelve
        pass

    def open_shelve(self, career):  # 将输入的姓名的 文件全部导出
        # 首先进行实例化
        # teacher_object = Teacher.Teacher(userinfo[0])

        # 对实例化对象进行储存
        ins_address = config.manager_address
        # print(address)
        ins_address = ins_address + '\\' + career + '_' + 'object'  # 找到储存管理员对象的地址
        # print(address)
        file_object = shelve.open(ins_address)  # 实例化对象的调用
        # print(operating_object[manager_info[1]+'_'+manager_info[0]].level)
        return file_object

        # file_object[userinfo[1] + '_' + userinfo[0]] = teacher_object  # 储存成功
        # print("添加成功！")
        # file_object.close()

    def creatTeacher(self):
        """
        当出现重复的姓名时，是会自动储存为第二个名字，所以不允许名字重复
        :return:
        """
        # def ins_object(userinfo):  # 将输入的姓名的 文件全部导出
        #     # 首先进行实例化
        #     teacher_object = Teacher.Teacher(userinfo[0])
        #
        #     # 对实例化对象进行储存
        #     ins_address = config.manager_address
        #     # print(address)
        #     ins_address = ins_address + '\\' + userinfo[1] + '_' + 'object'  # 找到储存管理员对象的地址
        #     # print(address)
        #     file_object = shelve.open(ins_address)  # 实例化对象的调用
        #     # print(operating_object[manager_info[1]+'_'+manager_info[0]].level)
        #     file_object[userinfo[1] + '_' + userinfo[0]] = teacher_object  # 储存成功
        #     print("添加成功！")
        #     file_object.close()

        name = input('请输入要创建的老师姓名：')
        password = input('请输入要创建的老师密码：')
        address = config.config
        f1 = open(address, 'r', encoding='utf-8')    # 查看原来中是否存在重名
        for i in f1:
            if name in i:
                print("此姓名存在，不可以！")
                f1.close()
                return self

        with open(address, 'a', encoding='utf-8') as f2:
            f2.write(name+'|'+password+'|'+'teacher' + '\n')

        # 将相对应的shelve文件打开
        userinfo = [name, 'teacher']
        teacher_object = Teacher.Teacher(name)          # 将老师实例化
        file_object = self.open_shelve('teacher')           # 实例化添加到系统中

        # 进行添加并将文件关闭
        self.add_shelve(userinfo, file_object, teacher_object)

        # address = config.manager_address
        # # print(address)
        # address = address + '\\' + user_info[1] + '_' + 'object'  # 找到储存管理员对象的地址
        # # print(address)
        # file_object = shelve.open(address)  # 实例化对象的调用
        # print(file_object[user_info[1]+'_'+user_info[0]].name)
        # file_object.close()
        return self
        # cycle = 0    # 控制循环计数和列表的下标
        # while True:
        #
        #     course_expert
        #     cycle += 1
        # print("创建老师成功")

    def creatStudent(self):
        """
        1、输入学生的姓名、密码、到userinfo中
        2、实例化学生的对象，用pickle进行储存
        :return:
        """
        name = input('请输入要创建的学生姓名：')
        password = input('请输入要创建的学生密码：')
        address = config.config
        f1 = open(address, 'r', encoding='utf-8')  # 查看原来中是否存在重名
        for i in f1:
            if name in i:
                print("此姓名存在，不可以！")
                f1.close()
                return self

        with open(address, 'a', encoding='utf-8') as f2:
            f2.write(name + '|' + password + '|' + 'student' + '\n')


            # 将相对应的shelve文件打开
        userinfo = [name, 'student']
        student_object = Student.Student(name)  # 将学生实例化
        file_object = self.open_shelve('student')  # 实例化添加到系统中

        # 进行添加并将文件关闭
        self.add_shelve(userinfo, file_object, student_object)
        return self

    def creatManager(self):
        name = input('请输入要创建的管理员姓名：')
        password = input('请输入要创建的管理员密码：')
        level = input('请输入要创建的管理员级别（分为high、medium、low）：')
        gender = input('请输入要创建的管理员性别（分为男、女）：')
        address = config.config
        f1 = open(address, 'r', encoding='utf-8')  # 查看原来中是否存在重名
        for i in f1:
            if name in i:
                print("此姓名存在，不可以！")
                f1.close()
                return self

        with open(address, 'a', encoding='utf-8') as f2:
            f2.write(name + '|' + password + '|' + 'manager' + '\n')

            # 将相对应的shelve文件打开
        userinfo = [name, 'manager']
        manager_object = Manager(name, level, gender)  # 将管理员实例化
        file_object = self.open_shelve('manager')  # 实例化添加到系统中

        # 进行添加并将文件关闭
        self.add_shelve(userinfo, file_object, manager_object)
        return self

    def creatCourse(self):
        """
        要用dump，dump进入course文件中
        :return:
        """
        name = input('请输入要创建的课程名称：')
        period = input('请输入要创建的课程周期：')
        price = input('请输入要创建的课程价格：')
        address = config.config2
        f1 = open(address, 'r', encoding='utf-8')  # 查看原来中是否存在重名
        for i in f1:
            if name in i:
                print("此课程存在，不可以！")
                f1.close()
                return self

        file_object1 = self.open_shelve('school')   # 将学校文件打开
        school = self.extract_view(file_object1, 'name')  # 对文件进行展示，并返回选择的‘学校’

        with open(address, 'a', encoding='utf-8') as f2:
            f2.write(name + '|' + 'course' + '\n')

        # 将相对应的shelve文件打开
        userinfo = [name, 'course']
        course_object = Teacher.Course(name, period, price)  # 将学生实例化
        course_object.school.append(school)
        file_object = self.open_shelve('course')  # 实例化添加到系统中

        # 进行添加并将文件关闭
        self.add_shelve(userinfo, file_object, course_object)

        # 后面对于相应的学校对象，也要将学校的课程这一栏添加这个东西
        file_object2 = self.open_shelve('school')  # 实例化添加到系统中
        school_object2 = file_object2['school' + '_' + school]
        school_object2.course.append(name)
        userinfo_2 = [school, 'school']
        self.add_shelve(userinfo_2, file_object2, school_object2)
        return self


    def creatClasses(self):   # 创建班级
        """
        首先：输入班级名称和学校   -----》这两个作为属性
        绑定一个学科对象，要先调用查看学科方法获取学科对象，用户选择学科，再将对象绑定到班级
        创建一个属于这个班级的文件用于存储学生信息，将文件的路径储存到班级对象中
        # *********************************************************
        此处关联的对象少，用列表放；关联的对象多，就放一个链接，专门放在文件里
        #  ********************************************************
        创建一个班级对象，（名称，学校，学科对象，讲师空列表（这个我倒觉得
        没有必要，因为可以通过班级找到，所以没有必要），学生信息所在的文件的路径，）
             dump进classes文件
        :
        """
        name = input('请输入要创建的班级名称：')

        address = config.config2
        f1 = open(address, 'r', encoding='utf-8')  # 查看原来中是否存在重名
        for i in f1:
            if name in i:
                print("此班级存在，不可以！")
                f1.close()
                return self

        file_object1 = self.open_shelve('school')  # 将学校文件打开
        school = self.extract_view(file_object1, 'name')  # 对文件进行展示，并返回选择的‘学校’

        with open(address, 'a', encoding='utf-8') as f2:
            f2.write(name + '|' + 'classes' + '\n')

        # 将相对应的shelve文件打开
        userinfo = [name, 'classes']
        classes_object = Teacher.Classes(name)  # 将学生实例化
        classes_object.school.append(school)
        file_object = self.open_shelve('classes')  # 实例化添加到系统中

        # 进行添加并将文件关闭
        self.add_shelve(userinfo, file_object, classes_object)

        # 后面对于相应的学校对象，也要将学校的班级这一栏添加这个东西
        file_object2 = self.open_shelve('school')  # 实例化添加到系统中
        school_object2 = file_object2['school' + '_' + school]
        school_object2.classes.append(name)
        userinfo_2 = [school, 'school']
        self.add_shelve(userinfo_2, file_object2, school_object2)
        return self


    def showClasses(self):
        """
        打开文件
        将文件中的班级对象读出来，展示
        :return:
        """
        return self

    def showSchool(self):
        operating_object = self.open_shelve('school')
        for i in operating_object:
            # print(i, 'hahaha:', operating_object[i])
            for j in operating_object[i].__dict__:
                # print(j, ':', operating_object[i].__dict__[j])
                list_element = self.check(j, operating_object[i].__dict__[j])
                a = operating_object[i]
                a.__dict__[j] = list_element
                operating_object[i] = a
                print(j, ':', list_element)
        operating_object.close()
        return self

    def bound_teac_clas(self):
        print("为班级添加老师成功")
        return self



    def del_obj(self):
        """
        当出现重复的姓名时，是会自动储存为第二个名字，所以不允许名字重复
        :return:
        """
        def del_user_info(del_name):     # 将userinfo和userinfo2里面的信息进行删除
            with open(config.config, 'r', encoding='utf-8') as f2:
                line = f2.readlines()
            with open(config.config, 'w', encoding='utf-8') as f3:
                for i in line:
                    if del_name in i:
                        continue
                    f3.write(i)
            with open(config.config2, 'r', encoding='utf-8') as f3:
                line = f3.readlines()
            with open(config.config2, 'w', encoding='utf-8') as f4:
                for i in line:
                    if del_name in i:
                        continue
                    f4.write(i)

        def del_stored_obj(pass_str, del_name):
            # 对实例化对象进行储存
            ins_address = config.manager_address
            # print(address)
            ins_address = ins_address + '\\' + pass_str + '_' + 'object'  # 找到储存管理员对象的地址
            # print(address)
            file_object = shelve.open(ins_address)  # 实例化对象的调用
            # print(operating_object[manager_info[1]+'_'+manager_info[0]].level)
            try:
                del file_object[pass_str + '_' + del_name]
            except KeyError:
                print("系统中不存在！")
            else:
                print("删除成功！")
            finally:
                file_object.close()

        def choice_continue(listofdel):  # del函数中选择数字的控制
            letter_selected = input('进入选择删除项请输入c，进入选择操作项目请输入b，输入其它将直接退出！')
            if letter_selected == 'c':
                return select_number(listofdel)
            elif letter_selected == 'b':
                pass
            else:
                exit("再见~已经退出~！")

        def select_number(listofdel):  # del函数的选择函数
            global count_num
            count_num += 1

            if count_num >= 20:
                exit('选择次数太多，再见！')

            list_transfer = []
            print(listofdel)
            for i, j in enumerate(listofdel):
                print(i + 1, '、', j)
                list_transfer.append(j)
            number_selected = input("请选择你要进行的操作，输入序号！")
            if number_selected.isdigit():
                if 0 < int(number_selected) <= len(listofdel.items()):  # 创建讲师账号
                    # print(listofdel[list_transfer[int(number_selected) - 1]])
                    del_name = input("请输入你要删除的名称！")
                    if del_name == self.name:
                        print("无法删除本人！")
                        return choice_continue(listofdel)
                    else:
                        del_stored_obj(listofdel[list_transfer[int(number_selected) - 1]], del_name)   # 传递，要删除的字符（如class）
                        del_user_info(del_name)                   # 删除user_info里面的东西

                else:
                    print('输入数字不存在！')
                    return choice_continue(listofdel)
            else:
                print("请输入数字！")
                return choice_continue(listofdel)

        list_of_del = {
            "删除老师": "teacher",
            "删除管理员(首先无法删除自己)": "manager",
            "删除学生": "student",
            "删除课程": "course",
            "删除班级": "classes"
        }
        list_of_del = OrderedDict(list_of_del)
        choice_continue(list_of_del)

        return self

# 中文流程：
# 首先 以管理员的身份登陆
# 登陆话之后就应该实例化一个对应身份的对象 manager_obj = Manager()
#   *************
#   注意：只用一个变量的话，他会按顺序依次的，并不需要同时给所有变量赋值
# 　*************
# 管理员对象可以调用所有的方法



