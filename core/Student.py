class Student:
    menu = {    # 一般的菜单用字典来储存
        '选择班级': "choice_classes", '查看班级情况': "view_classes",
        '查看老师情况': "view_teacher"
    }

    def __init__(self, name):
        self.name = name
        self.classes = []    # 学生自主选择的班级情况

    def choice_classes(self):
        print("选择班级成功!")
        return self
    def view_classes(self):
        print("查看班级成功")
        return self
    def view_teacher(self):
        print("查看老师情况成功")
        return self