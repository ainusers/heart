### heart 这是一颗跳动的心脏

描述我进入机器学习算法领域的历程，算法即核心。

### 1. 文本特征提取算法 （文本 -> 向量）
| 算法名称 | 参考地址 |
| --- | --- |
| One-hot | https://blog.csdn.net/qq_44186838/article/details/118425070 |
| TF-IDF | https://blog.csdn.net/qq_44186838/article/details/118425070 |
| Word2vec | https://blog.csdn.net/qq_44186838/article/details/118425070 |


### 2. 数据预处理算法
| 算法名称 | 算法功能 | 算法说明 |
| --- | --- | --- |
| StandardScaler | 无量纲化 | 标准化，基于特征矩阵的列，将特征值转换至服从标准正态分布 |
| MinMaxScaler | 无量纲化 | 区间缩放，基于最大最小值，将特征值转换到[0, 1]区间上 |
| Normalizer | 归一化 | 基于特征矩阵的行，将样本向量转换为“单位向量” |
| Binarizer | 二值化 | 基于给定阈值，将定量特征按阈值划分 |
| OneHotEncoder | 哑编码 | 将定性数据编码为定量数据 |
| Imputer | 缺失值计算 | 计算缺失值，缺失值可填充为均值等 |
| PolynomialFeatures | 多项式数据转换 | 多项式数据转换 |
| FunctionTransformer | 自定义单元数据转换 | 使用单变元的函数来转换数据 |
