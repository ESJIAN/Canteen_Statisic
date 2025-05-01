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
from xlwt import Workbook


def store_single_entry_to_temple_excel(data, file_path):
    """
    将单条目的数据追加存储到临时excel表格中
    :param data: 要存储的字典数据
    :param file_path: 存储的文件路径
    :return: None
    """

    if not isinstance(data, dict):
        raise ValueError("数据必须是字典类型")
    
    # 确保字典的值是列表
    for key, value in data.items():
        if not isinstance(value, list):
            data[key] = [value]  # 转换为列表

    # 将字典数据转换为二维列表
    headers = list(data.keys())
    rows = list(zip(*data.values()))

    try:
        if os.path.exists(file_path):
            # 打开现有文件
            workbook = xlrd.open_workbook(file_path, formatting_info=True)
            sheet = workbook.sheet_by_index(0)
            # 过滤掉没有内容的行
            existing_rows = sum(1 for row_idx in range(sheet.nrows) if any(sheet.row_values(row_idx))) # Learning3:条件Sum函数的高级用法

            # 创建可写副本
            writable_workbook = copy(workbook)
            writable_sheet = writable_workbook.get_sheet(0)

            # 追加数据
            for row_index, row_data in enumerate(rows, start=existing_rows):
                for col_index, cell_value in enumerate(row_data):
                    writable_sheet.write(row_index, col_index, str(cell_value))  # 转为文本存储

            # 保存文件
            writable_workbook.save(file_path)
        else:
            # 创建新文件
            workbook = Workbook()
            sheet = workbook.add_sheet("Sheet1")

            # 写入表头
            for col_index, header in enumerate(headers):
                sheet.write(0, col_index, header)

                # 写入数据
                for row_index, row_data in enumerate(rows, start=1):
                    for col_index, cell_value in enumerate(row_data):
                        sheet.write(row_index, col_index, str(cell_value))  # 转为文本存储

            # 保存文件
            workbook.save(file_path)

        print("数据已成功追加存储到Excel文件中。")
    except Exception as e: # Leraning2：不能操作Excel正在打开的表
        print(f"写入Excel文件时出错: {e}")

def clear_temp_excel():
    """
    清空暂存的 Excel 表格内容
    :param: None
    :return: None
    """
    try:
        if os.path.exists(__main__.TEMP_SINGLE_STORAGE_EXCEL_PATH):
            # 打开现有文件
            workbook = xlrd.open_workbook(__main__.TEMP_SINGLE_STORAGE_EXCEL_PATH, formatting_info=True)
            writable_workbook = copy(workbook)
            sheet = writable_workbook.get_sheet(0)
            original_sheet = workbook.sheet_by_index(0)

            # 清空内容，只保留表头
            for row_index in range(1, original_sheet.nrows):
                for col_index in range(original_sheet.ncols):
                    sheet.write(row_index, col_index, "")  # 清空单元格内容

            # 保存文件
            writable_workbook.save(__main__.TEMP_SINGLE_STORAGE_EXCEL_PATH)
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
        print(f"Error:打开暂存表工作簿出错 {e}")
        return
    
    # 读取主工作表格数据
    try:
        # 打开工作簿
        main_workbook = xlrd.open_workbook(excel_file_path, formatting_info=True)
        # 创建可写副本
        main_workbook_copy = copy(main_workbook)  
        print(f"Notice: 主工作表加载成功，文件路径: {excel_file_path}")
    except Exception as e:
        print(f"Error: {e}")
        return

    # 获取表头数据
    headers = temp_storage_workbook.sheet_by_index(0).row_values(0)  # 获取表头的第一行数据
    # 确保表头是一个扁平的列表
    if not all(isinstance(header, str) for header in headers):
        raise ValueError("表头必须是字符串类型")
    
    # 轮询读取暂存表格数据行
    for row_index in range(1, temp_storage_workbook.sheet_by_index(0).nrows):
        
        # 读取行数据
        row_data = temp_storage_workbook.sheet_by_index(0).row_values(row_index)#   
        # 创建一个字典，用于存储列索引和列名的对应关系
        header_index = {name: idx for idx, name in enumerate(headers)}
        # 获取行中公司列单元中公司名数据
        company_name = row_data[header_index["公司"]]
        # 获取行中金额列单元中金额数据
        amount = row_data[header_index["金额"]]
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



   
   

# Learning:
# 1. Openpyxl 不对 .xls 文件格式提供支持，只能对 .xlsx 文件格式提供支持
# 2. 代码操作Excel打开的表时候会出现权限遭拒错误

# TODO:
# - [x] 修复数据存储到Excel文件中的报错:ValueError: If using all scalar values, you must pass an index
# - [X] 实现以相对路径的方式存储表格到指定目录
# - [x] 2025.4.30 实现追加写入表格的行逻辑
# - [ ] 2025.5.1 实现数据提交到主表、副表Excel文件的功能
#   - [x] 修复Error: openpyxl does not support the old .xls file format, please use xlrd to read this file, or convert it to the more recent .xlsx file format.
#   - [x] 修复NameError: name 'input_data' is not defined
#   - [ ] 实现提交条目数据到主表公司
#      - [x] 将openpyxl替换为xlwd，实现Excel以xls文件保存，减少与原表格的数据格式冲突
#      - [x] 修复： [Errno 13] Permission denied: '.\\src\\data\\input\\manual\\temp_manual_input_data.xls'
# - [ ] 2025.5.1 修复暂存一次表格前7行出现None字符的问题