import pandas as pd
from wrapper.algorithms.KSRL import KSRL
DATA_DIR = "/home/raihan/NCDW/dataset/Prescription_Data"

class Extract:
    def __init__(self):
        self.data_df = pd.read_excel(DATA_DIR+ "/prescription_data_with_pat_info.xlsx")
    def anonymization(self):
        print(self.data_df.columns)
        self.data_df['DOB'] = self.data_df['DOB'].astype(str)
        self.data_df['GENDER_DATA'] = self.data_df['GENDER_DATA'].apply(lambda x: 'M' if x=="Male" else "F")
        self.data_df['PIK'] = self.data_df.apply(
            lambda x: KSRL(x.PATIENT_NAME, x.DOB, x.GENDER_DATA, x).getPIK(), axis=1)
        self.data_df.drop('PATIENT_NAME', axis=1, inplace=True)
        print(self.data_df.head)

if __name__ == '__main__':
    extract = Extract()
    extract.anonymization()
    extract.data_df.to_csv("../dataset/anonymized_prescription_dataset_mysoft.csv", index=False)

