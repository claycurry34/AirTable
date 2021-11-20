from typing import Dict, List
import requests
from requests.structures import CaseInsensitiveDict
import json

map_is_initialized: bool = False
character_map: Dict[str, Dict[str, any]] = None


def load_database() -> None:
    """
    Performs API request using Letters api url and Clay's personal authorization key.

    Returns a hash map (or a Dictionary, in Python) mapping uppercase letters to data associated with the letter
        {uppercase letters} -> { lowercase, English, Spanish, Igbo, Youruba, Kalabari}
    """

    # 1) Generating fields for Letters API Request
    api_url = "https://api.airtable.com/v0/app5VUgXNB2NPXOvT/Table%201"
    headers = CaseInsensitiveDict()
    headers["Authorization"] = "Bearer keyzrqqscFMGSlo8M"
    # 2) Perform API request
    response = requests.get(api_url, headers=headers).text
    records = json.loads(response)['records']
    # 3) Parse API response
    outer_map = {}
    for row in records:
        column = row['fields']
        outer_map[column['Uppercase']] = {
            "Lowercase": column['Lowercase'],
            "English": column['English'] == "True",
            "Spanish": column['Spanish'] == "True",
            "Igbo": column['Igbo'] == "True",
            "Yoruba": column['Yoruba'] == "True",
            "Kalabari": column['Kalabari'] == "True"
        }

    # 4) Cache response
    global map_is_initialized
    global character_map
    map_is_initialized = True
    character_map = outer_map


def get_sorted_characters(requested_language: str) -> List[str]:
    """
    Accepts some language as an argument and

    Returns a sorted array of characters from the requested language
    """
    global map_is_initialized
    global character_map
    if not map_is_initialized:
        load_database()
    requested_characters = []
    for character in character_map.keys():
        character_info = character_map.get(character)
        if character_info.get(requested_language):
            requested_characters.append(character)
    return sorted(requested_characters)


