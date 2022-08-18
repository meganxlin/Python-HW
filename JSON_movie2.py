import pandas as pd

df = pd.read_json('movie.json')
s = int(len(df) / 8)
p = 0

for i in range(7):
    temp = df[p:p + s]
    temp.to_json('movie.json'+str(i+1)+'.json')
    p += s
df[p:].to_json('movie_split.json')