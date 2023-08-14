# function: 朴素贝叶斯算法进行文本分类
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# 假设你有一个包含文本数据和标签的DataFrame，其中"Text"列包含文本数据，"Label"列包含标签
# 你可以根据你的实际数据来调整下面的代码

# 假设数据保存在名为df的DataFrame中
# df = pd.read_csv('your_data.csv')

# 例子数据
data = {
    'Text': ['交换机故障', '网络连接问题', '安装配置教程', 'VPN无法连接', '服务器宕机', '路由器设置'],
    'Label': ['交换机', '网络', '教程', 'VPN', '服务器', '路由器']
}
df = pd.DataFrame(data)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(df['Text'], df['Label'], test_size=0.2, random_state=42)

# 文本特征提取
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# 使用朴素贝叶斯算法进行分类
classifier = MultinomialNB()
classifier.fit(X_train_counts, y_train)

# 预测
y_pred = classifier.predict(X_test_counts)

# 评估模型性能
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Classification Report:")
print(report)
