from typing import Union
from urllib.parse import urljoin

from requests import get, RequestException


class DataFetcher:
    """
    Fetches data from the given url with optional parameters.
    """
    def __init__(self, url: str,
                 endpoint: str,
                 query_params: Union[dict, None] = None,
                 headers: Union[dict, None] = None,
                 cookies: Union[dict, None] = None):

        self.url = url
        self.endpoint = endpoint
        self.query_params = query_params
        self.headers = headers
        self.cookies = cookies

    def get_response_json(self) -> Union[dict, None]:
        """
        Sends a GET request to the specified URL with class parameters.

        Returns:
            dict or None: JSON response data if successful, None if request fails.
        """
        try:
            response = get(urljoin(self.url, self.endpoint),
                           params=self.query_params,
                           headers=self.headers,
                           cookies=self.cookies)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            print(f'Error fetching data: {e}')
            return None
