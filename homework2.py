#成绩排序

import numpy as np

scoretype=np.dtype({'names':['姓名','语文','数学','英语'],
                    'formats': ['U32', 'i', 'i', 'i']})

score = np.array(
    [
    ('张飞',68,65,30),
    ('关羽',95,76,98),
    ('刘备',98,86,88),
    ('典韦',90,88,77),
    ('许褚',80,90,90)
    ],dtype=scoretype)


courses = {'语文': score[:]['语文'],
           '数学': score[:]['数学'], '英语': score[:]['英语']}


for course, scores in courses.items():
    print(course,"平均成绩：",np.mean(scores))
    print(course,"最小成绩：",np.amin(scores))
    print(course,"最大成绩：",np.amax(scores))
    print(course,"方差：",np.std(scores))
    print(course,"标准差：",np.var(scores))
    print("*********************")

print('总成绩排序')
ranks = sorted(score, key=lambda x: x[1]+x[2]+x[3], reverse=True)
print(ranks[:])

