import os
import cv2
import pandas as pd
from paddleocr import PaddleOCR
import numpy as np

def image_to_excel(
    image_path: str,
    lang: str = "ch",
    structure_version: str = "PP-StructureV2"
):
    """
    识别图片中的表格并导出为Excel文件。

    :param image_path: 输入图片路径
    :param lang: OCR语言
    :param structure_version: PaddleOCR结构化版本
    """
    output_path = "./src/data/input/manual/temp_img_input.xlsx"
    # 初始化 PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang=lang, det=True, rec=True, structure_version=structure_version)

    # 表格结构识别
    result = ocr.ocr(image_path, cls=True)

    # 处理识别结果
    try:
        table = []
        row_index = 1
        row = []
        for index in range(2, len(result[0])):
            if result[0][index][1][0] == "编码":
                continue
            else:
                row.append(result[0][index][1][0])
                print(f"Notice: 第 {row_index} 行已添加 {result[0][index][1][0]}")
                if (index - 2) % 5 == 0 and (index - 2) != 0:
                    row.reverse()
                    table.append(row.copy())
                    row_index += 1
                    row.clear()
    except Exception as e:
        print("表格结构识别失败，请检查图片格式是否正确")
        return

    # 存储为 Excel
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    if os.path.exists(output_path):
        # 读取已有内容
        existing_df = pd.read_excel(output_path, header=None)
        # 在尾部插入一空行
        empty_row = pd.DataFrame([[""] * existing_df.shape[1]], columns=existing_df.columns)
        # 新内容
        new_df = pd.DataFrame(table)
        # 拼接
        combined_df = pd.concat([existing_df, empty_row, new_df], ignore_index=True)
        combined_df.to_excel(output_path, index=False, header=False)
    else:
        df = pd.DataFrame(table)
        df.to_excel(output_path, index=False, header=False)
    print("全部识别文本已分组导出，人工后处理即可")

# TODO:
# [x] 2025.5.4:修复因为后续条目没有编号造成的错位现象