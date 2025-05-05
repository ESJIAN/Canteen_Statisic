import os
import cv2
import pandas as pd
from paddleocr import PaddleOCR
import numpy as np
from paddleocr import PaddleOCR, PPStructure

def image_to_excel(
    image_path: str,
    save_folder: str = "./src/data/input/manual",
    det_model_dir: str = 'best_accuracy',
    rec_model_dir: str = 'best_accuracy',
    structure_model_dir: str = 'best_accuracy'
):
    """
    使用PaddleOCR和PPStructure识别图片中的表格并导出为Excel文件。

    :param image_path: 输入图片路径
    :param save_folder: Excel文件保存目录
    :param det_model_dir: 检测模型路径
    :param rec_model_dir: 识别模型路径
    :param structure_model_dir: 表格结构模型路径
    """
    os.makedirs(save_folder, exist_ok=True)
    file_stem = os.path.splitext(os.path.basename(image_path))[0]

    # 初始化 OCR 和表格结构识别引擎
    ocr = PaddleOCR(det_model_dir=det_model_dir, rec_model_dir=rec_model_dir)
    table_engine = PPStructure(det_model_dir=det_model_dir, structure_model_dir=structure_model_dir)

    # 进行表格结构识别
    result = table_engine(image_path)

    # 提取表格内容并保存为 Excel
    for i, item in enumerate(result):
        if item['type'] == 'table':
            table_html = item['res']['html']
            dfs = pd.read_html(table_html)
            for j, df in enumerate(dfs):
                excel_path = os.path.join(save_folder, f"{file_stem}_table_{i}_{j}.xlsx")
                df.to_excel(excel_path, index=False)
    print("全部表格已识别并导出为Excel文件。")

# TODO:
# [x] 2025.5.4:修复因为后续条目没有编号造成的错位现象