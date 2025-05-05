from paddleocr import PaddleOCR, PPStructure
import os
import pandas as pd

# 配置路径
image_path = "./src/data/input/img/9d9381751d72a45dc93902257c28d67.jpg"
save_folder = "./src/data/test"
os.makedirs(save_folder, exist_ok=True)
file_stem = os.path.splitext(os.path.basename(image_path))[0]

# 初始化 OCR 和表格结构识别引擎
table_engine = PPStructure(det_model_dir='best_accuracy', structure_model_dir='best_accuracy')

# 进行表格结构识别
result = table_engine(image_path)

# 提取表格内容并保存为 Excel
for i, item in enumerate(result):
    if item['type'] == 'table':
        table = item['res']['html']
        # 使用pandas读取html表格
        dfs = pd.read_html(table)
        for j, df in enumerate(dfs):
            excel_path = os.path.join(save_folder, f"{file_stem}_table_{i}_{j}.xlsx")
            df.to_excel(excel_path, index=False)