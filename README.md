# Project Name : exploratory-data-analysis---customer-loans-in-finance833


## A description of the project: 

what it does:The project retrieves data for customers that took out loans from a loan provider. 
the aim of the project: The aim of the project is to understand whether we can get insight into 
what factors will help us understand the likelihood of loss or default.
and what you learned

## Installation instructions : 

The packages required are : 
```psycopg2 , sqlalchemy , numpy , pandas and logging ``` 


## Usage instructions 

When you first clone the repository you will not have access to the credential.yaml file as it has been added 
to gitignore. 
Here is the parameters you need to import the data:

```
RDS_HOST: eda-projects.cq2e8zno855e.eu-west-1.rds.amazonaws.com
RDS_PASSWORD: EDAloananalyst
RDS_USER: loansanalyst
RDS_DATABASE: payments
RDS_PORT: 5432
```

Make sure you have updated pip or pip3 and if you have python2 installed on your machine 
ensure you use python3 instead of just python when running your file.
To run the file first navigate to the folder where your file resides in then use
``` python3 dbutils.py```

## File structure of the project

.
├── credentials.yaml
├── db_utils.py
├── helper_functions
│   ├── load_credentials.py
│   └── __pycache__
│       └── load_credentials.cpython-310.pyc
├── loan_payments_data.csv
└── README.md

## License information

The Open Software License 3.0

