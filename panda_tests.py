# import pandas as pd 
# pd.__version__
# df = pd.DataFrame([11,22,33], columns=['Col_Name'])
# print(df)
# print(type(df))
# data = {
#     'Name' : ['Ritik', 'Aman', 'Priya','Lalita'],
#     'age'  : [16,17,18,19],
#     'Marks' : [85,78,98,88]
# }
# s = pd.DataFrame(data)
# print(s)


import pandas as pd 

# df = pd.DataFrame([11, 22, 33], columns=['col_name'])
# print(df)

# print(type(df))

data= {
    'Name':['A','B','C','D'],
    'Age':[18,19,19,18],
    'marks':[70,80,85,90]
}
# print(data)
# print(type(data))

df=pd.DataFrame(data)
print(df)
print(type(df))

# print(df.head(2))
# print(df.tail(2))

# print(df.shape)
# print(df.columns)

# print(df.info())

# print(df.describe())

# df['Team'] = ['CEO','HR','CTO','DA']
# df
# Name= 'Madhav','Vishakha','Lalita','Rishabh'
# Age=  [16,17,18,19],
# Team= 'CEO','HR','CTO','DA'
# Monthly_Salary= 90000,70000,5000,30000,

# df.loc[df.Name=='Madhav','Monthly_Salary'] = 90000
# df
# Name= 'Madhav','Vishakha','Lalita','Rishabh''ABC'
# Age=  [16,17,18,19,21]
# Monthly_Salary= 90000,70000,50000,30000,21000
# Team= 'CEO','HR','CTO','DA','IT'
# Bonus= 18000.0,14000.0,10000.0,6000.0,2000.0

# df['DOJ'] = ['2024-01-01','2024-01-15','2024-03-28','2024-03-03']
# df
# df['DOJ'].dtype
# df['DOJ'] = pd.to_datetime(df['DOJ'])
# df['DOJ'].dtype

# df.isnull()
# import numpy as np
# df.loc[df.Name=='Rishabh','Saiary'] = np.nan
# df
