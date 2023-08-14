import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc("font", family='YouYuan')

# function: 绘制饼状图
def plot(read_file_name):
    path = 'C:/Users/jky/source/Python/request_cluster/src/'
    read_file_path = path + read_file_name

    with open(read_file_path, 'r', encoding='utf-8') as file:
        # 读取文件中的所有行
        lines = file.readlines()

    # 用于存储单词和频率的字典
    word_frequency = {}

    for line in lines:
        # 去除行末尾的换行符并拆分为单词和频率
        word, frequency = line.strip().split(' ')
        # 将频率转换为整数
        frequency = int(frequency)
        # 非单字行存储单词和频率的对应关系到字典中
        word_frequency[word] = frequency

    # 提取标签和频率
    labels = list(word_frequency.keys())
    frequency = list(word_frequency.values())

    # 绘制饼状图
    plt.figure(figsize=(10, 10))
    plt.pie(frequency, labels=labels, autopct='%1.1f%%', startangle=0)
    plt.axis('equal')  # 使饼状图保持圆形
    plt.title(read_file_name)
    plt.show()


plot('frequency_group.txt')
plot('frequency_account.txt')
plot('frequency_theme.txt')
