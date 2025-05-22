import pandas as pd
import numpy as np  

# Sample fruit price DataFrame
data = {'Fruit': ['Apple', 'Banana', 'Orange'],  
        'Price': [2.5, 1.2, 3.3]}
df= pd.DataFrame(data)
print(df)


# Calculate average price  
avg_price = df['Price'].mean()  
print(avg_price)

# Filter prices > average
filter = df['Fruit']<'D'
print(df.loc[filter])

# isin() filter on fruits   
fruit_filter = df['Fruit'].isin(['Apple','Orange']) 
df.loc[fruit_filter]
print(df.loc[fruit_filter])

