import cv2
import pandas as pd
from paddleocr import PaddleOCR

# 1. 读取图片
image_path = "./src/data/input/img/9d9381751d72a45dc93902257c28d67.jpg"

# 2. 初始化 PaddleOCR（中文模型，表格识别）
ocr = PaddleOCR(use_angle_cls=True, lang="ch", det=True, rec=True, structure_version="PP-StructureV2")

# 3. 表格结构识别
result = ocr.ocr(image_path, cls=True)

# 4. 解析结果，提取文本内容
# 你可以根据实际表格的列顺序调整下面的字段
columns = ["编码", "品名及规格", "单位", "数量", "单价", "金额"]
data_rows = []

# 先找到表头的起始索引
header_indices = {}
for idx, item in enumerate(result):
    if isinstance(item, list) and len(item) == 2 and isinstance(item[1], tuple):
        text = item[1][0]
        for col in columns:
            if col in text:
                header_indices[col] = idx

# 假设表头后面就是数据行，按每行6列分组
start_idx = min(header_indices.values()) + 1 if header_indices else 0
row_length = len(columns)
flat_texts = [item[1][0] for item in result if isinstance(item, list) and len(item) == 2 and isinstance(item[1], tuple)]

# 提取数据行
for i in range(start_idx, len(flat_texts), row_length):
    row = flat_texts[i:i+row_length]
    if len(row) == row_length:
        data_rows.append(row)

# 5. 存储为 Excel
df = pd.DataFrame(data_rows, columns=columns)
df.to_excel("./src/data/test/test.xlsx", index=False, encoding="utf-8-sig")
print("表格识别并导出成功")



