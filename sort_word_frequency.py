import jieba
from collections import Counter


# function: 读取文本文件分词后按词频排序
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


get_stopwords_list('data_group.txt', 'frequency_group.txt')
get_stopwords_list('data_account.txt', 'frequency_account.txt')
get_stopwords_list('data_theme.txt', 'frequency_theme.txt')
