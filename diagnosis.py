import mysql.connector
import json

def get_disease_info(condition):
    with open('secret.json', 'r') as secret_file:
        db_config = json.load(secret_file)
    
    db_dermis = mysql.connector.connect(**db_config)

    cursor = db_dermis.cursor()

    query = "SELECT causes, treatment, severity FROM diseases WHERE condition = %s"

    cursor.execute(query, (condition,))

    result = cursor.fetchone()

    cursor.close()

    response = {}

    if result:
        causes, treatment, severity = result

        response['causes'] = causes
        response['treatment'] = treatment
        response['severity'] = severity

        return response
    else:
        return None, 404.
