import pandas as pd
data = { 'even': range(20,0,-2),
         'odd':  range(1,21,2)
       }
df = pd.DataFrame(data)
print(df)
print(df.apply(max))

def odd_bigger(row):
    if row['odd'] > row['even']:
        return True
    return False

for index, row in df.iterrows():
    print(odd_bigger(index))

"""Making a change to trace it with GIT"""
"""Second change to trace with GIT now on a new branch"""