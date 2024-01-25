import pandas as pd
import sys
import random

# grupos = sys.argv[1:]
df1 = pd.read_csv("./data/Coleta_Negras.csv")
df2 = pd.read_csv("./data/Coleta_Pardas.csv")
df3 = pd.read_csv("./data/Coleta_Brancas.csv")

min_length = min(len(df1),len(df2),len(df3))

df1 = df1.sample(frac=1, random_state=42).reset_index(drop=True)
df2 = df2.sample(frac=1, random_state=42).reset_index(drop=True)
df3 = df3.sample(frac=1, random_state=42).reset_index(drop=True)


coleta_df = pd.concat([df1,df2,df3], ignore_index=True)

coleta_df = coleta_df.sample(frac=1, random_state=42).reset_index(drop=True)

coleta_df.to_csv("Coleta_Total.csv", index=False)