import re
import pandas

def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)',text) ]

with open('random.txt') as f:
    lines = f.read().splitlines()
lines.sort(key=natural_keys)

df = pandas.DataFrame(data={"image":lines})
df.to_csv("0414.csv", sep=',',index=False)