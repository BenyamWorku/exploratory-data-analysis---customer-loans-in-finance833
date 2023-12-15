import psycopg2
from helper_functions.load_credentials import load_config
from sqlalchemy import create_engine
import pandas as pd
import logging

class RDSDatabaseConnector:

    def __init__(self):
        self.config_file_path = "./credentials.yaml"
        credentials = self.load_config()
        self.__dict__.update(credentials)

    def load_config(self):
        try:
            return load_config(self.config_file_path)
        except Exception as e :
            logging.error(f"Error loading configuration from {self.config_file_path}:{e}")
            raise
    def initialize_engine(self):
        
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{self.RDS_USER}:{self.RDS_PASSWORD}@{self.RDS_HOST}:{self.RDS_PORT}/{self.RDS_DATABASE}")
        return engine
    
    def extract_data(self,table_name = "loan_payments"):
       
        # Initialize the engine
        engine = self.initialize_engine()
        # Extract data into a Pandas DataFrame
        df = pd.read_sql_table(table_name, engine)
        return df

    # Step 7: Now create another function which saves the data to an appropriate file format to your local machine. 
    # This should speed up loading up the data when you're performing your EDA/analysis tasks. The function should save the data in .csv format, since we're dealing with tabular data.
    def save_data(self,df, file_path,file_format='csv'):
        try:
            if file_format=='csv':
                df.to_csv(file_path,index=False)
                logging.info(f"Data saved to {file_path}in {file_format} format.")
        except Exception as e:
            logging.error(f"Error saving data to file:{e}")
            raise
if __name__ == "__main__":
    connector=RDSDatabaseConnector()
    df=connector.extract_data(table_name='loan_payments')
    connector.save_data(df,file_path='/home/benmlengineer/Documents/Aicore/exploratory-data-analysis---customer-loans-in-finance833/loan_payments_data.csv')