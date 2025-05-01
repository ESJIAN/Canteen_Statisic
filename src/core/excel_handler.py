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


def cmmit_data_to_storage_excel(temp_excel_file):
    """
    提交暂存 Excel 数据到主表、副表 Excel 文件
    :param: temp_excel_file_path: 要存储的暂存表
    """
    # 1. 打开工作簿
    wb = load_workbook(file_path)
    ws = wb[sheet_name]

    # 2. 读出已有日期列表
    dates = []
    for row in range(data_start, ws.max_row+1):
        cell = ws[f"{date_col}{row}"].value
        if not cell: break
        # 如果是字符串，先解析
        d = cell if isinstance(cell, datetime) else datetime.strptime(cell, '%Y-%m-%d')
        dates.append((row, d))

    # 3. 二分查找第一个大于新日期的位置
    D_new = (input_data['日期']
            if isinstance(input_data['日期'], datetime)
            else datetime.strptime(input_data['日期'], '%Y-%m-%d'))
    lo, hi = 0, len(dates)
    while lo < hi:
        mid = (lo + hi) // 2
        if dates[mid][1] > D_new:
            hi = mid
        else:
            lo = mid + 1
    insert_idx = dates[lo][0] if lo < len(dates) else (dates[-1][0] + 1)

    # 4. 在工作表中插入空行
    ws.insert_rows(insert_idx)

    # 5. 填入新数据
    row = insert_idx
    ws[f"{date_col}{row}"].value = D_new
    # 假设其他字段在 B…J 列
    cols = ['B','C','D','E','F','G','H','I','J']
    keys = ['类别','品名','备注','金额','数量','单价','单位','公司']
    for col, key in zip(cols, keys):
        ws[f"{col}{row}"].value = input_data[key]

    # 6. 保存
    wb.save(file_path)
    return insert_idx


# TODO:
# - [x] 修复数据存储到Excel文件中的报错:ValueError: If using all scalar values, you must pass an index
# - [X] 实现以相对路径的方式存储表格到指定目录
# - [x] 2025.4.30 实现追加写入表格的行逻辑

