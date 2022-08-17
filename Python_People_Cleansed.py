import pandas as pd

df1 = pd.read_csv("people_1.txt", sep="\t")
df2 = pd.read_csv("people_2.txt", sep="\t")

df = pd.concat([df1, df2])

df['FirstName'] = df.FirstName.str.upper().str.strip()
df['LastName'] = df.LastName.str.upper().str.strip()
df['Email'] = df.Email.str.upper().str.strip()
df['Phone'] = df.Phone.str.replace('-','').str.strip()
df['Address'] = df.Address.str.replace('No.','').str.replace('#','').str.strip()

df = df.drop_duplicates()
print(len(df))

print(df.head(500))
