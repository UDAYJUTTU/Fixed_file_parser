from scripts.Generate_csv_file import *
from scripts.Anonymise_data  import *
from scripts.Anonymise_big_data import *


csv_path                = os.path.abspath("Data_Processing/files/Random_data.csv")
anonymise_data_path     = os.path.abspath("Data_Processing/files/anonymised_data.csv")
anonymise_big_data_path = os.path.abspath("Data_Processing/files/anonymised_big_data_file.csv")

generate_randon_data()
anonymise_data()
process_big_data()