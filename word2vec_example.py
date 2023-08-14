# function: word2vec模型的使用
import gensim.downloader as api

# 加载word2vec模型
wv = api.load('word2vec-google-news-300')

# 使用.key_to_index和.index_to_key属性获取词汇表中的词汇
words = list(wv.key_to_index.keys())
# 或者直接获取索引到词汇的映射
word_to_index = wv.key_to_index
index_to_word = wv.index_to_key

# 接下来可以继续使用words或者word_to_index、index_to_word进行后续的操作
# 例如：
# for i, word in enumerate(words):
#     if i == 10:
#         break
#     print(f"Word {i + 1}: {word}")
# # 输出词汇表的大小和词向量的维度
# print(len(words))
# vec_computer = wv['computer']
# print(vec_computer.shape)

# 输出最相似的词汇
similar_words = wv.similar_by_word('hello', topn=5)
print(similar_words)

# 选出不是同类的词汇
# not_similar_words = wv.doesnt_match(['运维', '服务', '项目', '交付', '支持', '售前', 'T0', 'T2', 'T1', '公告', '通知',
#                                      '台湾', '商务'])
# print(not_similar_words)
