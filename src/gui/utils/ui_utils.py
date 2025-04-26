# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 1:04
# @Author  : ESJIAN
# @Email   : esjian@outlook.com
# @File    : ui_utils.py
# @Software: VsCode




from datetime import datetime

def get_current_date():
    """
    获取系统当前日期，格式为 YYYY-MM-DD
    """
    return datetime.now().strftime("%Y-%m-%d")





def manual_temp_storage(input_fields):
    """
    暂存当前条目所有输入框内的信息
    :param input_fields: 输入框的字典或列表，键为字段名，值为对应的 QLineEdit 对象
    :return: 包含所有输入框内容的字典
    """
    temp_storage = {}
    for field_name, input_field in input_fields.items():
        if input_field.text():  # 检查输入框是否有内容
            temp_storage[field_name] = input_field.text()
    return temp_storage
    
    
    

# Summary：
# 1. 抽象的看所有widget都是一个个的对象，都是有属性和方法的，属性就是它的状态，方法就是它能做的事情。