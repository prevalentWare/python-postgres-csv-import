# PostgreSQL Data Importer

This script allows you to import data from a CSV file directly into a PostgreSQL table.

## Requirements

- Python
- `psycopg2` and `python-dotenv` packages
- A `.env` file with PostgreSQL connection parameters

## Setup

1. Clone the repository.
2. Create a `.env` file in the root directory with the following format:

```
DB_HOST=<your_database_host>
DB_PORT=<your_database_port>
DB_NAME=<your_database_name>
DB_USER=<your_database_user>
DB_PASSWORD=<your_database_password>
```

Replace the placeholders with your actual PostgreSQL connection details.

3. Install the required Python packages:

```
pip install -r requirements.txt
```

## Usage

To run the script:

```
python import_to_pg.py <path_to_file.csv> <table_name> <delimiter>
```

**Parameters:**

- `path_to_file.csv`: Path to the CSV file you want to import.
- `table_name`: The name of the PostgreSQL table you want to import the data into.
- `delimiter`: The delimiter used in your CSV file (e.g., `","` for comma-separated values or `";"` for semicolon separated values).

## Note

Ensure that the CSV's header matches the columns in the specified PostgreSQL table.
