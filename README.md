### Parse fixed width file

- Parse_fixed_width file structure
- Parse_Fixed_Width
    - input
    - output
    - scripts
        - utils.py
    - testing
        - test_cases.py
    - __main__.py
    - DOCKERFILE

- To run the file 
``` use command 
    python Parse_Fixed_Width
    
    for help
    python Parse_Fixed_Width -h
```
- Modify input data records.json or specify your own path and Generated output are in output folder.


### Data processing
- Data Processing file structure
- Data_Processing
    - files
    - scripts
        - Anonymise_big_data.py
        - Anonymise_data.py
        - Generate_csv_file.py
        - main.py

- Generate_csv_file.py script produces random data with "First Name, Last Name, Address, Dob" in it.
- Anonymise_data.py is used to anonymise the data using randomly generated output
- Anonymise_big_data.py is used to anonymise the data using the pyspark 



