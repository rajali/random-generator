import random

# updated 7 Nov 2019
weightDict = {
    1 : 268,
    2 : 207,
    3 : 241,
    4 : 217,
    5 : 253,
    6 : 242,
    7 : 250,
    8 : 247, 
    9 : 235,
    10: 224,
    11: 253,
    12: 253,
    13: 228,
    14: 208,
    15: 237,
    16: 243,
    17: 211,
    18: 260,
    19: 245,
    20: 229,
    21: 238,
    22: 252,
    23: 224,
    24: 239,
    25: 251,
    26: 244,
    27: 226,
    28: 212,
    29: 230,
    30: 213,
    31: 240,
    32: 237,
    33: 246,
    34: 226,
    35: 215,
    36: 245,
    37: 229,
    38: 238,
    39: 224,
    40: 252,
    41: 250,
    42: 248,
    43: 230,
    44: 209,
    45: 227
}

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 41, 43, 44, 45]

lw = []

l = [1,2,3,4,5,6,7,10,11,12,15,16,20,21,22,23,24,29,30,33,36,40,41,43,44,45]

# populate the weight for each member of l in lw
for x in X:
    lw.append(weightDict.get(x))
    
# Approximate decimal probability ["0.92", 0.436", "0.413", "0.132", "0.0177]
newLine = "\n"

# Open files for appending data
f1 = open("sat/091119_pattern2_5.txt", "a")
f2 = open("sat/091119_pattern3_5.txt", "a")

########################################################################################################################
# Step A: Create random combinations based on two criteria (past draws weightage, and just random pick)
########################################################################################################################
for x in range (0, 80000000):
  
    # if occurence happens more than probabilityOfOccurrencePB% of the time
    patternOne = str(sorted(random.sample(sorted([x for x in X if random.random() > 0.326710926970499]), k=6)))
    
    # Pattern generated based on the weightage / past draws
    patternTwo = str(sorted(random.choices(X, weights = lw, k = 6)))
    
    # writing random number pattern to file.
    f1.writelines([str(patternOne), newLine])
    f2.writelines([str(patternTwo), newLine])

# Close files
f1.close()
f2.close()

########################################################################################################################
# Step B: create random index generator, this will be used in the loop below to pick ten numbers from the above generated combinations
########################################################################################################################
# Pattern 1
# generated from random.org (between range (0, 80000000)
indicesPattern = [898669, 700830, 919263, 6714777, 44033390, 38171568, 48679414, 62836115, 66616355, 70444747]

# Pattern 2
for i in range (1, 10):
  indicesPattern2 = str(random.sample(x for x in range(0,80000000) if random.random() > 0.326710926970499, k=1))

########################################################################################################################
# Step C: Pick up number combinations at the above generated indices
########################################################################################################################
fpOneExtract = open("sat/091119_B_extract2.txt", "a")

# From Pattern 1 file
for r in range(len(indicesPattern)):
    fpOne = open("sat/091119_pattern2_5.txt", "r")
    for i, line in enumerate(fpTwo):
        if i == indicesPattern[r]:
            fpOneExtract.writelines([str(i), ":", line, newLine])
        else:
            continue
    fpOne.close()
fpOneExtract.close()


# From pattern 2 file
fpTwoExtract = open("sat/091119_C_extract2.txt", "a")

for r in range(len(indicesPattern2)):
    fpTwo = open("sat/091119_pattern3_5.txt", "r")
    for i, line in enumerate(fpTwo):
        if i == indicesPattern3[r]:
            fpTwoExtract.writelines([str(i), ":", line, newLine])
        else:
            continue
    fpTwo.close()

fpTwoExtract.close()

########################################################################################################################
# Step D: Now you can pickup number from a shortlist found in either of 091119_C_extract2.txt or 091119_B_extract2 files
########################################################################################################################


