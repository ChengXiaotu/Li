from gensim.models import Word2Vec
import numpy as np


# 训练数据
sentences = [
    "番茄非常好吃",
    "西红柿熟了",
    "我喜欢吃西红柿"
]

# 训练 Word2Vec 模型
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# 计算“西红柿”和“番茄”的向量
vector_tomato = model.wv['西红柿']
vector_tomato_fruit = model.wv['番茄']

# 计算两个向量的余弦相似度
similarity = np.dot(vector_tomato, vector_tomato_fruit) / (np.linalg.norm(vector_tomato) * np.linalg.norm(vector_tomato_fruit))

print(f"西红柿和番茄的近似度: {similarity}")
# print(model.wv.similarity('西红柿','番茄'))