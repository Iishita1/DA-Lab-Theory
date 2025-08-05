import pandas as pd 
df=pd.read_excel('Datasets/1.xlsx')
df2=pd.read_excel('Datasets/2.xlsx')

df_concat_Row = pd.concat([df, df2], axis=0)
df_concat_Col = pd.concat([df, df2], axis=1)
print(df_concat_Col,'\n')