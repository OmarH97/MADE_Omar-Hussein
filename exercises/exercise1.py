import pandas as pd
from sqlalchemy import create_engine


source_link = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"

airports_data = pd.read_csv(source_link, sep=";")
print(airports_data.head())

sqlite_database = create_engine('sqlite:///airports.sqlite', echo=False)

airports_data.to_sql(name='airports', con=sqlite_database)





