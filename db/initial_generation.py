# 生成初始管理员的信息
import os
import sys
import shelve
sys.path.insert(0, os.path.dirname(os.getcwd()))
from core import Manager
from core import Student
from core import Teacher


def initial_generation():
    # manager_black = Manager.Manager('black', 'high', 'male')     # 初始化
    # manager_john = Manager.Manager('john', 'medium', 'male')
    # print(manager_black, manager_john)

    # teacher_alex = Teacher.Teacher('alex', ['Python', 'Linux'])
    # student_zero = Student.Student('zero', '16')
    # school_Beijing = Teacher.School('Beijing')
    # school_Beijing.course.append("course_python")
    # school_Beijing.course.append("course_linux")
    # school_Shanghai = Teacher.School('Shanghai')
    # school_Shanghai.course.append("course_go")
    # school_Shanghai.course.append("course_chinese")

    # course_python = Teacher.Course('python', '2周', '4000元')
    # course_python.school.append('school_Beijing')
    # course_linux = Teacher.Course('linux', '4周', '6000元')
    # course_linux.school.append('school_Beijing')
    # course_go = Teacher.Course('go', '7周', '10000元')
    # course_go.school.append('school_Shanghai')
    # course_chinese = Teacher.Course('chinese', '3周', '3000元')
    # course_chinese.school.append('school_Shanghai')

    # classes_rocket = Teacher.Classes('rocket')
    # classes_rocket.school.append('school_Beijing')

    # operating_object = shelve.open('manager_object')      # 利用shelve序列化
    # operating_object['manager_black'] = manager_black
    # operating_object['manager_john'] = manager_john
    # operating_object.close()

    # operating_object = shelve.open('school_object')      # 利用shelve序列化
    # operating_object['school_Beijing'] = school_Beijing
    # operating_object['school_Shanghai'] = school_Shanghai
    # operating_object.close()

    # operating_object = shelve.open('course_object')      # 利用shelve序列化
    # operating_object['course_python'] = course_python
    # operating_object['course_linux'] = course_linux
    # operating_object['course_go'] = course_go
    # operating_object['course_chinese'] = course_chinese
    # operating_object.close()

    # operating_object = shelve.open('classes_object')      # 利用shelve序列化
    # operating_object['classes_rocket'] = classes_rocket
    # operating_object.close()

    # operating_object = shelve.open('teacher_object')      # 利用shelve序列化
    # operating_object['teacher_alex'] = teacher_alex
    # operating_object.close()

    # operating_object = shelve.open('student_object')      # 利用shelve序列化
    # operating_object['student_zero'] = student_zero
    # operating_object.close()
    pass


if __name__ == '__main__':
    # initial_generation()
    operating_object = shelve.open('course_object')

    del operating_object['classes_10888']
    operating_object.close()
    # for i in operating_object:
    #     print(i, 'hahaha:', operating_object[i])
    #     for j in operating_object[i].__dict__:
    #         print(j, 'jejejejeje', operating_object[i].__dict__[j])
    # operating_object.close()

    # a = operating_object['school_Beijing']
    # a.course = ['python', 'linux']
    # operating_object['school_Beijing'] = a
    # print(operating_object['school_Beijing'].course)
    # #
    # del a.j
    # operating_object['school_Shanghai'] = a


    # a = operating_object['school_Shanghai']
    # a.course = ['go', 'chinese']
    # operating_object['school_Shanghai'] = a
    # operating_object.close()

    # a = operating_object['course_chinese']
    # a.school = ['Shanghai']
    # operating_object['course_chinese'] = a
    # print(operating_object['course_chinese'].school)