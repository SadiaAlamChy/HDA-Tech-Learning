import math
import re
import hashlib
from datetime import datetime

import pandas as pd

SHIFT_PATTERN = 4
CONTEXT=['j z g', 'o w u', 'i e', 'k q']
VOWEL = ['a', 'e', 'i', 'o', 'u']
SALUTAION = ['mr', 'miss', 'mrs', 'mst', 'md', 'dr', 'prof', 'ms', 'master', 'baby']
RE_SALUTAION = re.compile("^(mr|mrs|miss|dr|prof|md|mst|ms|master|engr|engg|baby|[a-z](\.|\s))[\.\s]*")
RE_YEAR = re.compile(r"\d\d\d\d")
class KSRL:
    def __init__(self, name, dob, gender, x):
        self.name= name
        self.dob = dob
        # self.phone_number = phone_number.strip()
        self.gender = gender.strip()
        self.x = x
    def removeSalutation(self):
        self.name = self.name.lower().strip()
        while(True):
            if(not RE_SALUTAION.search(self.name) == None):
                self.name = re.sub("^(mr|mrs|miss|dr|prof|md|mst|ms|master|engr|engg|baby|[a-z](\.|\s))[\.\s]*", " ", self.name).strip()
            else:
                break
    def removeVowelAndMap(self):
        self.unambigious_name = ''
        name_list = self.name.split()
        for n_part in name_list:
            first_letter = n_part[0]
            for contex in CONTEXT:
                if (first_letter in contex):
                    first_letter = contex[0]
            n_part = first_letter + re.sub(r"a|e|i|o|u", '', n_part[1:])
            self.unambigious_name += n_part + ' '

    def get_birth_year(self):
        try:
            # print(self.dob, type(self.dob))
            if(RE_YEAR.search(self.dob) != None):
                # print('case1')
                birth_year = RE_YEAR.search(self.dob).group(0)
                # print(birth_year)
                return birth_year
            elif(not math.isnan(self.x.age_yy)):
                # print('case2')
                reg_year = RE_YEAR.search(self.x.reg_date).group(0)
                birth_year = int(reg_year) - int(self.x.age_yy)
                return birth_year
            else:
                # print('case3')
                return RE_YEAR.search(self.x.reg_date).group(0)
        except Exception as e:
            print(e)
            # print(self.x)
            # reg_year = RE_YEAR.search(self.x.reg_date).group(0)
            # birth_year = int(reg_year) - int(self.x.age_yy)
            # print(birth_year)
            # return str(birth_year)


    def unambiguous_gender_birthyear(self):
        gender_up = self.gender.upper()
        birth_year_range = str(int(self.get_birth_year())-2) + '-' + str(int(self.get_birth_year())+2)
        return gender_up+birth_year_range

    def encrypt(self, text, s):
        result = ""
        # transverse the plain text
        for i in range(len(text)):
            char = text[i]
            result += chr((ord(char) + s - 97) % 26 + 97)
        return result

    def getPIK(self):
        self.removeSalutation()
        self.removeVowelAndMap()
        hashlib.md5("whatever your string is".encode('utf-8')).hexdigest()
        part1 = hashlib.md5(self.unambiguous_gender_birthyear().encode('utf-8')).hexdigest()
        part2 = hashlib.md5(self.unambigious_name.encode('utf-8')).hexdigest()
        # part3 = hashlib.md5(self.phone_number.encode('utf-8')).hexdigest()
        # part1 = self.encrypt(self.unambiguous_gender_birthyear(), 4)
        # part2 = self.encrypt(self.unambigious_name, 4)
        # part3 = self.encrypt(self.phone_number, 10)
        # print(len(part1), len(part2), len(part3))
        # print(part1 + "#" + part2 + "#" + part3)
        return  part1+part2


if __name__ == '__main__':
    dt =KSRL('M . A. HANNAN IQBAAL', '1936-12-13', "M", pd.DataFrame)
    print(dt.getPIK())
    dt = KSRL('Md. HANNAN EQBAL', '1936-12-13', "M", pd.DataFrame)
    print(dt.getPIK())
    # qrrrrmufpr
