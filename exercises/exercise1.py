import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import BIGINT, TEXT, FLOAT

source_link = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"

airports_data = pd.read_csv(source_link, sep=";")
print(airports_data.head())

sqlite_datatypes = {'column_1': BIGINT, 'column_2': TEXT, 'column_3': TEXT, 'column_4': TEXT, 'column_5': TEXT,
                    'column_6': TEXT, 'column_7': FLOAT, 'column_8': FLOAT, 'column_9': BIGINT, 'column_10': FLOAT,
                    'column_11': TEXT, 'column_12': TEXT, 'geo_punkt': TEXT}

# Changing the datatypes using pandas did not work!
# airports_data = airports_data.astype(sqlite_datatypes)

# echo is not standard for Python and was not specified in the exercise. Therefore, it is set to False.
sqlite_database = create_engine('sqlite:///airports.sqlite', echo=False)

# If the index is left by default True: somehow the test shape will be 2/4.
# Once the index is dropped the shape matches the test 4/4.
airports_data.to_sql(name='airports', con=sqlite_database, index=False, if_exists='replace', dtype=sqlite_datatypes)

# References:
# https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
# https://docs.sqlalchemy.org/en/20/core/engines.html#dbengine-logging
# https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.BIGINT
# https://stackoverflow.com/questions/41363343/pythonsqlalchemy-change-dtype-object-to-string-dynamically
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html#r689dfd12abe5-1
