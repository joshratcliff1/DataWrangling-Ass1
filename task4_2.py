import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sps
import datetime

df = pd.read_csv("data_wrangling_medical_2020_u7199704.csv")

# Part 2

# Calculate Pearson Correlations
print("Pearson correlation for bmi and age at consulation is {}".format(df['bmi'].corr(df['age_at_consultation'])))
print("Pearson correlation for bmi and height is {}".format(df['bmi'].corr(df['height'])))
# print("Pearson correlation for state and marital status is {}".format(df['state'].corr(df['marital_status'])))

#print(df.marital_status[:20])

'''https://www.kaggle.com/kuldeepnpatel/chi-square-test-of-independence'''

# Contingency Table
contingency_table=pd.crosstab(df.state,df.marital_status)
# print('contingency_table :-\n',contingency_table)


# Observed Values
Observed_Values = contingency_table.values
# print("Observed Values :-\n",Observed_Values)

# Expected Values
b = sps.chi2_contingency(contingency_table)
Expected_Values = b[3]
# print("Expected Values :-\n",Expected_Values)

# chi-square statistic - χ2
chi_square = sum([(o-e)**2./e for o,e in zip(Observed_Values,Expected_Values)])
# print(chi_square)
chi_square_statistic = sum(chi_square)
# print("chi-square statistic:-",chi_square_statistic)

# Calculate n
pre_n = sum([o for o in Observed_Values])
n = sum(pre_n)
# print("n:", n)

cramer_V = (chi_square_statistic/n/5)**0.5
print('V:',cramer_V)

