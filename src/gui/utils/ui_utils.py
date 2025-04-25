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