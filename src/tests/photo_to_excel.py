import cv2
import pandas as pd
from paddleocr import PaddleOCR

# 1. 读取图片
image_path = "./src/data/input/img/9d9381751d72a45dc93902257c28d67.jpg"
img = cv2.imread(image_path)

# 2. 初始化 PaddleOCR（中文模型，表格识别）
ocr = PaddleOCR(use_angle_cls=True, lang="ch", det=True, rec=True, structure_version="PP-StructureV2")

# 3. 表格结构识别
result = ocr.ocr(image_path, cls=True, structure=True)

# 4. 提取表格数据
tables = []
for res in result:
    if 'table' in res:
        for table in res['table']:
            df = pd.DataFrame(table['cell'])
            tables.append(df)

# 5. 导出为 Excel
if tables:
    tables[0].to_excel("./src/data/test/test.xlsx", index=False, encoding="utf-8-sig")
    print("表格识别并导出成功")
else:
    print("未检测到表格，请检查图片内容或更换图片")



