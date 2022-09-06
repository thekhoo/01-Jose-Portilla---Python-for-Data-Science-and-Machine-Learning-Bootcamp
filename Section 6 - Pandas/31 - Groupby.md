# 31 - Groupby

Groupby allows you to group rows based off a column and perform an aggregate function on them *(sum, std, avg)*.

## Grouping by Column

Creating the DataFrame.

```py
import numpy as np
import pandas as pd

data = {
    'Company': ['GOOG','GOOG','MSFT','MSFT','FB','FB'],
    'Person': ['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
    'Sales': [200,120,340,124,243,350]
}

# Creating a DataFrame from the Data
df = pd.DataFrame(data)
```

Grouping by the company column. `df.groupby(column_name)` returns a groupby object. An aggregate function has to be called on it.

**NOTE:** Python will automatically ignore any non-numerical columns when an aggregate function is called as non-numerical columns cannot be summed, averaged etc.

```py
# Grouping by Company
byComp = df.groupby('Company')

# Getting the mean
mean_df = byComp.mean()

# Getting the sum
sum_df = byComp.sum()

# Getting the standard deviation
std_df = byComp.std()

# Getting the number of instances (Count)
count_df = byComp.count()

# Getting data for a specific company (ONE LINE)
fb_sales = df.groupby('Company').sum()['FB']
```

## Using Groupby with Describe Methods

Used to give an overview of all the statistical calculations for each company.

```py
df = df.groupby('Company').describe()
# Add .transpose() if you want the companies to be in the column
```

