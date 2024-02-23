
import pandas as pd
from scipy.stats import skew , kurtosis 
from collections import defaultdict

class DataDistribution:
    
    def __init__(self,df):
        self.df=df

    def determine_distribution(self):
        ''' expected output of this method 
        'normal': ['loan_amount', 'funded_amount', 'funded_amount_inv',
                    'int_rate', 'instalment', 'issue_date', 
                    'dti', 'mths_since_last_delinq', 'mths_since_last_record',
                    'open_accounts', 'total_accounts', 
                    'total_payment', 'total_payment_inv', 'total_rec_prncp',
                    'last_payment_date', 'next_payment_date', 'last_credit_pull_date', 
                    'mths_since_last_major_derog'], 
        'skewed': ['annual_inc', 'delinq_2yrs', 'inq_last_6mths', 
                    'out_prncp', 'out_prncp_inv', 'total_rec_int', 
                    'total_rec_late_fee', 'recoveries', 
                    'collection_recovery_fee', 'last_payment_amount', 
                    'collections_12_mths_ex_med'], 
        'constant': ['policy_code']}
        '''

        normality_dict={}
        numeric_columns = self.df.select_dtypes(include='number').columns.to_list()

        for a_column in numeric_columns[2:]:
        # numeric_columns ignores the first 2 columns namely id and member_id columns 

            column_values = self.df[a_column].values  # Extract the column data
            skewness = skew(column_values,nan_policy='omit')
            kurt = kurtosis(column_values,nan_policy='omit')

            # Set threshold values for skewness and kurtosis
            skew_threshold = 0.5
            kurt_threshold = 2.0

            # Determine distribution category
            if column_values.std() < 1e-6:
                normality_dict[a_column] = 'constant'
                continue
            if abs(skewness) >= skew_threshold or abs(kurt) >= kurt_threshold:
                normality_dict[a_column]='skewed_distribution'
            else:
                normality_dict[a_column]='normal_distribution'
            # Counter(normality_dict.values())
        new_dict=defaultdict(list)
        for key,value in normality_dict.items():
            new_dict[value].append(key)
        new_dict=dict(new_dict)
        return new_dict

data_finance=pd.read_csv('loan_payments_data.csv')
dd=DataDistribution(data_finance)
print(dd.determine_distribution())

#  there seems to be an issue with precision error. 
# Preprocessing the data should come before imputation 