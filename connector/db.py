import mysql.connector
import json
from pathlib import Path

secret_path = Path(__file__).parent / 'auth' / 'secret.json'

with open(secret_path, 'r') as secret_file:
    db_config = json.load(secret_file)

db_dermis = mysql.connector.connect(**db_config)