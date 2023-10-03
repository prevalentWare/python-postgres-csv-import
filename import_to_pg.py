import sys
import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection parameters
DB_PARAMS = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

def copy_to_table(file_path, table_name, delimiter):
    """Copy data from a CSV file to a PostgreSQL table."""
    # Create a connection
    with psycopg2.connect(**DB_PARAMS) as conn:
        with conn.cursor() as cur:
            with open(file_path, 'r') as f:
                cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER DELIMITER '{delimiter}'", f)
            print(f"Data imported to {table_name} successfully.")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python import_to_pg.py <path_to_file.csv> <table_name> <delimiter>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    table_name = sys.argv[2]
    delimiter = sys.argv[3]
    
    copy_to_table(file_path, table_name, delimiter)
