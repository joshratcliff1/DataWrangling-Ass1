import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sps
import datetime
from math import log10

# show complete records by changing rules
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv("data_wrangling_medical_2020_u7199704.csv")


# Calculate first digits for the target attributes
df['cl_fd'] = df.cholesterol_level.astype(str)
df['cl_fd'] = df['cholesterol_level'].astype('|S')
df['cl_fd'] = df.cl_fd.str[0:1].astype(int)

df['bp_fd'] = df.blood_pressure.astype(str)
df['bp_fd'] = df['blood_pressure'].astype('|S')
df['bp_fd'] = df.bp_fd.str[0:1].astype(int)

df['mc_fd'] = df.medicare_number.astype(str)
df['mc_fd'] = df['medicare_number'].astype('|S')
df['mc_fd'] = df.mc_fd.str[0:2].astype(int)

# Check to makre sure we're getting the right first digits
# print(df[['cholesterol_level','cl_fd','blood_pressure','bp_fd', 'medicare_number', 'mc_fd']][0:8])





loop_items = ['cl_fd', 'bp_fd', 'mc_fd']
rows = 20000

for item in loop_items:
    rows = 20000
    print(df[item].value_counts())
    print("")
    values = list(df[item].value_counts())
    order = df[item].value_counts().index.tolist()
    # print(values)
    # print(order)

    zip_mc = zip(order, values)
    result = sorted(list(zip_mc))
    print(result)

    percent = [x[1]*100/rows for x in result]
    print(percent)
    print(sum(percent))








# x = [i for i in range(1, 10)]
# plt.bar(x, Lf)
# plt.xticks(x, x)
# plt.show()

'''
def benford(n):
    return log10(n+1) - log10(n)


x = [i for i in range(1, 10)]
results = [benford(i) for i in x]

fig, ax = plt.subplots()
plt.bar(x, results)
plt.xticks(x, x)
plt.show()
'''


# print(df.cholesterol_level)
# print(df['cholesterol_level'].value_counts())

