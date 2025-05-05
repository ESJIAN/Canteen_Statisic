from sklearn.cluster import KMeans
import numpy as np

def sort_ocr_results(data):
    """
    对PaddleOCR识别结果进行行列排序。

    Args:
        data: PaddleOCR识别结果，格式如上所示。

    Returns:
        排序后的文本列表。
    """

    # 1. 数据预处理
    boxes = [item[0] for item in data]
    texts = [item[1][0] for item in data]
    # 计算每个文本框的中心点坐标
    centers = []
    for box in boxes:
        x_coords = [point[0] for point in box]
        y_coords = [point[1] for point in box]
        center_x = (min(x_coords) + max(x_coords)) / 2
        center_y = (min(y_coords) + max(y_coords)) / 2
        centers.append([center_x, center_y])
    centers = np.array(centers)

    # 2. 行聚类
    # 使用K-均值聚类将文本框聚类成不同的行
    kmeans = KMeans(n_clusters=5, random_state=0, n_init = 'auto')  # 假设有5行，可以根据实际情况调整
    row_labels = kmeans.fit_predict(centers[:, 1].reshape(-1, 1))  # 只使用y坐标进行聚类

    # 3. 行内排序
    # 对每一行内的文本框，根据x坐标进行排序
    rows = {}
    for i, label in enumerate(row_labels):
        if label not in rows:
            rows[label] = []
        rows[label].append((centers[i][0], texts[i]))  # 存储x坐标和文本

    sorted_rows = {}
    for label, items in rows.items():
        sorted_rows[label] = sorted(items, key=lambda x: x[0])  # 根据x坐标排序

    # 4. 结果输出
    # 将排序后的文本框按照行列顺序输出
    sorted_texts = []
    for label in sorted(sorted_rows.keys()):  # 按照行号排序
        for _, text in sorted_rows[label]:
            sorted_texts.append(text)

    return sorted_texts