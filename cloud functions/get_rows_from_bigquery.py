from google.cloud import bigquery
from google.cloud.exceptions import NotFound
import mysql.connector as connection
import json


def get_rows_from_bigquery(request):
    table_name = request.args["table_name"]
    project_id = "chatmine-388722"
    schema = "co_dtkl"
    table_id = "{0}.{1}.{2}".format(project_id, schema, table_name)
    headers = {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'application/json'
    }
    if table_name.strip() == "":
        return json.dumps({"result": "error", "description": "no table name"})

    client = bigquery.Client()

    try:
        client.get_table(table_id)
    except NotFound:
        return json.dumps({"result": "error", "description": "table not found"})

    query = "SELECT COUNT(*) filas FROM `{0}`.`{1}`".format(schema, table_name)
    query_job = client.query(query)
    query_job.result()

    rows = list(query_job)
    return (json.dumps({"result": "ok", "rows": rows[0].filas}), 200, headers)