from db_utils import RDSDatabaseConnector

import datetime
import pandas as pd

data_finance=pd.read_csv('loan_payments_data.csv')
class DateTransform:
    def __init__(self,df):
        self.df=df
    # date_columns=[ element for element in list(data_finance.columns)  if 'date' in element]

    def convert_to_date(self,columns):
        
        self.df[columns]=self.df[columns] \
        .apply(lambda x: pd.to_datetime(x,format='%b-%Y',errors='coerce'))
        return self.df

# create a notebook - done in main.ipynb 