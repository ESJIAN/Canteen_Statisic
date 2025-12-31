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

def find_matching_month_rows(self,app,year,month,day,main_excel_file_path, sheet_name, columns = [2, 3]):
    """
    查找匹配的行数

    Parameters:
        self: 类实例
        app: xlwings 的 App 对象
        year: 年份
        month: 月份
        day: 日
        main_excel_file_path: 主 Excel 文件路径
        sheet_name: 工作表名称
        columns: 列索引列表
    
    """
    try:

        current_month = month

        workbook = app.books.open(main_excel_file_path)
        try:

            signal = False
            for i in workbook.sheets:
                title = re.sub(r'\s+', '' ,i.name)  # 修正中文标题中的空格i)# Mistake: sheet 对象没有叫做 title 的方法
                if title == sheet_name:
                    sheet = workbook.sheets[i]  # 使用指定的工作表名称
                    signal = True
                    break
            
            if not signal:
                print(f"Error: 表 `{sheet_name}` 不存在")
                return

        except Exception as e:
            print(f"Error: 在主表中查找 C 列中等于今天日数的行数和 B 列中等于本月月数的行数时出错, 错误信息 {e}")
            return None

        # 优化: 批量读取B列以减少Excel API调用
        # 查找 B 列中等于本月月数的行数
        used_rows_count = sheet.used_range.rows.count
        b_col_values = sheet.range((1, columns[0]), (used_rows_count, columns[0])).value
        if not isinstance(b_col_values, list):
            b_col_values = [[b_col_values]]
        elif b_col_values and not isinstance(b_col_values[0], list):
            b_col_values = [[val] for val in b_col_values]
        
        month_rows = [
            row_index + 1
            for row_index in range(used_rows_count)
            if b_col_values[row_index][0] is not None 
            and (not any(i not in "0123456789." for i in str(b_col_values[row_index][0]))) 
            and (str(b_col_values[row_index][0]).lstrip("0") == str(int(current_month)).lstrip("0"))
        ]
        print(f"Notice: B 列中等于本月月数的行数: {month_rows}")
        
        # 优化: 复用已读取的B列数据
        # [x]BUG:解决 row_index = 5 时候抛出的 ·unsupported operand type(s) for -: 'str' and 'int'· 问题
        # 查找 B 列中等于上月月数的行数
        last_month_rows = [
            row_index + 1
            for row_index in range(used_rows_count)
            if b_col_values[row_index][0] is not None 
            and (not any(i not in "0123456789." for i in str(b_col_values[row_index][0]))) 
            and (str(b_col_values[row_index][0]).lstrip("0") == str(int(current_month) - 1).lstrip("0"))
        ]
        print(f"Notice: B 列中等于上月月数的行数: {last_month_rows}")
        
        # 上月处理
        new_last_month_rows = []
        for i in last_month_rows:
            day = int(sheet.range((i, columns[1])).value)
            if day > 20:
                new_last_month_rows.append(i)
            else:
                print(f"Notice: 去除上月 {i} 行(日)")
        last_month_rows = new_last_month_rows

        # 本月处理
        new_month_rows = []
        for j in month_rows:

            day = int(sheet.range((j, columns[1])).value)
            if day <= 20:
                new_month_rows.append(j)
            else:
                print(f"Notice: 去除本月 {j} (行)日")
        month_rows = new_month_rows


        #上月末加本月20天为一个月
        month_rows += last_month_rows
        # 打印结果
        print(f"Notice: B 列中等于本月月数的行数: {month_rows}")

        # 关闭工作簿
        workbook.save()
        return month_rows

    except Exception as e:
        print(f"Error: 查找行数时出错,错误信息 {e}")
        __main__.SAVE_OK_SIGNAL = False
        return []
        
def find_matching_today_rows(app,year,month,day,main_excel_file_path, sheet_name, columns = [2, 3]):
    
    """
    在主表中查找 C 列中等于今天日数的行数和 B 列中等于本月月数的行数，
    并对比两个列表中相同的行数。

    Parameters:
      app: xw.App 对象，用于打开 Excel 文件
      year: int，年
      month: int，月
      day: int，日
      main_excel_file_path: str，主表路径
      sheet_name: str，工作表名称
      columns: list，月和日所在的列数, 主表为2、3列, 子表为1、2列

    Returns:


    """

    try:

        current_month = month
        current_day = day
        
        # 打开工作簿
        workbook = app.books.open(main_excel_file_path)

        try:

            signal = False
            for i in workbook.sheets:
                title = re.sub(r'\s+', '' ,i.name)  # 修正中文标题中的空格i)# Mistake: sheet 对象没有叫做 title 的方法
                if title == sheet_name:
                    sheet = workbook.sheets[i]  # 使用指定的工作表名称
                    signal = True
                    break
            
            if not signal:
                print(f"Error: 表 `{sheet_name}` 不存在")
                return

        except Exception as e:
            print(f"Error: 在主表中查找 C 列中等于今天日数的行数和 B 列中等于本月月数的行数时出错, 错误信息 {e}")
            return None

        # 优化: 批量读取两列数据以减少Excel API调用
        used_rows_count = sheet.used_range.rows.count
        
        # 批量读取B列和C列
        b_col_values = sheet.range((1, columns[0]), (used_rows_count, columns[0])).value
        c_col_values = sheet.range((1, columns[1]), (used_rows_count, columns[1])).value
        
        # 标准化为列表格式
        if not isinstance(b_col_values, list):
            b_col_values = [[b_col_values]]
        elif b_col_values and not isinstance(b_col_values[0], list):
            b_col_values = [[val] for val in b_col_values]
            
        if not isinstance(c_col_values, list):
            c_col_values = [[c_col_values]]
        elif c_col_values and not isinstance(c_col_values[0], list):
            c_col_values = [[val] for val in c_col_values]
        
        # 查找 C 列中等于今天日数的行数
        day_rows = [
            row_index + 1
            for row_index in range(used_rows_count)
            if c_col_values[row_index][0] is not None 
            and (not any(i not in "0123456789." for i in str(c_col_values[row_index][0]))) 
            and (str(c_col_values[row_index][0]).lstrip("0") == str(int(current_day)).lstrip("0"))
        ]

        # 如果返回值为空，则
        print(f"Notice: C 列中等于今天日数的行数: {day_rows}")

        # 查找 B 列中等于本月月数的行数 (应该是month不是day)
        month_rows = [
            row_index + 1
            for row_index in range(used_rows_count)
            if b_col_values[row_index][0] is not None 
            and (not any(i not in "0123456789." for i in str(b_col_values[row_index][0]))) 
            and (str(b_col_values[row_index][0]).lstrip("0") == str(int(current_month)).lstrip("0"))
        ]
        print(f"Notice: B 列中等于本月月数的行数: {month_rows}")

        # 找到两个列表中相同的行数
        matching_rows = list(set(day_rows) & set(month_rows))
        print(f"Notice:相同的行数: {matching_rows}", day_rows, month_rows)

        # 保存工作簿
        workbook.save() # Mistake: workbook 错误调用 close 方法导致对象提前退出
        return matching_rows

    except Exception as e:
        print(f"Error: 查找行数时出错,错误信息 {e}")
        return None


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

def get_all_sheets_todo_for_main_table(app,model):
    """
    Retrieves all sheet names to be processed for the main table from both manual and photo mode Excel files.
    
    This function reads sheet names from column J of the first sheet in two Excel files:
    1. Manual mode file (TEMP_SINGLE_STORAGE_EXCEL_PATH)
    2. Photo mode file (PHOTO_TEMP_SINGLE_STORAGE_EXCEL_PATH)
    
    Returns:
        list: A deduplicated list of non-empty sheet names found in both files.
        
    Note:
        - Empty values are filtered out from the results.
        - Errors during file reading are caught and printed, but don't stop execution.
    """
    sheets_to_add = set()

    ""
    if model == "manual":
        try:
            manual_workbook = app.books.open(__main__.TEMP_SINGLE_STORAGE_EXCEL_PATH)
            manual_sheet = manual_workbook.sheets[0]
            
            # 动态获取暂存表中每一行条目所要提交到的表中
            values = manual_sheet.range("J2:J" + str(manual_sheet.used_range.rows.count)).value
            if not isinstance(values, list):
                values = [values]
            
            sheets_to_add.update(filter(None, values))

        except Exception as e:
            print(f"Error: 无法读取手动模式: {e}")

    elif model == "photo":
        try:

            photo_workbook = app.books.open(__main__.PHOTO_TEMP_SINGLE_STORAGE_EXCEL_PATH)
            photo_sheet = photo_workbook.sheets[0]
            values = photo_sheet.range("J2:J" + str(photo_sheet.used_range.rows.count)).value
            
            if not isinstance(values, list):
                values = [values]
            
            sheets_to_add.update(filter(None, values))

        except Exception as e:
            print(f"Error: 无法读取图片模式: {e}")

    return list(sheets_to_add)


def sheets_of_sub_table(app,model):
    """
    在手动模式和图片模式的临时表中查找条目对对应的sheet名，并返回一个包含所有需要添加的sheet名的列表。
    Parameters:
        app: xlwings应用实例
        model: 模式名,manual或photo
    Returns:
        list: 包含所有需要添加的sheet名的列表
    """
    # 使用集合来存储唯一的sheet名
    sheets_to_add = set()
    # 读取手动模式的临时表

    # 监测第二行是否为空

    try:

        if model == "manual":

            # 打开手动模式的临时表
            manual_workbook = app.books.open(__main__.TEMP_SINGLE_STORAGE_EXCEL_PATH)
            manual_sheet = manual_workbook.sheets[0]
            
            # 检测第二行是否为空
            if manual_sheet.range("C2").value is None:
                print("Warning: 手动模式临时表的第二行为空，可能没有数据。")
                return []
            
            values = manual_sheet.range("C2:C" + str(manual_sheet.used_range.rows.count)).value
            if not isinstance(values, list):
                values = [values]
            sheets_to_add.update(filter(None, values))

        elif model == "photo":
            photo_workbook = app.books.open(__main__.PHOTO_TEMP_SINGLE_STORAGE_EXCEL_PATH)
            photo_sheet = photo_workbook.sheets[0]
            # 检测第二行是否为空
            if photo_sheet.range("C2").value is None:
                print("Warning: 图片模式临时表的第二行为空，可能没有数据。")
                return []
            values = photo_sheet.range("C2:C" + str(photo_sheet.used_range.rows.count)).value
            if not isinstance(values, list):
                values = [values]
            sheets_to_add.update(filter(None, values))

    except Exception as e:
        print(f"Error: 临时表中查找所有需要添加的sheet名失败: {e}")

    return list(sheets_to_add)


