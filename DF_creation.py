import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [85.5, 90.0, 78.5]
}

df= pd.DataFrame(data)
print("DataFrame: \n",df)

print(df.info())