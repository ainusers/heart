from sklearn.feature_extraction.text import TfidfVectorizer


# 注：信息检索领域非常重要的搜索词重要性度量；用以衡量一个关键词w对于查询（Query，可看作文档）所能提供的信息


vectorizer = TfidfVectorizer()
corpus = ['This is the first document.',
          'This is the second document.',
          'And the third one',
          'Is this the first document?'
          ]
# 获取文本特征
X = vectorizer.fit_transform(corpus)
print(X)

''' 运行结果：
  (0, 8)	0.4387767428592343
  (0, 3)	0.4387767428592343
  (0, 6)	0.35872873824808993
  (0, 2)	0.5419765697264572
  (0, 1)	0.4387767428592343
  (1, 8)	0.40412894713275094
  (1, 3)	0.40412894713275094
  (1, 6)	0.3304018949358263
  (1, 1)	0.40412894713275094
  (1, 5)	0.6331460890591822
  (2, 6)	0.2884767487500274
  (2, 0)	0.5528053199908667
  (2, 7)	0.5528053199908667
  (2, 4)	0.5528053199908667
  (3, 8)	0.4387767428592343
  (3, 3)	0.4387767428592343
  (3, 6)	0.35872873824808993
  (3, 2)	0.5419765697264572
  (3, 1)	0.4387767428592343
'''