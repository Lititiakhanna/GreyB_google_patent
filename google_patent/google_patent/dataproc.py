import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

data = pd.read_csv('./googlepatent.csv', header=0)

clean_data = data.dropna()

# print(clean_data)

# row_sums = clean_data.sum(axis=1)
# print(str(row_sums))

frequency_counts = clean_data['number_of_authors'].value_counts()
frequency_df = frequency_counts.reset_index()
frequency_df.columns = ['category', 'count'] 
# print(frequency_counts)

description = clean_data['number_of_viewers'].describe()
description_df = description.reset_index()
# print(description)


DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
DATABASE = os.getenv('DB_NAME')

# print(PORT,DATABASE, USER)
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

clean_data.to_sql('google_patent_data', engine, if_exists='replace', index=False)
frequency_df.to_sql('categorical_frequency_count', engine, if_exists='replace', index=False)
description_df.to_sql('numerical_statistics', engine, if_exists='replace', index=False)


# print(description_df)
# print(frequency_df)
print("Data inserted successfully!")
