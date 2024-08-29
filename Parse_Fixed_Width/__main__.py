import argparse
import os
from scripts.utils import *
from testing.Parse_fix_wid_test import unittest
# print(os.getcwd())

'''
    Default paths
'''
fix_len_file_name       = 'fixed_width'
spec_path               = os.path.abspath("Parse_Fixed_Width/input/spec.json")
fixed_width_file_path   = os.path.abspath(f'Parse_Fixed_Width/output/{fix_len_file_name}.txt')
records_file            = os.path.abspath('Parse_Fixed_Width/input/records.json')
parsed_csv_file         = os.path.abspath(f'Parse_Fixed_Width/output/{fix_len_file_name}.csv')


'''
    Arg parse overwrites defaults if any arguments are passed
'''
arg_parser = argparse.ArgumentParser()
arg_parser.usage  = """

    Program uses Spec.json file Columns and offsets to create Fixed Width & CSV file
    to add records data into with Spec file use "records.json" file in input folder 
    to provide the records

    Optional args:
        -sf spec_json_path(str)           : Path to spec.json file / update spec.json in input folder 
        -rf records_path(str)             : path to records.json file / update records.json in input Folder
        -fwf fixed_width_file_path(str)   : path to fixed_width file 
        -fcf csv_file_path(str)           : path to fixed_width file 
    
    Default:
        spec_json_path(str)     : Uses spec.json file in input Folder
        records_path(str)       : Uses records.json file in input Folder
        fixed_width_file_path   : Stores as Fixed_width.txt in output folder
        csv_file_path           : Stores as fixed_width.csv in output folder

"""
arg_parser.add_argument('-sf','--spec_json_path', type=str, nargs='*',default='')
arg_parser.add_argument('-rf','--records_path', type=str, nargs='*',default='')
arg_parser.add_argument('-fwf','--fixed_width_file_path', type=str, nargs='*',default='')
arg_parser.add_argument('-fcf','--csv_file_path', type=str, nargs='*',default='')

args = arg_parser.parse_args()
'''
    overwriting if args provided
'''
# spec json
if len(args.spec_json_path)>0:
    if type(args.spec_json_path) is list:
        args.spec_json_path = args.spec_json_path[0]
    os.path.exists(args.spec_json_path)
    spec_path = args.spec_json_path

# records
if len(args.records_path)>0:
    if type(args.records_path) is list:
        args.records_path = args.records_path[0]
    os.path.exists(args.records_path)
    records_file = args.records_path

# Fixed width path
if len(args.fixed_width_file_path)>0:
    if type(args.fixed_width_file_path) is list:
        args.fixed_width_file_path = args.fixed_width_file_path[0]    
    print(args.fixed_width_file_path)
    os.path.exists(os.path.dirname(args.fixed_width_file_path))
    fixed_width_file_path = args.fixed_width_file_path

# csv path
if len(args.csv_file_path)>0:
    if type(args.csv_file_path) is list:
        args.csv_file_path = args.csv_file_path[0]
    os.path.exists(os.path.dirname(args.csv_file_path))
    parsed_csv_file = args.csv_file_path

print("spec_path\t\t", spec_path)
print("records_file\t\t", records_file)
print("fixed_width_file_path\t", fixed_width_file_path)
print("parsed_csv_file\t\t", parsed_csv_file)

main(sp_path=spec_path,fwf_path=fixed_width_file_path,csv_path=parsed_csv_file,rec_path=records_file) # change records parameter accordingly