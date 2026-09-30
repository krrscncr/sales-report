import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:@127.0.0.1:3306/sales_db")

df = pd.read_csv("data/sales.csv")
df.to_sql("sales", engine, if_exists="append", index=False)

print(f"Загружено {len(df)} строк в таблицу sales")