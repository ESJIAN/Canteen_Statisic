import xlwings as xw

def is_visually_empty(cell):
    val = cell.value
    formula = cell.formula
    print(f"单元格值: {val}, 公式: {formula}")
    
    # 如果有公式但值为 None，认为“视觉不空”
    if formula and val is None:
        return False

    # 如果值为 0.0，清除公式并将其视为空
    if val == 0.0:
        cell.clear_contents()  # 清除公式
        print("单元格值为 0.0，公式已被清除，并认为该单元格为空")
        return True

    # 判断是否为横杠、空字符串、或者空值
    if val is None or (isinstance(val, str) and val.strip() in ["", "-"]):
        return True
    
    return False

# 指定文件名
xls_file = '2025年主副食-三矿版主食.xls'

# 打开 Excel 文件并检查 K83
app = xw.App(visible=False)
wb = app.books.open(xls_file)

try:
    sheet = wb.sheets['大米']
    cell = sheet.range('K83')
    empty = is_visually_empty(cell)
    print(f"文件：{xls_file}，工作表：'大米'，单元格 K83 是否 visually empty：{empty}")
finally:
    wb.close()
    app.quit()

# 加上 input() 防止程序退出
a = input("程序结束，按回车键退出...")
