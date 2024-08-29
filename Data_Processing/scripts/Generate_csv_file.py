import random
from datetime import timedelta,datetime
import csv
import os
from sys import exit

csv_path = os.path.abspath("Data_Processing/files/Random_data.csv")

def generate_randon_data(Total_rows = 50000,random_data_path = csv_path,
                         header_data = ['first_name','last_name','address','date_of_birth']):
    '''
        Generates random data using the random in Python  
    
        Args:
            Total_rows          : Number of rows of random data 
            random_data_path    : Path to the randomly generated data file
            header_data         : column names of header must be 4 column

        Returns:
            None 
                - Prints Error and exit / Success message 
    '''

    print("Adding Random data")
    # generate first_name
    agg_first_names     = gen_random_names(Total_rows) 
    
    # generate last_name
    agg_last_names      = gen_random_names(Total_rows)

    # address
    agg_address         = gen_random_address(Total_rows)

    # dob
    agg_dob             = gen_random_dob(Total_rows)
    
    # validation check
    if not os.path.exists(os.path.dirname(random_data_path)):
        print(f"Error\t: Path {random_data_path} does not exists")
        exit()
    if len(header_data)!= 4:
        print("Error\t:Incorrect columns names in header data only 4 columns are allowed")
        exit()
    # open the csv file 
    with open(random_data_path,'w',encoding='utf-8',newline='') as random_file_pat:
        csv_writer = csv.writer(random_file_pat)
        csv_writer.writerow(header_data)
        for idx in range(Total_rows):
            csv_row = [agg_first_names[idx],agg_last_names[idx],agg_address[idx],agg_dob[idx]]
            csv_writer.writerow(csv_row)
    print(f"\nGenerated file at location {random_data_path}")    

def gen_random_names(No_rows):

    '''
        Generates random names  
    
        Args:
            No_rows: Number of random name rows 
        Returns:
            [] list of names 
    '''

    start_index = 0
    Names       = []
    while start_index < No_rows:
        len_name = random.randint(3,7)
        Name = ''
        for _ in range(len_name):
            number = random.randint(65,65+25)
            Name += chr(number)
        Names.append(Name.title())
        start_index+=1
    return Names
    
def gen_random_address(No_rows):
    
    '''
        Generates random address  
    
        Args:
            No_rows: Number of random name rows 
        Returns:
            [] list of addresses 
    '''

    useful_keywords =['Street','Lane','Street Road','Avenue']
    Addresses   = []
    house_no    = [f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}" for _ in range(No_rows)]
    Address     = gen_random_names(No_rows)
    Lane_2      = [random.choice(useful_keywords) for i in range(No_rows)]
    zipcode     = [f"{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}" for _ in range(No_rows)]

    for H_No,add,lane,zipcode in zip(house_no,Address,Lane_2,zipcode):
        Addresses.append(f'{H_No} {add} {lane} {zipcode}')
    return Addresses

def gen_random_dob(No_rows):
    
    '''
        Generates random data of births  
    
        Args:
            No_rows: Number of random name rows 
        Returns:
            [] list of names 
    '''

    start_date      = datetime(1960,1,1)
    end_date        = datetime(2023,12,31)
    date_range      = end_date - start_date
    date_of_births  = []
    for _ in range(No_rows):
        rnd_date = start_date + timedelta(days =random.randint(0,date_range.days))
        date_of_births.append(rnd_date)
    return date_of_births

if __name__ == "__main__":

    generate_randon_data(100)
    # generate_randon_data(10000000)