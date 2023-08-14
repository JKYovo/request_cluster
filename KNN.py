# function: KNN算法的实现
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier

# 示例数据
X_train_text = ["机器学习", "深度学习", "人工智能", "数据分析", "数据挖掘", "大数据", "云计算", "云服务", "云原生",
                "云平台"]
y_train = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]

X_test_text = ["数据分析", "机器学习"]

# 将文字数据转换成数值特征
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train_text)
X_test = vectorizer.transform(X_test_text)

# 创建KNN分类器并进行训练
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train, y_train)

# 进行预测
predictions = knn.predict(X_test)
print("预测结果:", predictions)
