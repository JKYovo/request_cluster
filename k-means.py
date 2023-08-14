import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# function: k-means聚类
def k_means(read_file_name):
    path = 'C:/Users/jky/source/Python/request_cluster/src/'
    read_file_path = path + read_file_name

    with open(read_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 用于存储单词和频率的字典
    word_frequency = {}

    for line in lines:
        # 去除行末尾的换行符并拆分为单词和频率
        # word, frequency = line.strip().split(' ')   # 以空格分割(中文词汇）
        word, frequency = line.strip().rsplit(' ', 1)   # 以空格分割，只分割一次（英文词汇）
        # 将频率转换为整数
        frequency = int(frequency)
        word_frequency[word] = frequency


# # 输入数据（词汇和频率）
# word_frequency = {
#     '协助': 217,
#     '交换机': 213,
#     '防火墙': 207,
#     '配置': 190,
#     '设备': 153,
#     # 以下省略，按照相同格式继续输入
# }

    # 将词汇和频率分别存储在两个列表中
    words = list(word_frequency.keys())
    frequencies = list(word_frequency.values())

    # 对频率数据进行归一化处理
    normalized_frequencies = np.array(frequencies) / sum(frequencies)

    # 组合成特征向量
    X = np.column_stack((frequencies, normalized_frequencies))

    # 设置聚类簇的数量
    n_clusters = 20

    # 使用K-Means进行聚类
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(X)

    # 获取每个数据点的聚类标签
    labels = kmeans.labels_

    # 可视化聚类结果
    for i in range(n_clusters):
        cluster_words = [words[j] for j in range(len(words)) if labels[j] == i]
        print(f"Cluster {i + 1}: {cluster_words}")

    # 绘制词频率数据的散点图
    plt.scatter(frequencies, normalized_frequencies, c=labels, cmap='rainbow')
    plt.xlabel('Frequency')
    plt.ylabel('Normalized Frequency')
    plt.title('K-Means Clustering')
    plt.show()

k_means('frequency_theme_English.txt')