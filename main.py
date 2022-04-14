# Data Manipulation With Pandas
import pandas as pd
import numpy as np
df=pd.read_csv('hospitaled.csv')

np_weight=np.array(df['Weight'])
np_height=np.array(df['Height'])
df['Bmi']=np_weight/np_height**2
# column names
print(df.columns)
# Dataframe values in 2 dimensional numpy array
print(df.values)
# Quick view of what the dataframe looks like
print(df.head())
# Setting and sorting the index for easy slicing and subsetting
gen=df.set_index('Genotype').sort_index()
form=(gen.iloc[15:20])
print(form['Race'])
print(form)
print(form['Weight'].mean())
# groupby and describe method to perform summary statistics of the weight column
red=df.groupby(['Genotype', 'Sex'])['Weight'].describe()
print(red)
# loc function for subsetting
xnv=df.loc[:, ['Sex','Weight', 'Height', 'Bmi']]
print(xnv)

print(df[(df['Sex']=='Male') & (df['Race']=='Black')])
print(df[(df['Sex']=='Female') & (df['Race']=='White')])

# Grouped summary statistics using pivot table
gss=df.pivot_table(values=['Weight', 'Height', 'Bmi'], columns='Sex',index='Name', aggfunc=np.median, fill_value=0, margins=True)
print(gss)
# Slicing outer level index
oti=df.set_index(['Name'])
print(oti.loc['Ubaydah'])
# Slicing inner level index by passing list of tuples
ili=df.set_index(['Name', 'Sex']).sort_index()
lot=ili.loc[('Faith', 'Female') : ('Aisha', 'Female')]
print(lot)
# Using functions to perform custom summary statistics
def pct25 (column):
    return column.quantile(0.25)

def pct75 (column):
    return column.quantile(0.75)
css=df[['Weight', 'Height', 'Bmi']].agg([pct25, pct75])
print(css)
# Using isin method to subset babies of black or white race
print(df[df['Race'].isin(['Black', 'White'])])
