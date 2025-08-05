import pandas as pd 
df=pd.read_excel('Datasets/1.xlsx')
df2=pd.read_excel('Datasets/2.xlsx')
df3=pd.read_excel('Datasets/3.xlsx')

# df_concat_Row = pd.concat([df, df2], axis=0) #row-wise concatenation
df_concat_Col = pd.concat([df, df2], axis=1) #column-wise concatenation
print(df_concat_Col,'\n')