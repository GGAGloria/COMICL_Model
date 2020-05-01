import random
import pandas as pd
list = random.sample(range(900, 57014), 600)
print(list)
df = pd.read_csv('training.csv',header=0,sep=',')
rows = df.iloc[list,0]
f= open("random.txt","w+")
for i in rows:
    f.write("%s\n"%i)
f.close()
