import matplotlib.pyplot as plt
from wordcloud import WordCloud


# 生成词云

def cloud(read_file_name):
    path = 'C:/Users/jky/source/Python/request_cluster/src/'
    read_file_path = path + read_file_name
    word_frequency = {}

    with open(read_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            word, frequency = line.strip().split(' ')
            frequency = int(frequency)
            word_frequency[word] = frequency
    # 生成词云
    wordcloud = WordCloud(font_path='simhei.ttf', background_color='white', width=1000, height=500)
    wordcloud.generate_from_frequencies(word_frequency)

    # 显示词云图
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    # plt.title('词云图')
    plt.show()


cloud('frequency_group.txt')
cloud('frequency_account.txt')
cloud('frequency_theme.txt')
