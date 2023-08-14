# -*- coding: utf-8 -*-
from gensim.models import KeyedVectors

model_path = 'D:/charmodel/sgns.baidubaike.bigram-char'
baidu_model = KeyedVectors.load_word2vec_format(model_path, binary=False)
path = 'C:/Users/jky/source/Python/request_cluster/src/'


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


# baidu_cluster_text(['苹果','香蕉','飞机'], 'test_cluster_Chinese.txt', 0.8)
baidu_cluster_file('test_data.txt', 'test_cluster_Chinese.txt', 0.7)
# baidu_cluster_text(
#     ['交换机', '服务器', '客户端', '网络设备', '虚拟机', '主机', '站点', '网段', '端口', '账号', '邮件', '路由器',
#      '设备', '分机', '无线网络', '路由', '互联网', '网页', '网站', '网关', '公网', '服务器', '交换机', '网段', '拨打',
#      '内网', '数据库', '数据中心', '无线连接', '客户机', '无线网', '域名', '测试环境', '网口', '发送', '查询', '邮箱',
#      '端口配置', '节点', '网络', '分机号', '交换机', '呼入', '网卡', '拨号', '机房设备', '插件', '网络拓扑', '加密',
#      '重新配置', '带宽', '重新安装', '连接', '网络管理', '视频会议', '网络结构', '服务器', '硬件', '计费', '视讯',
#      '链路'], 'cluster_Chinese', 0.5)
# baidu_cluster_text(
#     ['交换机', '服务器', '客户端', '网络设备', '虚拟机', '主机', '站点', '网段', '端口', '账号', '邮件', '路由器',
#      '设备', '分机', '无线网络', '路由', '互联网', '网页', '网站', '网关', '公网', '服务器', '交换机', '网段', '拨打',
#      '内网', '数据库', '数据中心', '无线连接', '客户机', '无线网', '域名', '测试环境', '网口', '发送', '查询', '邮箱',
#      '端口配置', '节点', '网络', '分机号', '交换机', '呼入', '网卡', '拨号', '机房设备', '插件', '网络拓扑', '加密',
#      '重新配置', '带宽', '重新安装', '连接', '网络管理', '视频会议', '网络结构', '服务器', '硬件', '计费', '视讯',
#      '链路'], 'cluster_Chinese', 0.53)
# baidu_cluster_text(
#     ['交换机', '服务器', '客户端', '网络设备', '虚拟机', '主机', '站点', '网段', '端口', '账号', '邮件', '路由器',
#      '设备', '分机', '无线网络', '路由', '互联网', '网页', '网站', '网关', '公网', '服务器', '交换机', '网段', '拨打',
#      '内网', '数据库', '数据中心', '无线连接', '客户机', '无线网', '域名', '测试环境', '网口', '发送', '查询', '邮箱',
#      '端口配置', '节点', '网络', '分机号', '交换机', '呼入', '网卡', '拨号', '机房设备', '插件', '网络拓扑', '加密',
#      '重新配置', '带宽', '重新安装', '连接', '网络管理', '视频会议', '网络结构', '服务器', '硬件', '计费', '视讯',
#      '链路'], 'cluster_Chinese', 0.57)
# baidu_cluster_text(
#     ['交换机', '服务器', '客户端', '网络设备', '虚拟机', '主机', '站点', '网段', '端口', '账号', '邮件', '路由器',
#      '设备', '分机', '无线网络', '路由', '互联网', '网页', '网站', '网关', '公网', '服务器', '交换机', '网段', '拨打',
#      '内网', '数据库', '数据中心', '无线连接', '客户机', '无线网', '域名', '测试环境', '网口', '发送', '查询', '邮箱',
#      '端口配置', '节点', '网络', '分机号', '交换机', '呼入', '网卡', '拨号', '机房设备', '插件', '网络拓扑', '加密',
#      '重新配置', '带宽', '重新安装', '连接', '网络管理', '视频会议', '网络结构', '服务器', '硬件', '计费', '视讯',
#      '链路'], 'cluster_Chinese', 0.58)
