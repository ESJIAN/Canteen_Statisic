# 必备三件套
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 生成500个二维数据点
np.random.seed(666)  # 固定随机种子方便复现
data = np.concatenate([
    np.random.normal(loc=[0,0], scale=0.5, size=(150,2)),
    np.random.normal(loc=[5,5], scale=1, size=(250,2)),
    np.random.normal(loc=[-5,5], scale=0.8, size=(100,2))
])

# 画个散点图看看
plt.scatter(data[:,0], data[:,1], s=10)
plt.title("原始数据分布")
plt.show()

# 创建模型（K=3）
kmeans = KMeans(
    n_clusters=3, 
    init='k-means++',  # 比random更聪明的初始化方式
    max_iter=300,      # 最大迭代次数
    tol=1e-04          # 收敛阈值
)

# 训练模型（注意这里没有y！是无监督学习）
kmeans.fit(data)

# 查看结果
print("质心坐标：\n", kmeans.cluster_centers_)
print("样本所属簇：", kmeans.labels_[:10])  # 查看前10个样本的类别

# 设置画布
plt.figure(figsize=(10,6))

# 绘制散点图
colors = ['red', 'blue', 'green']
for i in range(3):
    plt.scatter(
        data[kmeans.labels_==i, 0], 
        data[kmeans.labels_==i, 1],
        s=20, 
        c=colors[i],
        label=f'Cluster {i+1}'
    )

# 绘制质心
plt.scatter(
    kmeans.cluster_centers_[:,0],
    kmeans.cluster_centers_[:,1],
    s=200, 
    marker='*',
    c='black',
    label='Centroids'
)

plt.title("聚类结果可视化")
plt.legend()
plt.show()