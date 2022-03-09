from sklearn.feature_extraction.text import CountVectorizer


# 注：One-Hot编码，又称独热编码，从提取方法来看也可以叫平权统计，中文的话要事先分好词，即按空格分好


# 如果想要降低特征的稀疏性的话，可以使用CountVectorizer(min_df=2)，这里min_df=2代表着只有频数（出现次数）超过2的词才会被记录。
vectorizer = CountVectorizer()
corpus = ['This is the first document.',
          'This is the second document.',
          'And the third one',
          'Is this the first document?'
          ]
# 获取文本特征
X = vectorizer.fit_transform(corpus)
print(X)

""" 原理解释：
提取：this is the first document second third and one
排序：
        and document first is one second the third this
    1    0      1      1    1  0    0     1    0     1
    2    0      1      0    1  0    1     1    0     1
    3    1      0      0    0  1    0     1    1     0
    4    0      1      1    1  0    0     1    0     1
"""

''' 运行结果：
  (0, 1)	1
  (0, 2)	1
  (0, 6)	1
  (0, 3)	1
  (0, 8)	1
  (1, 5)	1
  (1, 1)	1
  (1, 6)	1
  (1, 3)	1
  (1, 8)	1
  (2, 4)	1
  (2, 7)	1
  (2, 0)	1
  (2, 6)	1
  (3, 1)	1
  (3, 2)	1
  (3, 6)	1
  (3, 3)	1
  (3, 8)	1
'''