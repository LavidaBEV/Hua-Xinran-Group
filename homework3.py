# 对汽车质量数据统计
import pandas as pd
# 导入csv数据
result = pd.read_csv('car_complain.csv')




# 独热编码
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
print(result.columns)
tags = result.columns[7:]

print('***************')
#品牌投诉总数
df= result.groupby(['brand'])['id'].agg(['count']).sort_values(by='count',ascending=False)
print('品牌投诉总数：')
print(df)

print('***************')
#车型投诉总数
df2= result.groupby(['car_model'])['id'].agg(['count']).sort_values(by='count',ascending=False)
print('车型投诉总数：')
print(df2)

print('***************')
#品牌车型投诉
df3= result.groupby(['brand','car_model'])['id'].agg(['count']).groupby(['brand']).mean().sort_values(by='count',ascending=False)
df4=df3.idxmax()
print('品牌的平均车型投诉最多是：',df4)

