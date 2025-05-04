# -*- coding: utf-8 -*-
# @Time    : 2025/5/3 21:19
# @Author  : wjwcj
# @Email   : wcj985@qq.com
# @File    : excel_handler_utils.py
# @Software: VsCode



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

