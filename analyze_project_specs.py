
import numpy as np
import pandas as pd

fpath1 = 'D:\Dropbox\Dropbox\_machine_learning\__data_engineer_nanodegree\Project1'
df1 = pd.read_csv(fpath1 + '\event_datafile_new.csv')

print(df1.columns)
print(df1.head(2))

df1['location'] = df1['location'].apply(lambda x: x.replace(",",""))
df1['song'] = df1['song'].apply(lambda x: x.replace(",",""))

df1.to_csv(fpath1 + '\event_data_corrected.csv')