import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.utils import *


class test_fixed_length(unittest.TestCase):

    def setUp(self):
        '''
            File path to Generate test files
        '''
        self.test_overflow   = os.path.abspath(f'Parse_Fixed_Width/testing/test_overflow.txt')
        self.test_data       = os.path.abspath(f'Parse_Fixed_Width/testing/test_data.txt')
        self.test_under      = os.path.abspath(f'Parse_Fixed_Width/testing/test_under.txt')
        self.test_empty      = os.path.abspath(f'Parse_Fixed_Width/testing/test_empty.txt')        


    def tearDown(self):
        '''
            Clean up remove files 

        '''
        if os.path.exists(self.test_overflow):
            os.remove(self.test_overflow)
        
        if os.path.exists(self.test_data):
            os.remove(self.test_data)

        if os.path.exists(self.test_under):
            os.remove(self.test_under)

        if os.path.exists(self.test_empty):
            os.remove(self.test_empty)


    def test_col_overflow_offset(self):
        # Test Fixed length when len(col)> offset
        dummy_spec = {
            "ColumnNames": ["FullName", "Designation", "Age"],
            "Offsets": ["5", "12", "3"],
            "FixedWidthEncoding": "windows-1252",
            "IncludeHeader": "True",
            "DelimitedEncoding": "utf-8"
        }
        mt_data = get_metadata_from_spec(dummy_spec)
        generate_fixed_length_file(self.test_overflow,mt_data)
        # read the file
        with open(self.test_overflow,'r',encoding=dummy_spec['DelimitedEncoding']) as file:
            line = file.readlines()
        self.assertEqual(line[0].strip(),'FullNDesignation Age')


    def test_fixed_width_data(self):
        # Test Fixed length file when data is paseed
        
        dummy_spec = {
            "ColumnNames": ["FullName", "Designation", "Age"],
            "Offsets": ["5", "12", "3"],
            "FixedWidthEncoding": "windows-1252",
            "IncludeHeader": "True",
            "DelimitedEncoding": "utf-8"
        }
        mt_data = get_metadata_from_spec(dummy_spec)
        data = [{
                "FullName" : "Alfred",
                "Designation" : "Assistant",
                "Age" : "75"
            },
            {
                "FullName" : "James Gordan",
                "Designation" : "Cop",
                "Age" : "45"
            },
            {
                "FullName" : "Dracula",
                "Designation" : "",
                "Age" : "1450"
            }]
            
        generate_fixed_length_file(self.test_data,mt_data,records=data)
        # read the file
        with open(self.test_data,'r',encoding=dummy_spec['DelimitedEncoding']) as file:
            line = file.readlines()
        self.assertEqual(line,['FullNDesignation Age\n', 'AlfreAssistant   75 \n', 'JamesCop         45 \n', 'Dracu            145\n'])


    def test_col_under_offset(self):
        # Test Fixed length file when Len(cols) < Offset

        dummy_spec = {
            "ColumnNames": ["Name",'Address','State','Zipcode'],
            "Offsets": ["5", "12",'5', "30"],
            "FixedWidthEncoding": "windows-1252",
            "IncludeHeader": "True",
            "DelimitedEncoding": "utf-8"
        }
        data = [{"Name" : "Bob","Address" : "Boardway","State" : "TN","Zipcode":'37027'}]
        mt_data = get_metadata_from_spec(dummy_spec)
        generate_fixed_length_file(self.test_under,mt_data,records=data)
        # read the file
        with open(self.test_under,'r',encoding=dummy_spec['DelimitedEncoding']) as file:
            line = file.readlines()
        self.assertEqual(line,['Name Address     StateZipcode                       \n', 'Bob  Boardway    TN   37027                         \n'])


    def test_empty_file(self):
        # Test when cols and offset are empty

        dummy_spec = {
            "ColumnNames": [],
            "Offsets": [],
            "FixedWidthEncoding": "windows-1252",
            "IncludeHeader": "False",
            "DelimitedEncoding": "utf-8"
        }
        mt_data = get_metadata_from_spec(dummy_spec)
        generate_fixed_length_file(self.test_empty,mt_data)
        # read the file
        with open(self.test_empty,'r',encoding=dummy_spec['DelimitedEncoding']) as file:
            line = file.readlines()
        self.assertEqual(line,[])


if __name__ == "__main__":
    unittest.main()

