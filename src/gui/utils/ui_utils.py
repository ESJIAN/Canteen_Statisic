# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 1:04
# @Author  : ESJIAN
# @Email   : esjian@outlook.com
# @File    : ui_utils.py
# @Software: VsCode

TOTAL_FIELD_NUMBER = 8  # 总字段所具有的TAG数


from datetime import datetime
from email.mime import application
from PySide6.QtWidgets import QApplication, QWidget  

from error_window import Ui_Form




def get_current_date():
    """
    获取系统当前日期，格式为 YYYY-MM-DD
    :param: None
    :return: 当前日期的字符串，格式为 YYYY-MM-DD
    """
    return datetime.now().strftime("%Y-%m-%d")


def show_error_window(self):
    """
    显示错误窗口
    :param: None
    :return: None
    """
    self.app = QApplication.instance()  # 检查是否已有 QApplication 实例
    if not self.app:
        self.app = QApplication([])  # 如果没有，则创建一个新的实例

    self.Form = QWidget()
    self.ui = Ui_Form()
    self.ui.setupUi(self.Form)
    self.Form.show()
    self.app.exec()  # Fixed1：若不加入self参数该独立事件的循环会导致窗口关闭后，程序无法继续执行，造成窗口闪现现象。



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
            print("Error: Not all fields are filled.")
            show_error_window(self)
            
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    



    

# Summary：
# 1. 抽象的看所有widget都是一个个的对象，都是有属性和方法的，属性就是它的状态，方法就是它能做的事情。

# Learning：
# 1. 弹窗事件循环的生命周期依赖于该调用函数的声明周期，如果该函数是一个独立的函数，那么它的生命周期就会在函数调用结束后结束，导致弹窗无法正常显示。
# 2. 子弹窗要想和共享主窗口的声明周期，需要利用self的引用来实现。也就是在主窗口中创建子窗口的实例，并将其作为属性存储在主窗口中，这样子窗口就可以和主窗口共享生命周期了。
#    来源：Fixed1的修复

# TODO：
# - [x] 2025.4.46 实现报错弹窗功能 
#   - [x] 修复报错弹框的闪现问题