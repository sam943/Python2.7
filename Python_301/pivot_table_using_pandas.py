# pip install pandas
# Panda is data analytics module for python
import datetime as dt
import pandas as pd
import numpy as np

# setup a data frame, which is similar to excel sheet
df = pd.read_csv("temps.csv")
#print df.head()
# using a lambda function to convert into datetime column
df['CDT'] = df['CDT'].apply(lambda x: dt.datetime.strptime(x,'%Y-%m-%d'))

# Lets create a pivot table out for monthly average tempuratures
print pd.pivot_table(df, index=[df['CDT'].apply(lambda x: dt.datetime.strftime(x,'%B'))], values=["Mean TemperatureF"], aggfunc=np.average)

