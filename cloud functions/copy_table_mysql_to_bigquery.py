import json
import pandas as pd
import mysql
from google.cloud import bigquery
from google.cloud.exceptions import NotFound

def get_engine():
    db_config = mysql.connector.connect(
        user="",
        password="",
        host="",
        database=""
    )
    
    return db_config


def copy_table_mysql_to_bigquery(request):
    table_source = request.args['table_source']
    table_destination = request.args['table_destination']
    project_id = ""
    schema = ""
    table_id =  '{0}.{1}.{2}'.format(project_id, schema, table_destination)

    if table_source.strip() == "" or table_destination.strip() == "":
        return json.dumps({'result': 'error', 'description': 'no table name'})

    engine = get_engine()
    query = 'SELECT * FROM {0}'.format(table_source)
    result_dataframe = pd.read_sql(query, engine)

    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
    )

    job = client.load_table_from_dataframe(
        result_dataframe, table_id, job_config=job_config
    )
    job.result()

    try:
        client.get_table(table_id)
    except NotFound:
        return json.dumps({'result': 'error', 'description': 'table not found'})

    return json.dumps({'result': 'ok'})