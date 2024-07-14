from json import dump, load
from os.path import exists
from typing import Union

from requests.cookies import RequestsCookieJar


def save_data_for_json(data: dict, file_path: str) -> None:
    """
    Save JSON data to a file.

    Args:
        data (dict): The JSON-serializable data to be saved.
        file_path (str): The file path where the data should be saved.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        dump(data, f, ensure_ascii=False, indent=4)


def load_data_from_json(file_path: str) -> Union[dict, None]:
    """
    Load JSON data from a file.

    Args:
        file_path (str): The file path from which to load JSON data.

    Returns:
        dict: The loaded JSON data as a dictionary.
    """
    if exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return load(f)
    else:
        print(f'File not found: {file_path}')


def create_cookie_jar(cookies_dict: dict) -> RequestsCookieJar:
    """
    Create a RequestsCookieJar from a dictionary of cookies.

    Args:
        cookies_dict (dict): A dictionary where keys are cookie names and values are cookie values.

    Returns:
        RequestsCookieJar: A RequestsCookieJar object populated with the provided cookies.
    """
    cookie_jar = RequestsCookieJar()
    for name, value in cookies_dict.items():
        cookie_jar.set(name, value)
    return cookie_jar
