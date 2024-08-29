from pyspark.sql import SparkSession
from pyspark.sql.types import StringType
from pyspark.sql.functions import sha2, concat_ws, lit
import os


csv_path    = os.path.abspath("Data_Processing/files/Random_data.csv")
output_path = os.path.abspath("Data_Processing/files/anonymised_big_data_file.csv")

def process_big_data(random_file = csv_path,output_path =output_path):
    '''
        takes csv file as an input and uses distributed computing pyspark to Anonymise data and stores as csv
    
        Args:
            random_file         : Path to csv file
            output_path         : Path to store Anonymized data

        Returns:
            None 
    '''
    print("processing file using Pyspark")
    # Initialize Spark session
    spark = SparkSession.builder.getOrCreate()

    # Read the CSV file
    df = spark.read.csv(random_file, header=True)

    # change datatypes
    df = df.withColumn("first_name",df['first_name'].cast(StringType())).withColumn("last_name",df['last_name'].cast(StringType()))

    # Anonymize
    df_anonymized = df.withColumn("first_name", sha2(df["first_name"], 256)) \
                    .withColumn("last_name", sha2(df["last_name"], 256)) \
                    .withColumn("address", sha2(df["address"], 256))

    # Write the anonymized data 
    df_anonymized.write.csv(output_path, header=True,mode='overwrite')

    # Stop session
    spark.stop()

if __name__ == "__main__":
    process_big_data(csv_path,output_path)