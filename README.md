# Python Cloud Functions with Google Cloud Platform (GCP)

This is a Python script for creating and deploying Google Cloud Functions that interacts with a MySQL database and Google's BigQuery. This script provides three main functionalities:

1. Listing tables from a MySQL database.
2. Copying a table from MySQL to BigQuery.
3. Getting the number of rows in a BigQuery table.

## Requirements
To execute this script, you need to install the following Python libraries:

```
pip install -r requirements.txt
```

## Environment Variables
Please set the following environment variables:

* **DB_USER**: MySQL database user
* **DB_PASSWORD**: MySQL database password
* **DB_HOST**: MySQL database host
* **DB_DATABASE**: MySQL database name
* **PROJECT_ID**: Google Cloud Project ID
* **SCHEMA**: BigQuery Dataset ID

## Usage

To use this script, you need to have access to both a MySQL database and a BigQuery database.

Here are the descriptions of each function in the script and how to use them.

1. **list_mysql_tables(request)**: This function returns a JSON with the schema, name and number of rows of each table in the MySQL database.

* **request**: An object that has an attribute `args`. No specific argument is expected in this function.

2. **copy_table_mysql_to_bigquery(request)**: This function copies a MySQL table to BigQuery.

- **request**: An object that has an attribute `args` with the following parameters:

    - **table_source**: The name of the MySQL table you want to copy.
    - **table_destination**: The name of the BigQuery table to be created.

3. **get_rows_from_bigquery(request)**: This function returns the number of rows in a specific BigQuery table.

- **request**: An object that has an attribute `args` with the following parameter:

    - **table_name**: The name of the BigQuery table from which you want to get the number of rows.

## Important Notes

- Make sure to provide the correct parameters in the `RequestArgsMock` object, following the mentioned format.

- To use this script, the MySQL database and BigQuery need to be accessible to the instance running this script. This includes network accessibility, correct IP addresses, and proper authentication.

- The warning raised from pandas (`pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection.`) could be ignored in this scenario as we are using a well-supported MySQL connection via `mysql-connector-python`.

- This script assumes that the GCP project ID and schema are already set. If you want to use this script with a different project or schema, you should change these values in the `project_id` and `schema` variables.

## Deployment on Google Cloud Functions

To deploy this script on Google Cloud Functions, you will have to separate each function (with their imports) into different .py files and create a main function in each file. The main function will act as an entry point for the cloud function and will call the appropriate function with the `request` argument.

Make sure to replace all local variables like `project_id`, `schema`, `user`, `password`, `host`, `database` with environment variables or secure secret manager solutions provided by GCP. Remember to test the functions thoroughly before deployment.