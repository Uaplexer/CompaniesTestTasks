from typing import Union
from urllib.parse import urljoin

from requests import Session, RequestException


class MySession(Session):
    """
    Custom session class extending requests.Session to provide additional methods.
    """

    def get_response_text(self, url: str, endpoint: Union[str, None] = None) -> Union[str, None]:
        """
        Sends a GET request to the specified URL and endpoint, returning response text.

        Args:
            url (str): The base URL for the request.
            endpoint (str, optional): The endpoint to append to the URL.

        Returns:
            str or None: The response text if successful, None if request fails.
        """
        try:
            response = self.get(urljoin(url, endpoint),
                                params=self.params,
                                headers=self.headers,
                                cookies=self.cookies)
            response.raise_for_status()
            return response.text
        except RequestException as e:
            print(f'Error fetching data: {e}')
            return None
