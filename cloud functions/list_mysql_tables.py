from google.cloud import bigquery
import pandas as pd
import mysql
import mysql.connector as connection

def get_engine():
    db_config = mysql.connector.connect(
        user="",
        password="",
        host="",
        database=""
    )
    
    return db_config


def list_mysql_tables(request):
    engine = get_engine()
    query = '''
        SELECT
            table_schema
            , table_name
            , table_rows
        FROM information_schema.tables
        WHERE table_schema = "[Database]" AND TABLE_TYPE = "BASE TABLE"
    '''

    result_dataframe = pd.read_sql(query, engine)
    engine.close()
    return (result_dataframe.to_json(orient='records'), 200)