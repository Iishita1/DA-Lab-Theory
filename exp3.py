import pandas as pd 
df=pd.read_excel('Datasets/tb_Stu_G1.xlsx')
df2=pd.read_excel('Datasets/tb_ST_Marks.xlsx')

df_marks=df.copy()
df_detail=df2.copy()    

# print(df_marks,'\n') 
# print(df_detail,'\n')

# Merge the two dataframes on 'Student_ID'
merged_df = pd.merge(df_marks, df_detail, on='Student_ID', how='right')
print(merged_df,'\n')
#in merging duplicate column names automatically get suffixed with _x and _y

merged_df2 = pd.merge(df_marks, df_detail, on='Student_ID', how='left')
print(merged_df2,'\n')
#left- all rows from left dataframe, NaN where no match in right

merged_df3 = pd.merge(df_marks, df_detail, on='Student_ID', how='inner')
print(merged_df3,'\n')
#inner- only rows with matching keys in both dataframes

merged_df4 = pd.merge(df_marks, df_detail, on='Student_ID', how='outer')
print(merged_df4,'\n')
#outer- all rows from both dataframes, NaN where no match

df_joined=df_marks.join(df_details, how="left")
print(df_joined,'\n')
