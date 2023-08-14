# function: 删除单个字的词频
def delete_single_word(read_file_name, save_file_name):
    path = 'C:/Users/jky/source/Python/request_cluster/src/'
    read_file_path = path + read_file_name
    save_file_path = path + save_file_name

    # 用于存储单词和频率的字典
    word_frequency = {}

    with open(read_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 处理每一行，并将单词和频率存储在字典中
    for line in lines:
        # 去除行末尾的换行符并拆分为单词和频率
        word, frequency = line.strip().split(' ')
        # 将频率转换为整数
        frequency = int(frequency)
        # 非单字行存储单词和频率的对应关系到字典中
        if (len(word) > 1):
            word_frequency[word] = frequency

    # 打印结果字典
    print(word_frequency)

    # 存入文件
    with open(save_file_path, 'w', encoding='utf-8') as file:
        for k, v in word_frequency.items():
            file.write(f'{k} {v}\n')


delete_single_word('frequency_theme.txt', 'frequency_theme.txt')
delete_single_word('frequency_group.txt', 'frequency_group.txt')
delete_single_word('frequency_account.txt', 'frequency_account.txt')