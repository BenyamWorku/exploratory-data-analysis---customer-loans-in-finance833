# data_finance=pd.read_csv('loan_payments_data.csv')

class DataFrameInfo:
    def __init__(self,df):
        self.df=df
        ''' Some useful utility methods you might want to create that are often used for EDA tasks are:

Describe all columns in the DataFrame to check their data types
Extract statistical values: median, standard deviation and mean from the columns and the DataFrame
Count distinct values in categorical columns
Print out the shape of the DataFrame
Generate a count/percentage count of NULL values in each column'''

    def describe_columns(self):
        return self.df.info()

    def extract_statistics(self):
        return self.df.describe()
    
    def count_distinct(self):
        return [{columns:list(self.df[columns].unique())} for columns in self.df.select_dtypes(include=['category']).columns]
    def display_shape(self):
        return self.df.shape
    def display_null_percentage(self):
        return self.df.isna().sum()/len(self.df)*100
