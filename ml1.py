import pandas as pd
import numpy as np
import jieba
import jieba.analyse
from collections import Counter
import sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import gensim
import gensim.corpora as corpora
from gensim.models.ldamodel import LdaModel
import warnings

# 加载数据
csv_file_path = './zhenmuyesv.csv'
df = pd.read_csv(csv_file_path)
print(sklearn.__version__)
warnings.filterwarnings("ignore", category=NotOpenSSLWarning)
# 数据预处理
# 假设文本列名为 'text'
def preprocess_text(content):
    # 这里可以添加更复杂的文本预处理步骤
    return " ".join(jieba.cut(content))

df['processed_text'] = df['content'].apply(preprocess_text)

# 词频分析
def get_top_n_words(corpus, n=None):
    vec = CountVectorizer().fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:n]

top_words = get_top_n_words(df['processed_text'], 10)

# 情感分析 (示例，需要进一步实现)
def sentiment_analysis(content):
    # 这里需要一个中文情感分析模型
    return np.random.choice(['Positive', 'Negative', 'Neutral'])

df['sentiment'] = df['processed_text'].apply(sentiment_analysis)

# 主题建模
def lda_topic_modeling(corpus):
    vectorizer = CountVectorizer()
    data_vectorized = vectorizer.fit_transform(corpus)
    
    # 构建LDA模型
    lda_model = LatentDirichletAllocation(n_components=5, max_iter=10, learning_method='online')
    lda_Z = lda_model.fit_transform(data_vectorized)
    
    return lda_model, vectorizer.get_feature_names(), lda_Z

lda_model, lda_feature_names, lda_Z = lda_topic_modeling(df['processed_text'])

# 数据可视化
# 词云
def plot_wordcloud(word_freq):
    wordcloud = WordCloud(width=800, height=400, background_color ='white').generate_from_frequencies(dict(word_freq))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

plot_wordcloud(dict(top_words))

# 词频直方图
def plot_top_words(word_freq):
    words = [word for word, freq in word_freq]
    freqs = [freq for word, freq in word_freq]
    plt.figure(figsize=(10, 5))
    plt.bar(words, freqs)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.title('Top Words in Corpus')
    plt.show()

plot_top_words(top_words)

# 主题可视化
def plot_top_topics(lda_model, feature_names, n_top_words=10):
    for topic_idx, topic in enumerate(lda_model.components_):
        print(f"Topic #{topic_idx + 1}:")
        print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
        # 这里可以进一步增加可视化代码

# 显示主题
plot_top_topics(lda_model, lda_feature_names)

# 注意：由于这里是静态的示例，某些功能（如情感分析）需要您根据实际情况进行实现。
