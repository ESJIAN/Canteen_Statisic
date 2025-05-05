from matplotlib import pyplot as plt
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
    # 计算每个文本框的中心点坐标
    centers = []
    for item in data[0]:
        boxes = item[0]                                # 得到单个定位框四个坐标以及条目数据
        texts = item[1][0]                             # 得到定位矩形的四个坐标点数据
        
        x_coords = [point[0] for point in boxes]       # 获取矩形框x轴四坐标
        y_coords = [point[1] for point in boxes]       # 获取矩形框y轴四坐标
        center_x = sum(x_coords) / 4                   # 四个点x坐标的平均值
        center_y = sum(y_coords) / 4                   # 四个点y坐标的平均值
        centers.append([center_x, center_y])
    
    # 将点调用matplot绘出来
    x_plots = [x[0] for x in centers]
    y_plots = [y[1] for y in centers]
    plt.scatter(x_plots, y_plots)
    plt.show()

    # 转换为numpy数组
    centers = np.array(centers)

    # 2. 行聚类
    kmeans_rows = KMeans(n_clusters=len(data[0]), init='k-means++', n_init='auto')
    row_labels = kmeans_rows.fit_predict(centers[:, 1].reshape(-1, 1))

    # 3. 行内排序
    rows = {}
    for i, row_label in enumerate(row_labels):
        if row_label not in rows:
            rows[row_label] = []
        rows[row_label].append((centers[i][0], centers[i][1], texts[i]))

    # 排序行（按Y坐标从上到下）
    sorted_rows = sorted(rows.items(), key=lambda x: np.mean([pt[1] for pt in x[1]]))

    # 4. 结果输出
    final_result = []
    for _, items in sorted_rows:
        # 行内按X排序
        sorted_items = sorted(items, key=lambda x: x[0])
        final_result.append([t[2] for t in sorted_items])  # 每行一个列表

    return final_result


