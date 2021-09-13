from typing import Dict
import requests
from requests.structures import CaseInsensitiveDict
import json


def load_database() -> Dict[str, Dict[str, str]]:
    """
    Performs API request using AirTable api url and Clay's personal authorization key.

    Creates a hash map (or a Dictionary, in Python) mapping uppercase letters to data associated with the letter
        {uppercase letters} -> { lowercase, English, Spanish, Igbo, Youruba, Kalabari}
    """

    # 1) Generating fields for AirTable API Request
    api_url = "https://api.airtable.com/v0/app5VUgXNB2NPXOvT/Table%201"
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer keyzrqqscFMGSlo8M"
    # 2) Perform API request
    response = requests.get(api_url, headers=headers).text
    records = json.loads(response)['records']
    # Parse API response
    outer_map = {}
    for row in records:
        column = row['fields']
        outer_map[column['Uppercase']] = {
            "Lowercase": bool(column['Lowercase']),
            "English": bool(column['English']),
            "Spanish": bool(column['Spanish']),
            "Igbo": bool(column['Igbo']),
            "Yoruba": bool(column['Yoruba']),
            "Kalabari": bool(column['Kalabari'])
        }
    return outer_map


letters = load_database()
print(letters)
