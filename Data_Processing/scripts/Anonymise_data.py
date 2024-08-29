import pandas as pd
import hashlib
import os

"""
    Anonymize 2 GB of data using pandas 
    Pandas chunk techinque

"""

partiton_size       = 100000
anonymise_data_path = os.path.abspath("Data_Processing/files/anonymised_data.csv")
csv_path            = os.path.abspath("Data_Processing/files/Random_data.csv")

def anonymize(value):
    '''
        sha256 technique to anonymize data
    
        Args:
            value : value to be hashed

        Returns:
            Hashed value
    '''

    value = str(value)
    hashed = hashlib.sha256(value.encode()).hexdigest()
    return hashed


def anonymise_data(csv_data_file_path = csv_path,anonymized_path= anonymise_data_path,chunk=partiton_size):
    
    '''
        Anonymize data by reading random file and generates anonymized csv formatted file
    
        Args:
            csv_data_file_path      : path of csv file 
            anonymized_path         : path to store anonymized data

        Returns:
            None 
    '''

    # read csv chunks
    with pd.read_csv(csv_data_file_path,chunksize=chunk) as partition_df:
        for idx, df in enumerate(partition_df):
            # Anonymize the specified column
            df['first_name']     = df['first_name'].apply(anonymize)
            df['last_name']      = df['last_name'].apply(anonymize)
            df['address']        = df['address'].apply(anonymize)

            # Write the anonymized chunk to CSV file
            if idx ==0:
                mode ='w'
                is_header = True
            else:
                mode= 'a'
                is_header = False

            df.to_csv(anonymized_path, mode=mode, header=is_header, index=False)

if __name__ == "__main__":
    anonymise_data(csv_path,anonymise_data_path,partiton_size)
