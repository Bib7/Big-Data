
# coding: utf-8

# In[1]:

# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'imd_student_blind.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)


# In[10]:

# Load a sheet into a DataFrame by index: df
df = xl.parse(0)

# Print the head of the DataFrame df
df.head()


# In[3]:

df.columns


# In[4]:

df.shape


# In[40]:

id_by_year = df.groupby('ano_ingresso')['a_ID'].count()
id_by_year


# In[36]:

from bokeh.charts import Bar, Histogram, output_notebook, show

p = Bar(id_by_year, values='a_ID', title="ID por ano", color='a_ID')

output_notebook()

show(p)


# In[ ]:



