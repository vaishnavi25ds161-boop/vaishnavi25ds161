import pandas as pd 
pd.__version__
df = pd.DataFrame([11,22,33], columns=['Col_Name'])
print(df)
print(type(df))
data = {
    'Name' : ['Ritik', 'Aman', 'Priya','Lalita'],
    'age'  : [16,17,18,19],
    'Marks' : [85,78,98,88]
}
s = pd.DataFrame(data)
print(s)


