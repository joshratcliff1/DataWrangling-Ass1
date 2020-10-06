import numpy as np
import statistics as s

L = [91, 7, 74, 14, 20, 32, 42, 55, 56, 84, 13, 42, 71, 99, 70, 4]

L_mean = np.mean(L)

L_SD = np.std(L)
s_SD = s.pstdev(L)

L_median = np.median(L)

Lm = []
for num in L:
    Lm.append(abs(num-L_median))

L_mode = s.mode(L)
L_MAD = np.median(Lm)



print("Mean is {}".format(L_mean))
print("Standard Deviation is {}. Note this is treating the set as the full population, not a sample,".format(L_SD))
print("Median is {}".format(L_median))
print("Median Absolute Deviation is {}".format(L_MAD))
print("Mode is {}".format(L_mode))




#print("stats SD is {}".format(s_SD))

