import psycopg2
from helper_functions.load_credentials import load_config
from sqlalchemy import create_engine
import pandas as pd
import logging

class RDSDatabaseConnector:
    """
    A class for connecting to an RDS database, extracting data, and saving it to a local file.

    Attributes:
        config_file_path (str): The path to the configuration file.
    
    Methods:
        __init__(): Initializes the RDSDatabaseConnector object, loading credentials from the specified configuration file.
        load_config(): Loads configuration settings from the specified file path.
        initialize_engine(): Initializes and returns a database engine using the configured RDS credentials.
        extract_data(table_name='loan_payments'): Extracts data from the specified table in the RDS database and returns it as a Pandas DataFrame.
        save_data(df, file_path, file_format='csv'): Saves the provided DataFrame to a file in the specified format at the given file path.

    Example:
    ```python
    connector = RDSDatabaseConnector()
    df = connector.extract_data(table_name='loan_payments')
    connector.save_data(df, file_path='/path/to/save/loan_payments_data.csv')
    ```
    """

    def __init__(self):
        """
    Initializes the RDSDatabaseConnector object.

    Loads RDS credentials from the specified configuration file and updates the object's attributes.

    Attributes:
        config_file_path (str): The path to the configuration file.
    """
        self.config_file_path = "./credentials.yaml"
        credentials = self.load_config()
        self.__dict__.update(credentials)

    def load_config(self):
        """
    Loads configuration settings from the specified file path.

    Returns:
        dict: A dictionary containing RDS credentials.
    
    Raises:
        Exception: If an error occurs while loading the configuration.
    """
        try:
            return load_config(self.config_file_path)
        except Exception as e :
            logging.error(f"Error loading configuration from {self.config_file_path}:{e}")
            raise
    def initialize_engine(self):
        """
    Initializes and returns a database engine using the configured RDS credentials.

    Returns:
        sqlalchemy.engine.base.Engine: The initialized database engine.
    """
        
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{self.RDS_USER}:{self.RDS_PASSWORD}@{self.RDS_HOST}:{self.RDS_PORT}/{self.RDS_DATABASE}")
        return engine
    
    def extract_data(self,table_name = "loan_payments"):
         
        """
        Extracts data from the specified table in the RDS database.

        Args:
            table_name (str, optional): The name of the table to extract data from. Default is 'loan_payments'.

        Returns:
            pandas.DataFrame: A Pandas DataFrame containing the extracted data.

        """
        # Initialize the engine
        engine = self.initialize_engine()
        # Extract data into a Pandas DataFrame
        df = pd.read_sql_table(table_name, engine)
        return df

    
    
    def save_data(self,df, file_path,file_format='csv'):
        
        """
    Saves the provided DataFrame to a file in the specified format at the given file path.

    Args:
        df (pandas.DataFrame): The DataFrame to be saved.
        file_path (str): The path where the file should be saved.
        file_format (str, optional): The format in which the file should be saved. Default is 'csv'.

    Raises:
        Exception: If an error occurs while saving the data to the file.
    """
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