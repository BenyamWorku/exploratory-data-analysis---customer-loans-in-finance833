import pandas as pd
from dataframe_info import DataFrameInfo
from data_distribution import DataDistribution

class DataFrameTransform:
    def __init__(self, df):
        self.df = df

    def impute(self):
        # Display null percentage using DataFrameInfo
        null_percentage = DataFrameInfo(self.df).display_null_percentage()

        # Create a DataFrame to store null percentage information
        result_df = pd.DataFrame({'column_name': null_percentage.index, 'missing_percentage': null_percentage.values})

        # Create a copy of the original DataFrame
        processed_df = self.df.copy()

        # Step 1: Drop columns with more than 50% missing values
        majority_null_columns = result_df[result_df.missing_percentage > 50].column_name.to_list()
        processed_df = processed_df.drop(columns=majority_null_columns)

        # Step 2: Impute category columns with mode 
        category_columns_to_impute = processed_df.select_dtypes(include='object').columns.to_list()
        # numerical_columns_to_impute = processed_df.select_dtypes(include='number').columns.to_list()
        # make sure the firt 2 columns id and member id are ignored before proceeding with preporcessing the columns 
        for col in category_columns_to_impute:
            processed_df[col].fillna(processed_df[col].mode()[0], inplace=True)
         # Step 3: Impute numerical columns with mean or median

        ''' 
        skewed_normal_constant=DataDistributon(processed_df)

        '''
        new_dict=DataDistribution(processed_df).determine_distribution()


        ''' new_dict = {'normal_distribution':[],'skewed_distribution':[],'constant':[]}'''



        normal_distribution_df=processed_df[new_dict['normal_distribution']]
        skewed_distribution_df=processed_df[new_dict['skewed_distribution']]
        # constant_distribution_df=processed_df[new_dict['constant']]
        # *********************
        normal_distribution_df=normal_distribution_df.fillna(normal_distribution_df.mean())
        skewed_distribution_df=skewed_distribution_df.fillna(skewed_distribution_df.median())
        # constant_distribution_df=processed_df.drop(constant_distribution_df)
        # **********************
        all_imputed_dfs=[processed_df[category_columns_to_impute],normal_distribution_df,skewed_distribution_df]
        processed_df=pd.concat(all_imputed_dfs,axis=1,join='inner')
        
        return processed_df

# Example usage
data_finance = pd.read_csv('loan_payments_data.csv')
dd = DataFrameTransform(data_finance)
processed_data = dd.impute()

# Display null percentage of the processed DataFrame
print(DataFrameInfo(processed_data).display_null_percentage())


