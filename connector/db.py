import os
import json
from pathlib import Path
import mysql.connector

secret_path = Path(__file__).parent / 'auth' / 'secret.json'

with open(secret_path, 'r') as secret_file:
    db_config = json.load(secret_file)

# db_config['host'] = os.environ.get('DB-HOST')
db_config['unix_socket'] = os.environ.get('DB-CONNECTOR')
db_config['database'] = os.environ.get('DB-NAME')

db_dermis = mysql.connector.connect(**db_config)