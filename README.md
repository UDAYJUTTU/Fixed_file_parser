### Parse Fixed Width File

- **Directory Structure**:
  - `Parse_Fixed_Width`
    - `input`
    - `output`
    - `scripts`
        - `utils.py`
    - `testing`
        - `test_cases.py`
    - `__main__.py`
    - `DOCKERFILE`

- **How to Run**:
    - To run the script, use the following command:
    ```sh
    python Parse_Fixed_Width
    ```
    - For help, use:
    ```sh
    python Parse_Fixed_Width -h
    ```

- Modify the input data in `records.json` or specify your own path. The generated output will be saved in the `output` folder.

### Data Processing

- **Directory Structure**:
  - `Data_Processing`
    - `files`
    - `scripts`
        - `Anonymise_big_data.py`
        - `Anonymise_data.py`
        - `Generate_csv_file.py`
        - `main.py`

- **Scripts Overview**:
  - `Generate_csv_file.py`: This script produces random data with the fields "First Name, Last Name, Address, Dob".
  - `Anonymise_data.py`: This script anonymizes the data using randomly generated output.
  - `Anonymise_big_data.py`: This script anonymizes large datasets using PySpark.
