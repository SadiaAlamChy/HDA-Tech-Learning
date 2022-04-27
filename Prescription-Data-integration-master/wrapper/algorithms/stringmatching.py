from fuzzywuzzy import fuzz
# import fuzzy
from pyphonetics import Soundex, FuzzySoundex
from pyphonetics import Metaphone, Lein
from pyphonetics import RefinedSoundex, MatchingRatingApproach
import numpy as np

context_char=[['J', 'Z', 'G'], ['W', 'O', 'U'], ['E', 'I'], ['K', 'Q']]

class PhoneticsMatiching:
    def __init__(self):
        self.soundex = Soundex()
        self.fz_soundex = FuzzySoundex()
        self.metaphone = Metaphone()
        self.rs = RefinedSoundex()

    def soundex_comparison(self, str1, str2):
        '''
        :param str1:
        :param str2:
        :return: Soundex(str1), Soundex(str2) and Soundex matching (True/False)
        '''
        # p1 = self.soundex.phonetics(str1)
        # p2 = self.soundex.phonetics(str2)
        # print(str1, str2)
        return self.soundex.sounds_like(str1, str2)

    def fuzzy_soundex_comparison(self, str1, str2):
        '''
        :param str1:
        :param str2:
        :return: FuzzySoundex(str1), FuzzySoundex(str2) and FuzzySoundex matching (True/False)
        '''
        p1 = self.fz_soundex.phonetics(str1)
        p2 = self.fz_soundex.phonetics(str2)
        return p1, p2, self.fz_soundex.sounds_like(str1, str2), self.distance(p1, p2), \
               self.distance_lev(p1, p2)

    def metaphone_comparison(self, str1, str2):
        p1 = self.metaphone.phonetics(str1)
        p2 = self.metaphone.phonetics(str2)
        return self.distance_lev(p1, p2)

    def distance(self, str1, str2):
        return self.rs.distance(str1, str2)

    def distance_lev(self, str1, str2):
        return self.rs.distance(str1, str2, metric='levenshtein')

    def distance_ham(self, str1, str2):
        if(len(str1) == len(str2)):
            return self.rs.distance(str1, str2, metric='hamming')
        else:
            return None

    def test(self, str1, str2):
        str1 = str1.strip()
        str1_l = str1.split()
        for st in str1_l:
            if(self.soundex_comparison(st, str2)):
                return 1
        for st in str1_l:
            if(self.metaphone_comparison(st, str2) <=1):
                return 1
        return 0
        #
        # print( str1, ' vs ', str2)
        # print('SND: ', self.soundex_comparison(str1, str2))
        # print('FSND: ', self.fuzzy_soundex_comparison(str1, str2))
        # print('META: ',self.metaphone_comparison(str1, str2))
        # return 0

def name_matching(name1, name2):
    try:
        soundex_list=[]
        name_list=[]
        # name1= name1. replace('.',' ')
        # name2= name2.replace('.', ' ')
        name1_l = [name1]
        name2_l = [name2]
        fuzz_matrix=get_fuzzy_matrix(name1_l,name2_l) # all possible subname 2D matrix
        # print(fuzz_matrix)
        # print(fuzz_matrix.shape)
        if(fuzz_matrix.shape[0]>fuzz_matrix.shape[1]): # column has minimum sub name
            maxInColumns = np.amax(fuzz_matrix, axis=0)  # find max ratio in particular column
            # print(maxInColumns)
            row_index=fuzz_matrix.argmax(axis=0)
            # print(row_index)
            avg_ratio= np.sum(maxInColumns)/ fuzz_matrix.shape[1]
            # print(avg_ratio)
            # for i in range(len(row_index)):
            #     soundex_list.append(soundex_matching(name1_l[row_index[i]], name2_l[i])) # Boolian sound list
            #     name_list.append(name1_l[row_index[i]]+ ' VS ' +name2_l[i]) # corresponding name list
        # row has minimum sub name
        else:
            maxInRows = np.amax(fuzz_matrix, axis=1) # find max ratio in particular row
            # print(maxInRows)
            # col_index = fuzz_matrix.argmax(axis=1)
            # print(col_index)
            avg_ratio = np.sum(maxInRows) / fuzz_matrix.shape[0]
            # print(avg_ratio)
            # for i in range(len(col_index)):
            #     soundex_list.append(soundex_matching(name1_l[i], name2_l[col_index[i]]))
            #     name_list.append(name1_l[i]+' VS '+ name2_l[col_index[i]])
        # print(soundex_list, avg_ratio)
        return avg_ratio
    except:
        return 0.00



def fuzzy_matching(str1,str2):
    try:
        return fuzz.ratio(str1.lower(),str2.lower())
    except:
        return 0.0

### 2D matrix of all subname combination
def get_fuzzy_matrix(name1, name2):
    ratio_matrix = []
    # print(name1, name2)
    for i in range(len(name1)):
        temp=[]
        for j in range(len(name2)):
            temp.append(fuzzy_matching(name1[i], name2[j]))
        ratio_matrix.append(temp)
    ratio_matrix = np.array(ratio_matrix)
    return ratio_matrix

## Phonetic algorithm eg. soundex and NYSIIS
def soundex_matching(name1, name2):
    soundex = Soundex()
    # print(name1, name2)
    if (soundex.sounds_like(name1, name2)):
        return 1
    soundex1 = fuzzy.nysiis(name1)
    soundex2=fuzzy.nysiis(name2)
    # print(soundex1, soundex2)
    lev_distance=levenshtein(soundex1,soundex2) # edit distance between two phonetics
    # print(soundex1, soundex2, lev_distance)
    if(lev_distance==0):
        return 1
    elif(lev_distance==1 and check_context_char(soundex1[0],soundex2[0])):
        return 1
    else:
        return 0
### cross check with context_char[]
def check_context_char(char1, char2):
    if (char1 == char2):
        return True
    for context in context_char:
        if(char1 in context and char2 in context):
            return True
    return False

### To find the edit distance between two string.
### DP based
### time complexity O(mn)
def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    # print (matrix)
    return (matrix[size_x - 1, size_y - 1])