# -*- coding: utf-8 -*-
# @Time    : 2025/4/26 19:34
# @Author  : ESJIAN
# @Email   : esjian@outlook.com
# @File    : excel_handler.py
# @Software: VsCode



from openpyxl import load_workbook
from datetime import datetime

import os
import pandas as pd
import __main__
import xlrd
from xlutils.copy import copy
def store_single_entry_to_temple_excel(data, file_path):
    """
    将单条目的数据追加存储到临时excel表格中
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
        try:
            # 检查文件是否存在，存在则追加，不存在则新建
            if os.path.exists(file_path):
                # 读取原有数据
                existing_df = pd.read_excel(file_path)
                # 追加新数据
                combined_df = pd.concat([existing_df, temp_manual_input_data], ignore_index=True)
                combined_df.to_excel(file_path, index=False)
            else:
                # 文件不存在，直接写入
                temp_manual_input_data.to_excel(file_path, index=False)
            print("数据已成功追加存储到Excel文件中。")
        except Exception as e:
            print(f"写入Excel文件时出错: {e}")
    else:
        print("数据为空，无法存储到Excel文件中。")

def clear_temp_excel():
    """
    清空暂存的 Excel 表格内容
    :param: None
    :return: None
    """
    # 只保留表头，清空内容
    try:
        if os.path.exists(__main__.TEMP_SINGLE_STORAGE_EXCEL_PATH):
            df = pd.read_excel(__main__.TEMP_SINGLE_STORAGE_EXCEL_PATH)
            empty_df = df.iloc[0:0]
            empty_df.to_excel(__main__.TEMP_SINGLE_STORAGE_EXCEL_PATH, index=False)
    except Exception as e:
        print(f"清空暂存表格时出错: {e}")


def cmmit_data_to_storage_excel(excel_file_path):
    """
    提交暂存 Excel 数据到主表、副表 Excel 文件
    :param: temp_excel_file: 要存储的暂存表
    """
    # 读取暂存表格数据
    try:
        # 打开工作簿
        temp_storage_workbook = xlrd.open_workbook(__main__.TEMP_SINGLE_STORAGE_EXCEL_PATH)
    except Exception as e:
        print(f"Error: {e}")
        return
    
    # 读取主工作表格数据
    try:
        # 打开工作簿
        main_workbook = xlrd.open_workbook(excel_file_path, formatting_info=True)
        # 创建可写副本
        main_workbook_copy = copy(main_workbook)  
        print(f"Notice: 工作表加载成功，文件路径: {excel_file_path}")
    except Exception as e:
        print(f"Error: {e}")
        return

    # 轮询读取暂存表格数据行
    for row_index in range(1, temp_storage_workbook.sheet_by_index(0).nrows):
        # 读取行数据
        row_data = temp_storage_workbook.sheet_by_index(0).row_values(row_index)
        # 获取行数据中的公司名称
        company_name = row_data["公司"]
        # 获取行数据中的金额
        amount = row_data["金额"]
        # 打开主表公司worksheet，追加金额数据
        try:
            corporation_worksheet = main_workbook_copy.sheet_by_name(company_name)
            # 访问8，D单元格
            cell = corporation_worksheet.cell(row=8, column=4)  
            # 获取当前单元格的值
            current_value = cell.value
            # 如果当前单元格的值是数字，则进行累加
            if isinstance(current_value, (int, float)):
                new_value = current_value + amount
            else:
                new_value = amount  # 如果不是数字，则直接使用新的金额
            # 更新单元格的值
            cell.value = new_value
            # 保存工作簿
            main_workbook_copy.save(excel_file_path)
            
        except Exception as e:
            print(f"Error: {e}")
            continue



    # 打开主表公司worksheet
    corporation_worksheet = main_workbook_copy.sheet_by_index(0)

   
   

# Learning:
# 1. Openpyxl 不对 .xls 文件格式提供支持，只能对 .xlsx 文件格式提供支持


# TODO:
# - [x] 修复数据存储到Excel文件中的报错:ValueError: If using all scalar values, you must pass an index
# - [X] 实现以相对路径的方式存储表格到指定目录
# - [x] 2025.4.30 实现追加写入表格的行逻辑
# - [ ] 2025.5.1 实现数据提交到主表、副表Excel文件的功能
#   - [x] 修复Error: openpyxl does not support the old .xls file format, please use xlrd to read this file, or convert it to the more recent .xlsx file format.
#   - [x] 修复NameError: name 'input_data' is not defined
#   - [ ] 实现提交条目数据到主表公司