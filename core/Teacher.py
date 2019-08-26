class Classes:
    def __init__(self, name):  # 这里的设置和我前面想的一样，只是我想的是创建班级，然后
                                            # 再分配科目和老师，但这里是只考虑分配老师
        self.name = name    # 班级名称 python——s9
        self.school = []    # 学校
        self.course = []        # 班级科目 python linux
        self.teacher = []
        self.student = ['student_obj']  # 学生对象
# ********************************************************
# 1、这种组合对象，两者之间只需要后面那个指向前面那个就可以了，就要链表一样，首尾相连即可，后面的
#  就是指要选择的那一方
#  2、静态链接 即一开始就链接好了的 则可以直接在init函数中设定好；动态的，是由别人选择它的，则
# 不用时限写好
# 至于被链接的那个如何看有谁链接它，则稍后再做解释
#  # 注意，此处可以有重复的相关，相互连接，比如一个老师对应三门科，表示他三门科都可以上，
#         # 而一个课只对应一个老师，一门科。所以老师和课都可以指向科目，含义有少许差别。
# ********************************************************


class Course:
    def __init__(self, name, period, price):
        self.name = name           # 课程的名字
        self.period = period       # 课程周期
        self.price = price         # 课程价格
        # self.school = school       # 和课程相关的学校  初始化时导入
        self.school = []
        self.classes = []         # 和此课程相关的班级


class School:
    def __init__(self, name):
        self.name = name
        self.teacher = []
        self.classes = []
        self.course = []


class Teacher:
    """
    
    """
    menu = {    # 一般的菜单用字典来储存
        '查看班级情况': "view_classes",
        '查看学生情况': "view_student",
        '添加可上任课程': "add_available_course",
        '添加可上任学校': "add_available_school"
    }

    def __init__(self, name):
        self.name = name
        # self.classes = ['classes_obj']         # 对象的组合用法时，若相关的对象有多个，则用列表表示
        self.courses = []   # 此处指此老师会的科目,为一个数组
        # self.courses = []  # 此处指为老师分配的科目
        self.classes = []  # 指为老师指派的班级
        self.school = []  #
        # 注意，此处可以有重复的相关，相互连接，比如一个老师对应三门科，表示他三门科都可以上，
        # 而一个课只对应一个老师，一门科。所以老师和课都可以指向科目，含义有少许差别。

    def view_classes(self):
        print("查看班级成功")
        return self
    def view_student(self):
        print("查看学生成功")
        return self
    def add_available_course(self):
        print("添加课程成功")
        return self
    def add_available_school(self):
        print("添加学校成功")
        return self