import random
import numpy

# updated 7 Nov 2019
weightDict = {
    1 : 11,
    2 : 22,
    3 : 16,
    4 : 17,
    5 : 16,
    6 : 15,
    7 : 21,
    8 : 16, 
    9 : 19,
    10: 14,
    11: 23,
    12: 8,
    13: 13,
    14: 16,
    15: 11,
    16: 14,
    17: 24,
    18: 13,
    19: 15,
    20: 19,
    21: 14,
    22: 22,
    23: 17,
    24: 17,
    25: 20,
    26: 11,
    27: 19,
    28: 14,
    29: 20,
    30: 17,
    31: 13,
    32: 17,
    33: 16,
    34: 17,
    35: 17
}

weightDictP = {
    1 : 0,
    2 : 4,
    3 : 8,
    4 : 5,
    5 : 3,
    6 : 4,
    7 : 6,
    8 : 4, 
    9 : 5,
    10: 3,
    11: 3,
    12: 4,
    13: 7,
    14: 3,
    15: 3,
    16: 3,
    17: 3,
    18: 1,
    19: 8,
    20: 5
}

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
pf = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lw = []
pw = []

l = [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35]
pl = [1, 3, 6, 7, 10, 11, 12, 13, 14, 17, 18, 19, 20]


# populate the weight for each member of l in lw
for x in X:
    lw.append(weightDict.get(x))

for x in pf:
    pw.append(weightDictP.get(x))

# shuffle the list
random.shuffle(X)

# shuffle the powerball list
random.shuffle(pf)

# Approximate decimal probability ["0.92", 0.436", "0.413", "0.132", "0.0177]
# Probabilities: 
# 5 low numbers: 0.02888567             ; Approximate predicted frequency in 100 draws: 2 to  3 times
# 4 low and 1 high: 0.15840529792509    ; Approximate predicted frequency in 100 draws: 15 to 16 times
# 3 low and 2 high: 0.326710926970499   ; Approximate predicted frequency in 100 draws: 32 to 33 times
# 2 low and 3 high: 0.31681059585018    ; Approximate predicted frequency in 100 draws: 31 to  32 times
# 1 low and 3 high: 0.144428359872876   ; Approximate predicted frequency in 100 draws: 14 times
# 5 high numbers : 0.0247591474067788   ; Approximate predicted frequency in 100 draws: 2 times

newLine = "\n"

############################################################################################################
# Step 1: Generate a list of pattern combiantions
# This generates two files of patterns generated and 2 file for the PB generated based on two approaches
# 1. one based on probabilityOfOccurrence
# 2. the other based on past draws weightage
############################################################################################################

f1 = open("thu/141119_A_4.txt", "a")
f2 = open("thu/141119_B_4.txt", "a")
f1b = open("thu/141119_A_PB_4.txt", "a")
f2b = open("thu/141119_B_PB_4.txt", "a")
for x in range (0, 80000000):
    probabilityOfOccurrence = 0.326710926970499
    probabilityOfOccurrencePB = 0.613
    # if occurence happens more than probabilityOfOccurrencePB% of the time
    pattern1 = str(sorted(random.sample(sorted([x for x in X if random.random() > probabilityOfOccurrence]), k=7)))
    pattern2 = str(sorted(random.choices(X, weights = lw, k = 7)))
    
    # if occurence happens less probabilityOfOccurrencePB% of the time
    pB1 = str(random.sample([x for x in pf if random.random() < probabilityOfOccurrencePB], k=1))
    pB2 = str(random.choices(pf, weights = pw, k = 1))

    f1.writelines([str(pattern1), newLine])
    #f1b.writelines([str(pB1), newLine])
    f2.writelines([str(pattern2), newLine])
    f1b.writelines([str(pB1), newLine])
    f2b.writelines([str(pB2), newLine])
    
f1.close()
f2.close()
f1b.close()
f2b.close()

############################################################################################################
# Step 2: Generate a list of indices to pick the combinations from
############################################################################################################
# Pattern 1
# generated from random.org
indicesPattern1 = [49134940, 6617868, 47739945, 7171041, 42775428, 79891384, 76714804, 11194881, 55362435, 19686036]

fpOneExtract = open("thu/141119_A_extract.txt", "a")

for r in range(len(indicesPattern1)):
    fpOne = open("thu/141119_A_4.txt", "r")
    for i, line in enumerate(fpOne):
        if i == indicesPattern1[r]:
            fpOneExtract.writelines([str(i), ":", line, newLine])
        else:
            continue
    fpOne.close()
fpOneExtract.close()

# Pattern 1b
# generated from random.org
indicesPattern1b = [33516054, 27063527, 5118498, 38073315, 25990691, 21591608, 9731373, 27233595, 70937671, 40310298]
fpOneBExtract = open("thu/141119_A_PB_extract.txt", "a")

for r in range(len(indicesPattern1b)):
    fpBOne = open("thu/141119_B_PB_4.txt", "r")
    for i, line in enumerate(fpBOne):
        if i == indicesPattern1b[r]:
            fpOneBExtract.writelines([str(i), ":", line, newLine])
        else:
            continue
    fpBOne.close()
fpOneBExtract.close()

# Pattern 2
indicesPattern2 = [79779220, 35452023, 62863039, 43601279, 37523615, 31468388, 76796719, 18637613, 29066850, 22527182]

fpTwoExtract = open("thu/141119_B_extract.txt", "a")

for r in range(len(indicesPattern2)):
    fpTwo = open("thu/141119_B_4.txt", "r")
    for i, line in enumerate(fpTwo):
        if i == indicesPattern2[r]:
            fpTwoExtract.writelines([str(i), ":", line, newLine])
        else:
            continue
    fpTwo.close()

fpTwoExtract.close()

# Pattern 2B
#for i in range (1, 10):
#    indicesPattern2 = str(random.sample(x for x in range(0,80000000) if random.random() > 0.326710926970499, k=1))
indicesPattern2B = [25950152, 79972004, 43051176, 64652211, 20272419, 22936854, 4745619, 47135653, 30612277, 33672206]

fpTwoBExtract = open("thu/141119_B_PB_extract.txt", "a")

for r in range(len(indicesPattern2B)):
    fpBTwo = open("thu/141119_B_PB_4.txt", "r")
    for i, line in enumerate(fpBTwo):
        if i == indicesPattern2B[r]:
            fpTwoBExtract.writelines([str(i), ":", line, newLine])
        else:
            continue
    fpBTwo.close()

fpTwoBExtract.close()

############################################################################################################
# Step 3: Pickup any combinations from the extracted results
############################################################################################################

    

