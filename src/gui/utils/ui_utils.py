# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 1:04
# @Author  : ESJIAN
# @Email   : esjian@outlook.com
# @File    : ui_utils.py
# @Software: VsCode

TOTAL_FIELD_NUMBER = 8  # 总字段所具有的TAG数

import sys
from datetime import datetime
from email.mime import application
from PySide6.QtWidgets import QApplication, QWidget  

from src.gui.error_window import TagNumShortage # Learning1：子模块的导入相对路径的起算点是主模块
from src.gui.check_window import ExcelCheckWindow  # Learning2:顶级脚本设定绝对倒入配置后不需要在子模块中重设




def get_current_date():
    """
    获取系统当前日期，格式为 YYYY-MM-DD
    :param: None
    :return: 当前日期的字符串，格式为 YYYY-MM-DD
    """
    return datetime.now().strftime("%Y-%m-%d")


def manual_temp_storage(self,input_fields):
    """
    暂存当前条目所有输入框内的信息
    :param input_fields: 输入框的字典或列表，键为字段名，值为对应的 QLineEdit 对象
    :return: 包含所有输入框内容的字典
    """
    
    exsit_tag_number=0 
    temp_storage = {}
    try:
        for field_name, input_field in input_fields.items():
            if input_field.text():  # 检查输入框是否有内容
                exsit_tag_number+=1 # 统计有内容的输入框数量
                temp_storage[field_name] = input_field.text()
        if exsit_tag_number==TOTAL_FIELD_NUMBER:
            return temp_storage
        else:
            print("Warning: Not all fields are filled.")
            show_error_window(self)
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    

def show_error_window(self):
    """
    显示错误窗口
    :param: None
    :return: None
    """

    
    if hasattr(self, 'Form') and self.PopWindowApplicationForm.isVisible():
        return  # 如果弹窗已经存在且可见，则不重复创建

    # 检验self是否有名为app的属性
    self.PopWindowApplication = QApplication.instance()
    if not self.PopWindowApplication:
        # 若没有为self追加创建一个app属性,继承自QApplication
        self.PopWindowApplication = QApplication([])
        # 为self追加创建一个Form属性,继承自QWidget
        self.PopWindowApplicationForm = QWidget()
        # 为self追加一个ui属性,继承自TagNumShortage
        self.PopWindowApplicationUi = TagNumShortage()
        #
        self.PopWindowApplicationUi.setupUi(self.PopWindowApplicationForm)
        
        self.PopWindowApplicationForm.show()
    else:
        # 为self追加创建一个Form属性,继承自QWidget
        self.PopWindowApplicationForm = QWidget()
        # 为self追加一个ui属性,继承自TagNumShortage
        self.PopWindowApplicationUi = TagNumShortage()
        #
        self.PopWindowApplicationUi.setupUi(self.PopWindowApplicationForm)
        
        self.PopWindowApplicationForm.show()


def show_check_window(self,file_path):
    """
    显示检查窗口
    :param: self,file_path
    :return: None
    """
    # 为self追加创建一个app属性,继承自QApplication
    #self.PopWindowAplication = QApplication([])  # Learning3&Fixed2:一个程序只能有一个 QApplication 实例


    # 为self追加创建一个Form属性,继承自QWidget
    self.PopWindowApplicationForm = QWidget()
    # 为self追加一个ui属性,继承自excel_check_window
    self.PopWindowApplicationUi = ExcelCheckWindow()
    # 将 ui 属性与 form 属性 
    self.PopWindowApplicationUi.setupUi(self.PopWindowApplicationForm)
    
    self.PopWindowApplicationUi.load_table_data(file_path)

    # 展示窗口
    self.PopWindowApplicationForm.show()
    


    


# Summary：
# 1. 抽象的看所有widget都是一个个的对象，都是有属性和方法的，属性就是它的状态，方法就是它能做的事情。

# Learning：
# 1. 弹窗事件循环的生命周期依赖于该调用函数的声明周期，如果该函数是一个独立的函数，那么它的生命周期就会在函数调用结束后结束，导致弹窗无法正常显示。
#    子弹窗要想和共享主窗口的声明周期，需要利用self的引用来实现。也就是在主窗口中创建子窗口的实例，并将其作为属性存储在主窗口中，这样子窗口就可以和主窗口共享生命周期了。
#    来源：Fixed1的修复
# 2. 顶级脚本设定绝对导入包配置代码后不需要在子模块中重设，因为主代码设置好的变量子代码可见
#    变量的传递分为单个文件内，和跨文件两种方式去传递
# 3. 在存在主窗口的时候，在创建子窗口时，不要创建新的QApplication实例，而是使用已经存在的实例。因为QApplication只能有一个实例，创建多个实例会导致错误。
#    来源：Fixed2的修复
# TODO：
# - [x] 2025.4.46 实现报错弹窗功能 
#   - [x] 修复报错弹框的闪现问题
# - [x] 2025.4.27 实现调用check_window.py以展示表格操作弹窗
#   - [x] 修复 RuntimeError: Please destroy the QApplication singleton before creating a new QApplication instance.
#   - [x] 修复 Excel 展示弹窗，仅弹窗但是不显示内容的问题——原因见main_window.py的Learning3
