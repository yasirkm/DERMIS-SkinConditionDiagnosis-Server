
from connector.db import db_dermis

def get_disease_info(condition):
    cursor = db_dermis.cursor()

    query = "SELECT description, causes, treatment, severity FROM skin_condition WHERE LOWER(name) = LOWER(%s)"

    cursor.execute(query, (condition,))

    result = cursor.fetchone()

    cursor.close()

    response = {}

    print('got', result)

    if result:
        description, causes, treatment, severity = result

        response['description'] = description
        response['causes'] = causes
        response['treatment'] = treatment
        response['severity'] = severity

        return response
    else:
        return None, 404
