import pandas as pd 
df = pd.read_excel('Datasets/tb_Stu_G1.xlsx')
print(df,'\n')
#prints False where value aint missing and True where value is missing
print(df.isnull(),'\n')
#prints no.of missing value in each column
print(df.isnull().sum(),'\n')
#prints no.of missing value in whole table
print(df.isnull().sum().sum(),'\n')
#drop the row if info is missing
print(df.dropna(),'\n')
#drop the row if all info is missing
print(df.dropna(how='all'),'\n')
# drop column
print(df.dropna(axis=1),'\n')
# add estimated value to missing value Technique 1(Fill with 0)
print(df.fillna(0),'\n')
#add estimated value to missing value Technique 2(Fill with mean)
df_temp=df.copy()
df_temp['Age'].fillna(df['Age'].mean(),inplace=True)
print(df_temp,'\n')

#add estimated value to missing value Technique 3(Fill with median)
df_t2=df.fillna(df.median(numeric_only=True))
print(df_t2,'\n')

#add estimated value to missing value Technique 4(Fill with forward fill) no value should be missing in 2 consecutive rows
df.ffill=df.fillna(method='ffill')
print(df.ffill,'\n')

#add estimated value to missing value Technique 5(Fill with backward fill) no 2 consecutive rows should be missing
df.bfill=df.fillna(method='bfill')
print(df.bfill,'\n')

#add estimated value to missing value Technique 6(Fill with linear interpolation)
df_interpolated=df.interpolate()
print(df_interpolated,'\n')
