import pandas as pd

import json
import random

df1 = pd.read_csv('annotated.csv')
# df2 = pd.read_csv('0405.csv') 
# arr1 = pd.isna(df1['caption'])
annotated = df1.iloc[:901,0]
print(annotated)
# arr2 = df2.iloc[:,0]
# arr = arr2.append(arr1)

filelist = pd.read_csv('filelist.csv')
unannotated = filelist.iloc[901:,0]
print(unannotated)

print(annotated.isin(unannotated))

todo = unannotated[~unannotated.isin(annotated)]
print(todo)
f= open("todo.csv","w+")
for i in todo:
    f.write("%s\n"%i)
f.close()
