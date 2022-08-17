import os
import json

with open('movie.json','r') as f1:
    loading = [json.loads(line.strip()) for line in f1.readlines()]

    print(len(loading))

    size_of_the_split=1249
    total = len(loading) // size_of_the_split

    print(total+1)
    for i in range(total+1):
        json.dump(loading[i * size_of_the_split:(i + 1) * size_of_the_split], open(
            "C:/Users/megan/OneDrive/桌面/Antra Python HW/Q2 Movie/data/data_split" + str(i+1) + ".json", 'w',
            encoding='utf8'), ensure_ascii=False, indent=True)