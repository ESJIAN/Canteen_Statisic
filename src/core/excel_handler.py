# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 19:34
# @Author  : ESJIAN
# @Email   : esjian@outlook.com
# @File    : excel_handler.py
# @Software: VsCode

import pandas as pd

def store_single_entry_to_excel(data, file_path):
    """
    将单条目的数据存储到excel表格中
    :param data: 要存储的字典数据
    :param file_path: 存储的文件路径
    :return: None
    """

    if isinstance(data, dict):
        # 确保字典的值是列表
        for key, value in data.items():
            if not isinstance(value, list):
                data[key] = [value]  # 转换为列表
    elif isinstance(data, list):
        # 确保列表的每个元素是列表
        if not all(isinstance(row, list) for row in data):
            raise ValueError("列表的每个元素必须是列表")
    else:
        raise ValueError("数据必须是字典或列表")    
    
    # 创建 DataFrame 对象
    temp_manual_input_data = pd.DataFrame(data)

    if not temp_manual_input_data.empty:
        # 将数据存储到Excel文件中
        temp_manual_input_data.to_excel(file_path, index=False)
        print("数据已成功存储到Excel文件中。")
    else:
        print("数据为空，无法存储到Excel文件中。")

# TODO:
# - [x] 修复数据存储到Excel文件中的报错:ValueError: If using all scalar values, you must pass an index
# - [X] 实现以相对路径的方式存储表格到指定目录

