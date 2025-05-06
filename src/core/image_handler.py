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
    使用PaddleOCR和PPStructure识别图片中的表格并导出为Excel文件（支持追加写入）。

    :param image_path: 输入图片路径
    :param save_folder: Excel文件保存目录
    :param det_model_dir: 检测模型路径
    :param rec_model_dir: 识别模型路径
    :param structure_model_dir: 表格结构模型路径
    """
    os.makedirs(save_folder, exist_ok=True)
    file_stem = os.path.splitext(os.path.basename(image_path))[0]
    excel_path = os.path.join(save_folder, f"temp_img_input.xlsx")

    # 初始化表格结构识别引擎
    table_engine = PPStructure(det_model_dir=det_model_dir, structure_model_dir=structure_model_dir)

    # 进行表格结构识别
    result = table_engine(image_path)

    # 提取表格内容
    new_tables = []
    for i, item in enumerate(result):
        if item['type'] == 'table':
            table_html = item['res']['html']
            dfs = pd.read_html(table_html)
            for df in dfs:
                new_tables.append(df)

    # 追加写入逻辑
    if os.path.exists(excel_path):
        # 读取已有数据
        try:
            existing_df = pd.read_excel(excel_path)
        except Exception:
            existing_df = pd.DataFrame()
        # 合并所有新表格
        combined_new = pd.concat(new_tables, ignore_index=True) if new_tables else pd.DataFrame()
        # 合并已有和新数据
        final_df = pd.concat([existing_df, combined_new], ignore_index=True)
    else:
        # 仅保存新表格
        final_df = pd.concat(new_tables, ignore_index=True) if new_tables else pd.DataFrame()

    # 保存到Excel
    final_df.to_excel(excel_path, index=False)
    print("全部表格已识别并追加导出到Excel文件。")

# TODO:
# [x] 2025.5.4:修复因为后续条目没有编号造成的错位现象
# [x] 2025.5.5:实现追加写入表格逻辑
#   [ ] 2025.5.6 解决多线程工作模式下造成的写入覆盖问题