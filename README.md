# Python Cloud Functions with Google Cloud Platform (GCP)

This is a Python script for creating and deploying Google Cloud Functions that interacts with a MySQL database and Google's BigQuery. This script provides three main functionalities:

1. Listing tables from a MySQL database.
2. Copying a table from MySQL to BigQuery.
3. Getting the number of rows in a BigQuery table.

See a [Final Application](https://gcp-python-ywtk7siozq-wn.a.run.app/)

## Requirements
To execute this script, you need to install the following Python libraries:

1. To get the application running, you'll first need to clone this repository: https://github.com/oardilac/SQL-and-NoSQL-Data-Manipulation-Project
2. Navigate to the SQL folder, and run the `mysqlsampledatabase.sql` file in a local instance or in Google Cloud Platform (GCP).
3. Install the required Python libraries using the following command:

```
pip install -r requirements.txt
```


## Configuration

There are two important configuration files, `.env.template` in the root directory and another in the `cloud functions` directory. 

1. Rename the `.env.template` file to `.env` and fill it with your specific information. The variables in this file are used by the `notebook.ipynb` file.
2. The environment variables in the `cloud functions` folder are used by the cloud functions. These should also be filled with your specific data.

The variables in both files are:

- **DB_USER**: MySQL database user
- **DB_PASSWORD**: MySQL database password
- **DB_HOST**: MySQL database host
- **DB_DATABASE**: MySQL database name
- **PROJECT_ID**: Google Cloud Project ID
- **SCHEMA**: BigQuery Dataset ID

## Running the Application

If you want to test the application with your code, you should update the API URLs in the `app` directory to match your local or cloud functions URLs.

This project uses Django and Google Cloud Run for web app deployment. The `app` folder contains the Django application that gets deployed on Google Cloud Run using a Dockerfile. 


## Note

Remember to fill in the `.env` file and `cloud functions` variables with your specific data. Without these variables, the application will not function properly.