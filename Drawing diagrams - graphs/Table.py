import numpy as np
import pandas as pd

# create a table
df = pd.DataFrame(index=['a', 'b', 'c', 'd'], columns=['column 1', 'column 2', 'column 3'])

# insert data/value
df['column 1'] = [1,2,3,4]
df['column 2'] = [5,6,7,8]
df['column 3'] = df['column 1'] + df['column 2']
print(df)

# drop a raw or a column
df = df.drop(axis=0, index='a')
df = df.drop(axis=1, columns='column 2')

