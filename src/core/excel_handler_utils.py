# -*- coding: utf-8 -*-
# @Time    : 2025/5/3 21:19
# @Author  : wjwcj
# @Email   : wcj985@qq.com
# @File    : excel_handler_utils.py
# @Software: VsCode

import time
import re


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


