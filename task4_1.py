import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sps
import datetime

# show complete records by changing rules
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv("data_wrangling_medical_2020_u7199704.csv")

# Part 1

