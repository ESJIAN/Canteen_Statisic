from img2table.document import Image
from img2table.ocr import TesseractOCR

# 1. 读取图片并创建 OCR 引擎
image_path = ".src/data/input/img/9d9381751d72a45dc93902257c28d67.jpg"
image = Image(src=image_path)
ocr_engine = TesseractOCR(lang="chi_sim")  # 中文识别

# 2. 表格识别
tables = image.extract_tables(ocr=ocr_engine, implicit_rows=False, borderless_tables=False)

# 3. 获取第一个表格（可遍历多个）
df = tables[0].df

# 4. 导出为 Excel 或 CSV
df.to_csv(".src\\data\\test\\test.xlsx", index=False, encoding="utf-8-sig")


# Learning:
# 1. TesseractOCR 的使用需要你前置环境，就是安装 Tesseract 库

# TODO:
# [ ] 2025.5.4 Fixed: raise EnvironmentError("Tesseract not found in environment. Check variables and PATH")