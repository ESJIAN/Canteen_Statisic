# -*- coding: utf-8 -*-
# @Time    : 2025/5/3 21:19
# @Author  : wjwcj
# @Email   : wcj985@qq.com
# @File    : excel_handler_utils.py
# @Software: VsCode

import time
import re
from datetime import datetime
import xlwings as xw
import __main__

KEYWORDS = ["过次页", "月计", "累计"]

def is_single_punctuation(s):
    # 判断是否是一个单独的标点字符
    import string
    return len(s) == 1 and s in string.punctuation

def is_visually_empty(cell):
    # 判断单元格是否视觉上为空，包括值为 None、""、"-"、0.0（但是由公式产生的）
    if cell.formula:  # 如果有公式
        if cell.value in [None, "", "-", 0.0]:
            cell.formula = ""  # 清除公式
            return True
        return False
    return cell.value in [None, "", "-"]

def is_previous_rows_after_page_break(sheet, row_idx, max_check=3):
    """
    检查当前行之前的若干行是否存在“过次页”-连续空行的模式。
    max_check：往前最多检查多少行。
    """
    empty_count = 0
    for i in range(1, max_check + 1):
        check_row = row_idx - i
        if check_row <= 0:
            break

        # 如果这一行是空的
        if all(is_visually_empty(sheet.range((check_row, col))) for col in range(1, 12)):
            empty_count += 1
            continue

        # 如果这一行有“过次页”类词语
        if any(sheet.range((check_row, col)).value in ["过次页"] for col in range(1, 12)):
            return True  # 前面几行是空，且再前一行为“过次页”
        else:
            break  # 有非空内容，停止向前检查

    return False


def convert_number_to_chinese(num):
    num = str(num).split('.')
    dec_label = ['角', '分','厘']
    units =['', '拾', '佰', '仟', '万', '拾','佰','千','亿','拾','百','千','兆']
    transtab = str.maketrans('0123456789','零壹贰叁肆伍陆柒捌玖')

    if len(num) == 2:  #如果有小数部分
        decp,intp = num[1].translate(transtab),num[0][::-1].translate(transtab)
        dec_part = [(decp[i] if decp[i]!='零'else'') +(dec_label[i] if decp[i]!='零'else'') for i in range(len(decp))]#如果小数部分有零则数字和单位都要忽略
        int_part = [intp[i] +(units[i] if intp[i]!='零'else'') for i in range(len(intp))]#如果整数部分有零则单位忽略
        dec_tmp = ''.join(dec_part).rstrip('零')
        int_tmp = ''.join(reversed(int_part)).replace('零零零', '零').replace('零零', '零')
        result = ''+dec_tmp if num[0] == '0' else ''+int_tmp+dec_tmp if int_tmp.endswith('零') else ''+int_tmp+'圆'+dec_tmp #整数部分是0则直接输出小数部分
    else:
        intp = num[0][::-1].translate(transtab)
        int_part = [intp[i] +(units[i] if intp[i]!='零'else'') for i in range(len(intp))]
        int_tmp = ''.join(reversed(int_part))
        int_tmp = int_tmp.rstrip('零').replace('零零零', '零').replace('零零', '零')
        result = ''+int_tmp+'圆' 
    return result

def find_matching_month_rows(main_excel_file_path, sheet_name, columns = [2, 3]):
    """
    在主表中查找 B 列中等于本月月数的行数。
    :param columns 月和日所在的列数, 主表为2、3列, 子表为1、2列
    :param main_excel_file_path: 主表路径
    :param sheet_name: 工作表名称
    :return: 本月行数的列表
    """
    try:
        # 获取当前月份
        today = datetime.now()
        current_month = today.month

        # 打开 Excel 文件
        with xw.App(visible=False) as app:
            workbook = app.books.open(main_excel_file_path)
            sheet = workbook.sheets[sheet_name]  # 使用指定的工作表名称

            # 查找 B 列中等于本月月数的行数
            month_rows = [
                row_index + 1
                for row_index in range(sheet.used_range.rows.count)
                if sheet.range((row_index + 1, 2)).value is not None and str(sheet.range((row_index + 1, columns[0])).value).lstrip("0") == str(current_month).lstrip("0")
            ]

            # 打印结果
            print(f"B 列中等于本月月数的行数: {month_rows}")

            # 关闭工作簿
            workbook.close()
            return month_rows

    except Exception as e:
        print(f"Error: 查找行数时出错: {e}")
        return []
        
def find_matching_today_rows(main_excel_file_path, sheet_name, columns = [2, 3]):
    """
    在主表中查找 C 列中等于今天日数的行数和 B 列中等于本月月数的行数，
    并对比两个列表中相同的行数。
    :param columns 月和日所在的列数, 主表为2、3列, 子表为1、2列
    :param main_excel_file_path: 主表路径
    :return: 相同行数的列表
    """
    try:
        # 获取当前日期和月份
        today = datetime.now()
        current_day = today.day
        current_month = today.month

        # 打开 Excel 文件
        with xw.App(visible=False) as app:
            workbook = app.books.open(main_excel_file_path)
            sheet = workbook.sheets[sheet_name]  # 使用指定的工作表名称

            # for row_index in range(sheet.used_range.rows.count):
            #     print(sheet.range((row_index + 1, 3)).value, current_day)

            # 查找 C 列中等于今天日数的行数
            day_rows = [
                row_index + 1
                for row_index in range(sheet.used_range.rows.count)
                if sheet.range((row_index + 1, 2)).value != None and str(sheet.range((row_index + 1, columns[1])).value).lstrip("0") == str(current_day).lstrip("0")
            ]

            # 查找 B 列中等于本月月数的行数
            month_rows = [
                row_index + 1
                for row_index in range(sheet.used_range.rows.count)
                if sheet.range((row_index + 1, 2)).value != None and str(sheet.range((row_index + 1, columns[0])).value).lstrip("0") == str(current_month).lstrip("0")
            ]

            # 找到两个列表中相同的行数
            matching_rows = list(set(day_rows) & set(month_rows))

            # 打印结果
            # print(f"C 列中等于今天日数的行数: {day_rows}")
            # print(f"B 列中等于本月月数的行数: {month_rows}")
            print(f"相同的行数: {matching_rows}")

            # 关闭工作簿
            workbook.close()
            return matching_rows

    except Exception as e:
        print(f"Error: 查找行数时出错: {e}")
        return []


def find_the_first_empty_line_in_main_excel(sheet):
    """
    在主表中找到第一空行
    :param 已经打开的sheet
    :return int行数
    """
    # 查找第一行空行，记录下空行行标（从表格的第二行开始）
    for row_index in range(0, sheet.used_range.rows.count):
        if sheet.range((row_index + 1, 1)).value is None and row_index != 0:
            # 检查前一行是否包含“领导”二字
            if row_index > 0:
                previous_row_values = [
                str(sheet.range((row_index, col)).value).strip()
                for col in range(1, sheet.used_range.columns.count + 1)
                if sheet.range((row_index, col)).value is not None
                ]
                if any("领导" in value for value in previous_row_values):
                    print(f"Notice: 第 {row_index} 行包含“领导”二字，继续查找下一行")
                    continue
            # 检查当前列的前几行是否包含“序号”二字
            column_values = [
                str(sheet.range((row, 1)).value).strip()
                for row in range(1, row_index + 1)
                if sheet.range((row, 1)).value is not None
            ]
            if not any("序号" in value for value in column_values):
                print(f"Notice: 前 {row_index} 行未找到“序号”二字，继续查找下一行")
                continue
            break
    return row_index

def find_the_first_empty_line_in_sub_main_excel(sheet):
    """
    在子主食表中找到第一空行
    :param 已经打开的sheet
    :return int行数
    """
    #暂时感觉这个for循环没什么问题
    #wjwcj: 2025/05/04 15:31
    for sub_row_index in range(sheet.used_range.rows.count):
        # 检查每行的1到11列是否都是空
        if all(is_visually_empty(sheet.range((sub_row_index + 1, col))) for col in range(1, 12)):

            # 向前检查是否是“过次页 + 空行 + 空行”的模式
            if is_previous_rows_after_page_break(sheet, sub_row_index + 1):
                print(f"忽略第 {sub_row_index + 1} 行（前面是‘过次页’+连续空行）")
                continue

            print("这里开始执行", str(sub_row_index + 1))   

            # 检查前一行是否符合某些条件（仅包含空格或单个标点符号）
            if sub_row_index > 0 and all(
                ((sheet.range((sub_row_index, col)).value is None) or 
                (is_single_punctuation(str(sheet.range((sub_row_index, col)).value).strip())))
                for col in range(1, 12)
            ):
                print(f"Notice: 发现第 {sub_row_index + 1} 行可用(仅包含空格或单个标点)，开始写入数据")
                break

            print(f"Notice: 发现第 {sub_row_index + 1} 行为空行，开始写入数据")
            break
    return sub_row_index + 1

def find_the_first_empty_line_in_sub_auxiliary_excel(sheet):
    """
    在子副食表中找到第一空行
    :param 已经打开的sheet
    :return int行数
    """
    #暂时感觉这个for循环没什么问题
    #wjwcj: 2025/05/04 15:34
    for sub_row_index in range(sheet.used_range.rows.count):
        # 检查每行的1到11列是否都是空
        if all(is_visually_empty(sheet.range((sub_row_index + 1, col))) for col in range(1, 12)):

            # 向前检查是否是“过次页 + 空行 + 空行”的模式
            if is_previous_rows_after_page_break(sheet, sub_row_index + 1):
                print(f"Warning: 忽略第 {sub_row_index + 1} 行（前面是‘过次页’+连续空行）")
                continue

            print("Notice: 这里开始执行", str(sub_row_index + 1))   

            # 检查前一行是否符合某些条件（仅包含空格或单个标点符号）
            if sub_row_index > 0 and all(
                ((sheet.range((sub_row_index, col)).value is None) or 
                (is_single_punctuation(str(sheet.range((sub_row_index, col)).value).strip())))
                for col in range(1, 12)
            ):
                print(f"Notice: 发现第 {sub_row_index + 1} 行可用(仅包含空格或单个标点)，开始写入数据")
                break

            print(f"Notice: 发现第 {sub_row_index + 1} 行为空行，开始写入数据")
            break
    return sub_row_index + 1

def get_all_sheets_todo_for_main_table():
    sheets_to_add = set()

    try:
        with xw.App(visible=False) as app:
            manual_workbook = app.books.open(__main__.TEMP_SINGLE_STORAGE_EXCEL_PATH)
            manual_sheet = manual_workbook.sheets[0]
            values = manual_sheet.range("J2:J" + str(manual_sheet.used_range.rows.count)).value
            if not isinstance(values, list):
                values = [values]
            sheets_to_add.update(filter(None, values))
    except Exception as e:
        print(f"Error: 无法读取手动模式: {e}")

    try:
        with xw.App(visible=False) as app:
            photo_workbook = app.books.open(__main__.PHOTO_TEMP_SINGLE_STORAGE_EXCEL_PATH)
            photo_sheet = photo_workbook.sheets[0]
            values = photo_sheet.range("J2:J" + str(photo_sheet.used_range.rows.count)).value
            if not isinstance(values, list):
                values = [values]
            sheets_to_add.update(filter(None, values))
    except Exception as e:
        print(f"Error: 无法读取图片模式: {e}")

    return list(sheets_to_add)


def get_all_sheets_todo_for_sub_table():
    sheets_to_add = set()
    try:
        with xw.App(visible=False) as app:
            manual_workbook = app.books.open(__main__.TEMP_SINGLE_STORAGE_EXCEL_PATH)
            manual_sheet = manual_workbook.sheets[0]
            values = manual_sheet.range("B2:B" + str(manual_sheet.used_range.rows.count)).value
            if not isinstance(values, list):
                values = [values]
            sheets_to_add.update(filter(None, values))

    except Exception as e:
        print(f"Error: 读取手动模式临时表失败: {e}")

    try:
        with xw.App(visible=False) as app:
            photo_workbook = app.books.open(__main__.PHOTO_TEMP_SINGLE_STORAGE_EXCEL_PATH)
            photo_sheet = photo_workbook.sheets[0]
            #图片导入的话品名在C列
            values = photo_sheet.range("C2:C" + str(photo_sheet.used_range.rows.count)).value
            if not isinstance(values, list):
                values = [values]
            sheets_to_add.update(filter(None, values))

    except Exception as e:
        print(f"Error: 读取图片模式临时表失败: {e}")

    return list(sheets_to_add)


