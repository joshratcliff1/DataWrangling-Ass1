import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sps
import datetime

# show complete records by changing rules
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv("data_wrangling_medical_2020_u7199704.csv")

print(df.isna().sum())

print(df.isnull().sum(axis = 0))






df['birth_date'] = pd.to_datetime(df.birth_date,format="%d/%m/%Y")
df['consultation_timestamp'] = df.consultation_timestamp.str[0:10]
df['consultation_timestamp'] = pd.to_datetime(df.consultation_timestamp,format="%Y-%m-%d")

df['age_at_consultation'] = df.age_at_consultation * 365.25
df['age_at_consultation'] = pd.to_timedelta(df['age_at_consultation'], unit='D')

df['birth_date_age'] = df['consultation_timestamp'] - df['birth_date']
df['date_delta'] = df['age_at_consultation'] - df['birth_date_age']

# print(df[['age_at_consultation', 'birth_date','consultation_timestamp', 'birth_date_age', 'date_delta']][0:10])

df_right_age = df[datetime.timedelta(0,0,0,0,0,0,0) <= df.date_delta]
df_right_age = df_right_age[df.date_delta < datetime.timedelta(365,0,0,0,0,0,0)]

# print(df_right_age[['age_at_consultation', 'birth_date','consultation_timestamp', 'birth_date_age', 'date_delta']][0:100])

rows = len(df)
age_consistency = len(df_right_age) / rows

print("age_consistency: ", age_consistency)
# df['consultation_timestamp'] = pd.to_datetime(df['consultation_timestamp'],format="%Y-%m-%d")
# print(df[['age_at_consultation', 'birth_date','consultation_timestamp', 'birth_date_age']][0:5])
