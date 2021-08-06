import random

# updated 5 Nov 2019
weightDict = {
    1 : 115,
    2 : 126,
    3 : 122,
    4 : 111,
    5 : 120,
    6 : 115,
    7 : 134,
    8 : 105, 
    9 : 112,
    10: 83,
    11: 100,
    12: 112,
    13: 107,
    14: 104,
    15: 118,
    16: 120,
    17: 121,
    18: 103,
    19: 118,
    20: 117,
    21: 111,
    22: 123,
    23: 113,
    24: 101,
    25: 127,
    26: 120,
    27: 128,
    28: 130,
    29: 118,
    30: 107,
    31: 105,
    32: 106,
    33: 134,
    34: 110,
    35: 120,
    36: 111,
    37: 126,
    38: 97,
    39: 106,
    40: 114,
    41: 111,
    42: 99,
    43: 116,
    44: 108,
    45: 127
}

f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 41, 43, 44, 45]
lw = []

# populate the weight for each member of l in lw
for x in f:
    lw.append(weightDict.get(x))
    
    
##############################################################################################################################
# Step 1: Generate a list of random combinations based on past draws weightage
##############################################################################################################################
# f1 = open("tue/051119_A_check.txt", "a")
f2 = open("tue/051119_B_check4.txt", "a")
f3 = open("tue/051119_C_check4.txt", "a")
index = 0

# shuffle the list
random.shuffle(f)

for x in range (0, 9930000):
    index = index + 1
    # pattern1 = str(sorted(random.sample(f, k=7)))
    # if pattern1 == "[4, 8, 23, 24, 30, 36, 42]":
    #    print("match found using pattern1 at index", index)
    
    # random.random() - This number is used to generate a float random number less than 1 and greater or equal to 0
    pattern2 = str(sorted(random.sample(sorted([x for x in f if random.random() > 0.413]), k=7)))
    if pattern2 == "[4, 8, 23, 24, 30, 36, 42]":
        print("match found using pattern2 at index", index)

    pattern3 = str(sorted(random.choices(f, weights = lw, k = 7)))
    if pattern3 == "[4, 8, 23, 24, 30, 36, 42]":
        print("match found using pattern3 at index", index)
    
    newLine = "\n"
    
    #f1.writelines([str(pattern1), newLine])
    f2.writelines([str(pattern2), newLine])
    f3.writelines([str(pattern3), newLine])
    
    	
#f1.close()
f2.close()
f3.close()
