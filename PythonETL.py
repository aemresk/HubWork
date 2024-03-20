import pandas as pd
import sqlalchemy

source_engine = sqlalchemy.create_engine('source-database-connection-string')
target_engine = sqlalchemy.create_engine('target-database-connection-string')
df = pd.read_sql("SELECT * FROM source_engine", source_engine)

df['new_column'] = 'value'

df.to_sql('target_table', target_engine, if_exists='append', index=False)
