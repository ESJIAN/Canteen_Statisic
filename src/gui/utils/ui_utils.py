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


def show_error_window():
    """
    显示错误窗口
    :param: None
    :return: None
    """
    app = QApplication.instance()  # 检查是否已有 QApplication 实例
    if not app:
        app = QApplication([])  # 如果没有，则创建一个新的实例

    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    app.exec()  # 启动事件循环



def manual_temp_storage(input_fields):
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
            show_error_window()
            
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    

# Summary：
# 1. 抽象的看所有widget都是一个个的对象，都是有属性和方法的，属性就是它的状态，方法就是它能做的事情。


# TODO：
# - [ ] 实现报错弹窗功能 
#   - [ ] 修复报错弹框的闪现问题