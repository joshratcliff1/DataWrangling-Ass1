import numpy as np
import statistics as s

L = [91, 7, 74, 14, 20, 32, 42, 55, 56, 84, 13, 42, 71, 99, 70, 4]
L.sort()
print(L)
print(len(L))
width_3 = (max(L) - min(L))/3
width_4 = (max(L) - min(L))/4
print("width3 is {}".format(width_3))
print("width4 is {}".format(width_4))

# Part 1
print("\nPart 1")
b_1_1 = L[0:8]
b_1_2 = L[8:]

#print(b_1_1)
b_1_1_m = int(s.median(b_1_1))
#print(b_1_1_m)
b_1_1 = [b_1_1_m for x in b_1_1]
print("Bin 1: {}".format(b_1_1))


#print(b_1_2)
b_1_2_m = s.median(b_1_2)
#print(b_1_2_m)
b_1_2 = [b_1_2_m for x in b_1_2]
print("Bin 2: {}".format(b_1_2))

# Part 2
print("\nPart 2")

b_2_1 = []
b_2_2 = []
b_2_3 = []

for num in L:
    if num < width_3:
        b_2_1.append(num)
    elif num < 2 * width_3:
        b_2_2.append(num)
    else:
        b_2_3.append(num)

b_2_1 = [s.mean(b_2_1) for x in b_2_1]
b_2_2 = [s.mean(b_2_2) for x in b_2_2]
b_2_3 = [s.mean(b_2_3) for x in b_2_3]

print("Bin 1: {}".format(b_2_1))
print("Bin 2: {}".format(b_2_2))
print("Bin 3: {}".format(b_2_3))

# Part 3
print("\nPart 3")

b_3_1 = []
b_3_2 = []
b_3_3 = []
b_3_4 = []

for num in L:
    if num < width_4:
        b_3_1.append(num)
    elif num < 2 * width_4:
        b_3_2.append(num)
    elif num < 3 * width_4:
        b_3_3.append(num)
    else:
        b_3_4.append(num)

# Update Bin 1 with Bin boundaries
new_bin = []
for num in b_3_1:
    if num < (b_3_1[0] + b_3_1[-1])/2:
        new_bin.append(b_3_1[0])
    else:
        new_bin.append(b_3_1[-1])
b_3_1 = new_bin

# Update Bin 2 with Bin boundaries
new_bin = []
for num in b_3_2:
    if num < (b_3_2[0] + b_3_2[-1])/2:
        new_bin.append(b_3_2[0])
    else:
        new_bin.append(b_3_2[-1])
b_3_2 = new_bin

# Update Bin 3 with Bin boundaries
new_bin = []
for num in b_3_3:
    if num < (b_3_3[0] + b_3_3[-1])/2:
        new_bin.append(b_3_3[0])
    else:
        new_bin.append(b_3_3[-1])
b_3_3 = new_bin

# Update Bin 4 with Bin boundaries
new_bin = []
for num in b_3_4:
    if num < (b_3_4[0] + b_3_4[-1])/2:
        new_bin.append(b_3_4[0])
    else:
        new_bin.append(b_3_4[-1])
b_3_4 = new_bin

print("Bin 1: {}".format(b_3_1))
print("Bin 2: {}".format(b_3_2))
print("Bin 3: {}".format(b_3_3))
print("Bin 4: {}".format(b_3_4))


# Part 4
print("\nPart 4")
b_4_1 = L[0:4]
b_4_2 = L[4:8]
b_4_3 = L[8:12]
b_4_4 = L[12:]

# Update Bin 1 with Bin boundaries
new_bin = []
for num in b_4_1:
    if num < (b_4_1[0] + b_4_1[-1])/2:
        new_bin.append(b_4_1[0])
    else:
        new_bin.append(b_4_1[-1])
b_4_1 = new_bin

# Update Bin 2 with Bin boundaries
new_bin = []
for num in b_4_2:
    if num < (b_4_2[0] + b_4_2[-1])/2:
        new_bin.append(b_4_2[0])
    else:
        new_bin.append(b_4_2[-1])
b_4_2 = new_bin

# Update Bin 3 with Bin boundaries
new_bin = []
for num in b_4_3:
    if num < (b_4_3[0] + b_4_3[-1])/2:
        new_bin.append(b_4_3[0])
    else:
        new_bin.append(b_4_3[-1])
b_4_3 = new_bin

# Update Bin 4 with Bin boundaries
new_bin = []
for num in b_4_4:
    if num < (b_4_4[0] + b_4_4[-1])/2:
        new_bin.append(b_4_4[0])
    else:
        new_bin.append(b_4_4[-1])
b_4_4 = new_bin

print("Bin 1: {}".format(b_4_1))
print("Bin 2: {}".format(b_4_2))
print("Bin 3: {}".format(b_4_3))
print("Bin 4: {}".format(b_4_4))