
from connector.db import db_dermis

def get_disease_info(condition):
    cursor = db_dermis.cursor()

    query = "SELECT description, causes, treatments, severity FROM skin_condition WHERE LOWER(name) = LOWER(%s)"

    cursor.execute(query, (condition,))

    result = cursor.fetchone()
    cursor.fetchall()

    cursor.close()

    response = {}

    if result:
        description, causes, treatments, severity = result

        response['description'] = description
        response['causes'] = causes
        response['treatments'] = treatments
        response['severity'] = severity

        return response
    else:
        return None, 404
