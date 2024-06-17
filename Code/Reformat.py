import pandas as pd
from sklearn.model_selection import train_test_split

################################################################
# # reformat
# # 读取CSV文件
# df = pd.read_csv('./data/train_data.csv')

# # 合并query和response字段为新的text字段
# df['text'] ='Q='+df['query'] + ' A=' + df['response']
# # 保留text和label字段
# df = df[['text', 'label']]

# # 保存包含新text字段的数据到新的CSV文件
# df.to_csv('./data/dataset_raw.csv', index=False)

# # 查看新数据的前几行
# print(df.head())


################################################################
# shuffle&split
# 读取CSV文件
df = pd.read_csv('./data/dataset_raw.csv')

# 打乱数据集顺序
df_shuffled = df.sample(frac=1, random_state=42)  # 随机打乱数据集顺序

# 分割数据集为训练集和测试集（7:3）
train_df, test_df = train_test_split(df_shuffled, test_size=0.3, random_state=42)

# 保存训练集和测试集到两个新的CSV文件
train_df.to_csv('./data/training_set.csv', index=False)
test_df.to_csv('./data/testing_set.csv', index=False)

# 打印训练集和测试集的大小
print("训练集大小:", len(train_df))
print("测试集大小:", len(test_df))