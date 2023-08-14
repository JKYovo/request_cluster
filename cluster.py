# -*- coding: utf-8 -*-
from gensim.models import KeyedVectors
import jieba
from collections import Counter
import gensim.downloader as api

model_path = 'D:/charmodel/sgns.baidubaike.bigram-char'
baidu_model = KeyedVectors.load_word2vec_format(model_path, binary=False)
path = 'C:/Users/jky/source/Python/request_cluster/src/'


# 加载预训练的Word2Vec模型（不需要分类的时候可以注释掉加快运行速度）
# wv = api.load('word2vec-google-news-300')


# function: 读取文本文件并按词频排序
def get_stopwords_list(read_file_name, save_file_name):
    read_path = 'C:/Users/jky/source/Python/request_cluster/src/'
    save_path = 'C:/Users/jky/source/Python/request_cluster/src/'
    read_file_path = read_path + read_file_name
    save_file_path = save_path + save_file_name

    # 从外部文件导入示例文本（中文）
    with open(read_file_path, 'r', encoding='utf-8') as file:
        text_data = file.read()

    # 使用结巴分词进行中文文本分词
    seg_list = jieba.cut(text_data, cut_all=False)

    # 使用Counter来统计词频
    word_freq = Counter(seg_list)

    # 输出词频结果到文本文件
    with open(save_file_path, 'w', encoding='utf-8') as file:
        for k, v in word_freq.items():
            file.write(f'{k} {v}\n')

    # 读取文本文件并按词频排序
    try:
        with open(save_file_path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            sorted_lines = []
            for line in lines:
                parts = line.strip().split(' ')
                if len(parts) == 2:
                    sorted_lines.append((parts[0], int(parts[1])))
                else:
                    print(f"Skipping line: {line.strip()} (Invalid format)")

            sorted_lines.sort(key=lambda x: x[1], reverse=True)

            # 将文件指针移动到文件开头
            file.seek(0)

            # 清空文件内容
            file.truncate()

            for word, frequency in sorted_lines:
                # print(f"{word} {frequency}")
                file.write(f'{word} {frequency}\n')
    except FileNotFoundError:
        print(f"Error: File '{read_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# 文件（写入）
def word2_cluster_file(read_file_name, save_file_name, similarity_threshold):
    path = 'C:/Users/jky/source/Python/request_cluster/src/'
    read_file_path = path + read_file_name
    save_file_path = path + save_file_name
    with open(read_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 用于存储单词的列表
    cleaned_lines = []

    for line in lines:
        # 按空格分割每一行，删除最后一个元素（频率）
        word = line.strip().split(' ')[:-1]
        # 剩下的单词按列表存储
        word = ' '.join(word)
        # 将提取的单词重新拼接成字符串
        cleaned_line = f'{word}\n'
        cleaned_lines.append(cleaned_line)
        # 使用列表推导式和strip()方法去除换行符
        cleaned_list = [word.strip() for word in cleaned_lines]

    # 用于存储分类结果的字典，key为类别名，value为对应类别中的词汇列表
    word_clusters = {}

    # 遍历要分类的词汇列表
    for word in cleaned_list:
        # 将词汇加入到任何一个类别之前，先查找是否与现有类别中的词汇相似
        found_similar_word = False
        for cluster_name, cluster_words in word_clusters.items():
            for cluster_word in cluster_words:
                try:
                    # 计算词汇之间的相似度
                    similarity = wv.similarity(word, cluster_word)
                    if similarity > similarity_threshold:
                        word_clusters[cluster_name].append(word)
                        found_similar_word = True
                        break
                except KeyError:
                    # 如果发生KeyError异常，则说明词汇不存在于Word2Vec模型中
                    pass
            if found_similar_word:
                break
        # 如果与现有类别中的词汇都不相似，则将词汇放入新的类别中
        if not found_similar_word:
            cluster_name = f"{word}"
            word_clusters[cluster_name] = [word]

    print(len(word_clusters))
    print("file函数")

    with open(save_file_path, 'w', encoding='utf-8') as file:
        for cluster_name, cluster_words in word_clusters.items():
            file.write(f"{cluster_name}: {cluster_words}\n")


# 文本（写追加）
def word2_cluster_text(cleaned_list, save_file_name, similarity_threshold):
    path = 'C:/Users/jky/source/Python/request_cluster/src/'
    save_file_path = path + save_file_name
    # 用于存储分类结果的字典，key为类别名，value为对应类别中的词汇列表
    word_clusters = {}

    # 遍历要分类的词汇列表
    for word in cleaned_list:
        # 将词汇加入到任何一个类别之前，先查找是否与现有类别中的词汇相似
        found_similar_word = False
        for cluster_name, cluster_words in word_clusters.items():
            for cluster_word in cluster_words:
                try:
                    # 计算词汇之间的相似度
                    similarity = wv.similarity(word, cluster_word)
                    if similarity > similarity_threshold:
                        word_clusters[cluster_name].append(word)
                        found_similar_word = True
                        break
                except KeyError:
                    # 如果发生KeyError异常，则说明词汇不存在于Word2Vec模型中
                    pass
            if found_similar_word:
                break
        # 如果与现有类别中的词汇都不相似，则将词汇放入新的类别中
        if not found_similar_word:
            cluster_name = f"{word}"
            word_clusters[cluster_name] = [word]

    print(len(word_clusters))
    print("text函数")

    with open(save_file_path, 'a', encoding='utf-8') as file:
        for cluster_name, cluster_words in word_clusters.items():
            file.write(f"{cluster_name}: {cluster_words}\n")
        file.write(f"'similarity_threshold': {similarity_threshold}\n")


# 文件（写入）
def baidu_cluster_file(read_file_name, save_file_name, similarity_threshold):
    read_file_path = path + read_file_name
    save_file_path = path + save_file_name
    with open(read_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cleaned_lines = []

    for line in lines:
        # 按空格分割每一行，删除最后一个元素（频率）
        # word = line.strip().split(' ')[:-1]
        # 剩下的单词按列表存储
        # word = ' '.join(line)
        # 将提取的单词重新拼接成字符串
        cleaned_line = f'{line}\n'
        cleaned_lines.append(cleaned_line)
        # 使用列表推导式和strip()方法去除换行符
    cleaned_list = [word.strip() for word in cleaned_lines]

    # 用于存储分类结果的字典，key为类别名，value为对应类别中的词汇列表
    word_clusters = {}

    # 遍历要分类的词汇列表
    for word in cleaned_list:
        # 将词汇加入到任何一个类别之前，先查找是否与现有类别中的词汇相似
        found_similar_word = False
        for cluster_name, cluster_words in word_clusters.items():
            for cluster_word in cluster_words:
                try:
                    # 计算词汇之间的相似度
                    similarity = baidu_model.similarity(word, cluster_word)
                    if similarity > similarity_threshold:
                        word_clusters[cluster_name].append(word)
                        found_similar_word = True
                        break
                except KeyError:
                    # 如果发生KeyError异常，则说明词汇不存在于Word2Vec模型中
                    pass
            if found_similar_word:
                break
        # 如果与现有类别中的词汇都不相似，则将词汇放入新的类别中
        if not found_similar_word:
            cluster_name = f"{word}"
            word_clusters[cluster_name] = [word]

    print(len(word_clusters))
    print("file函数")

    with open(save_file_path, 'w', encoding='utf-8') as file:
        for cluster_name, cluster_words in word_clusters.items():
            file.write(f"{cluster_name}: {cluster_words}\n")


# 文本（写追加）
def baidu_cluster_text(cleaned_list, save_file_name, similarity_threshold):
    # 用于存储分类结果的字典，key为类别名，value为对应类别中的词汇列表
    word_clusters = {}
    save_file_path = path + save_file_name
    # 遍历要分类的词汇列表
    for word in cleaned_list:
        # 将词汇加入到任何一个类别之前，先查找是否与现有类别中的词汇相似
        found_similar_word = False
        for cluster_name, cluster_words in word_clusters.items():
            for cluster_word in cluster_words:
                try:
                    # 计算词汇之间的相似度
                    similarity = baidu_model.similarity(word, cluster_word)
                    if similarity > similarity_threshold:
                        word_clusters[cluster_name].append(word)
                        found_similar_word = True
                        break
                except KeyError:
                    # 如果发生KeyError异常，则说明词汇不存在于Word2Vec模型中
                    pass
            if found_similar_word:
                break
        # 如果与现有类别中的词汇都不相似，则将词汇放入新的类别中
        if not found_similar_word:
            cluster_name = f"{word}"
            word_clusters[cluster_name] = [word]

    print(len(word_clusters))
    print("text函数")

    with open(save_file_path, 'a', encoding='utf-8') as file:
        for cluster_name, cluster_words in word_clusters.items():
            file.write(f"{cluster_name}: {cluster_words}\n")
        file.write(f"'similarity_threshold': {similarity_threshold}\n")


# get_stopwords_list('test_data.txt', 'test_frequency.txt')
# word2_cluster_file('test_data.txt', 'test_cluster_English.txt', 0.4)
# word2_cluster_file('test_data.txt', 'test_cluster_English.txt', 0.5)
baidu_cluster_file('test_data.txt', 'test_cluster_Chinese.txt', 0.5)

