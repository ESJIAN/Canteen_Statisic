import os
import cv2
import pandas as pd
from paddleocr import PaddleOCR
import numpy as np
import sys

# 以绝对方式导入同目录模块中的函数
from k_means_algorithm import sort_ocr_results

# 1. 读取图片
image_path = "./src/data/input/img/9d9381751d72a45dc93902257c28d67.jpg"

# 2. 初始化 PaddleOCR（中文模型，表格识别）
ocr = PaddleOCR(use_angle_cls=True, lang="ch", det=True, rec=True, structure_version="PP-StructureV2")

# 3. 表格结构识别
result = ocr.ocr(image_path, cls=True)

# 4. 从第OCR扫描到的第三 3个对象开始
try:
    table = sort_ocr_results(result)
    # table = []
    # row_index = 1
    # row = []
    # for index in range(2, len(result[0])):
    #     if result[0][index][1][0] == "编码":
    #         continue
    #     else:
    #         row.append(result[0][index][1][0])
    #         print(f"Notice: 第 {row_index} 行已添加 {result[0][index][1][0]}") # 打印识别出的行
    #         if ( index -2 ) % 5  == 0 and (index - 2) != 0:
    #             row.reverse()      
    #             table.append(row.copy()) # 如果只是传入row对象，则在后面clear的时候会一并把table中的row引用给清空
    #             row_index += 1
    #             row.clear()

except Exception as e:
    print("表格结构识别失败，请检查图片格式是否正确")

# 5. 存储为 Excel
output_path = "./src/data/test/test.xlsx"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df = pd.DataFrame(table)
df.to_excel(output_path, index=False, header=False)
print("全部识别文本已分组导出，人工后处理即可")

# TODO:
# [x] 2025.5.4:修复因为后续条目没有编号造成的错位现象