import os
import csv
import json
import codecs
from sys import exit


def get_metadata_from_spec(spec_file_pt):

    '''
        Uses spec file to extract all Metadata and validate the information    
    
        Args:
            Spec file (json) : Spec file perform

        Returns:
            Tuple : Metadata records from spec
            or None with error
        
    '''    

    try:
        if type(spec_file_pt) is dict:
            spec_file = spec_file_pt
        else:
            with open(spec_file_pt,'r',encoding='utf-8') as spec_file:
                spec_file = json.loads(spec_file.read())
        
        # get all attributes
        col_names   = spec_file['ColumnNames']
        offsets     = spec_file['Offsets']
        fwencoding  = spec_file['FixedWidthEncoding']
        header_flag = spec_file['IncludeHeader']
        encoding    = spec_file['DelimitedEncoding']

        # Basic validation        
        if not validation({'cols':col_names,'offset': offsets,
                    'header':header_flag,'encoding': encoding}):
            return None
        print(f'Spec file Validated Successfully')

        metadata = (col_names,offsets,fwencoding,header_flag,encoding)
        return metadata
    
    except json.JSONDecodeError:
        print(f"Error\t: Invalid Json file")
        return None
    except FileExistsError:
        print(f'Error\t: File does not exists at location {spec_file_pt}')
        return None
    except Exception as e:
        print(f'Error\t: Unknown Error {e}')
        return None
    


def generate_fixed_length_file(out_path_fixed_len_file,mt_data,records = None):
    
    '''
        Generate Fixed length file using the spec file
    
        Args:
            out_path_fixed_len_file(str) : Path to store Fixed length path file
            mt_data(tuple) : metadata of spec.json file
        
        Optional:
            records(list) 

        Returns:
            None
        
    '''    

    print("\nGenerating Fixed Length File using Spec file")
    # read Metadata
    column_names, offsets, fixed_width_encoding, include_header, delimited_encoding = mt_data

    try:
        with open(out_path_fixed_len_file,'w',encoding=delimited_encoding) as file:
                if include_header.title() == 'True':
                    print("\nAdding Header to the Fixed Width file")
                    header_line = [str(col).ljust(int(off))[:int(off)] for col,off in zip(column_names,offsets)]
                    header_str  = ''.join(header_line)
                    file.write(header_str+'\n')

            # Optional when records are passed 
                if records: 
                    print("Adding Records to Fixed Width File")
                    for record in records:
                        line =''
                        for idx,tuple_val in enumerate(record.items()):
                            key,value = tuple_val
                            line +=str(value).ljust(int(offsets[idx]))[:int(offsets[idx])] 
                        file.write(line+'\n')
    except Exception as e:
        print(f"Error\t: Program Stop with Unknown Expection {e}")
        exit()
    

def parse_file_to_csv(fixed_wid_file_path, out_file_path, metadata):
    
    '''
        Parse Fixed width file to generate csv file
    
        Args:
            fixed_wid_file_path(str)  : Path to Fixed width file 
            out_file_path(str)        : Path to output file path
            metadata(tuple)           : Spec.json Metadata
            
        Returns:
            None
        
    '''    
    print("\nParsing Fixed length file to csv file")
    
    # read Metadata
    column_names, offsets, fixed_width_encoding, include_header, delimited_encoding = metadata

    # read fixed len file
    with open(fixed_wid_file_path,'r',encoding=delimited_encoding) as FW, open(out_file_path,'w',newline='',encoding=delimited_encoding) as CSVFile:
        # if include_header.title() == 'True': # assuming we write data in Fixed width file
        csvwriter = csv.writer(CSVFile)
        for line in FW.readlines():
            start_idx   = 0
            csv_row     = []
            for offset in offsets:
                field = line[start_idx:start_idx+int(offset)].strip()
                print(field)
                csv_row.append(field)
                start_idx += int(offset)
            print("This is CSV row",csv_row)
            csvwriter.writerow(csv_row)
        

def validation(spec_data):

    '''
        Performs Data Validation check on Spec.json file 
    
        Args:
            spec_data(json)

        Returns:
            1  validation success
            0  with error when validation Failed
    '''    
    
    # Cols & Offset
    if 'cols' in spec_data and 'offset' in spec_data:
        if len(spec_data['cols']) != len(spec_data['offset']):
            print(f'Error\t: Validaton Failed No approriate offset for columnn')
            return 0
    else:
        print(f'Error\t: Validaton Failed spec file missing col names or offset')
        return 0

    # Header
    if 'header' in spec_data:
        if spec_data['header'] not in ['True','False','true','false']:
            print(f'Error\t: Validation Failed Header formmatted wrongly')
            return 0
    else:
        print(f'Error\t: Validaton Failed spec file missing Header information')
        return 0
    
    # Encoding
    if "encoding" in spec_data:
        try:
            codecs.lookup(spec_data['encoding'])
        except LookupError:
            print(f'Error\t: Validation Failed Invalid Encoding style')
            return 0
    return 1


def main(sp_path,fwf_path,csv_path,rec_path=None):
    
    '''
        Main Operation Performs following operations
            * Extract Metadata from Spec.json file
            * Generate Fixed width file using the Metadata
            * Generate CSV file using Fixed width file 
    
        Args:
            sp_path     : Path to spec.json file
            rec_path    : Path to records.json
            fwf_path    : Path to Fixed width file 
            csv_path    : Path to output csv file

        Returns:
            None
    '''    

    metadata = get_metadata_from_spec(sp_path)
    if metadata:
        # add logic read data when only data is added
        if rec_path:
            with open(rec_path,'r',encoding='utf-8') as json_file:
                rec = json.loads(json_file.read())
            generate_fixed_length_file(fwf_path,metadata,records=rec)
        else:
            generate_fixed_length_file(fwf_path,metadata)

        # use generate file to convert it into csv
        parse_file_to_csv(fwf_path,csv_path,metadata)
        
if __name__ == "__main__":
    main()