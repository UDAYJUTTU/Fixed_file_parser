### Parse Fixed Width File

The following script converts the input `records.json` (if provided) to a fixed-width text file. In the next operation, the script generates a text-delimited file, such as a CSV, using the fixed-width text file.

**Note:** All output files are generated in the `output` folder, and input files are typically located in the `input` folder.

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

### Data Processing

The `Data_Processing` folder contains multiple scripts that perform the following operations:
1. Generate a random data CSV file.
2. Anonymize data for small datasets.
3. Anonymize data for large datasets.

- **Directory Structure**:
  - `Data_Processing`
    - `files`
    - `scripts`
      - `Anonymise_big_data.py`
      - `Anonymise_data.py`
      - `Generate_csv_file.py`
      - `main.py`

- **Scripts Overview**:
  - `Generate_csv_file.py`: This script generates random data with fields such as "First Name, Last Name, Address, Date of Birth".
  - `Anonymise_data.py`: This script anonymizes data using the randomly generated output.
  - `Anonymise_big_data.py`: This script anonymizes large datasets using PySpark.

- **How to Run**:
  - Run individual scripts to perform the necessary operations. For example, to generate a random CSV file:
    ```sh
    python Generate_csv_file.py
    ```
  - Alternatively, you can run all operations together (Generate Random Data + Anonymize Data + Anonymize Big Data) by executing:
    ```sh
    python main.py
    ```
