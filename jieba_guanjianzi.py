# 使用 jieba 进行关键词提取的样例代码。这段代码首先对文本进行分词，然后使用基于 TF-IDF 算法的 jieba.analyse 模块提取关键词
import jieba
import jieba.analyse
import pandas as pd

# 加载数据
# 假设您的 CSV 文件路径是 'your_data.csv'，并且文本列的标题是 'content'
csv_file_path = './zhenmuyesv.csv'
df = pd.read_csv(csv_file_path)

# 设置 jieba 的 TF-IDF 关键词提取
# topK 指定每个文档提取的关键词数量
topK = 15

def extract_keywords(text):
    keywords = jieba.analyse.extract_tags(text, topK=topK)
    return keywords

# 应用关键词提取
df['keywords'] = df['content'].apply(extract_keywords)

# 显示结果
print(df['keywords'])
