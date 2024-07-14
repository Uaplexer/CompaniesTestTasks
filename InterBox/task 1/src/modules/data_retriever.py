from typing import Union, List, Dict


class CountryDataRetriever:
    """
    Retrieves and transforms country data.
    """

    @staticmethod
    def get_name(country: Dict) -> Union[str, None]:
        """
        Extracts the common name of the country.

        Args:
            country (Dict): A dictionary containing country data.

        Returns:
            Union[str, None]: The common name of the country, or None if not found.
        """
        return country.get('name', {}).get('common')

    @staticmethod
    def get_capital_names(country: Dict) -> Union[str, None]:
        """
        Extracts the capital names of the country.

        Args:
            country (Dict): A dictionary containing country data.

        Returns:
            Union[str, None]: A comma-separated string of capital names, or None if not found.
        """
        return ', '.join(country.get('capital', []))

    @staticmethod
    def get_flag(country: Dict, image_type: str = 'png') -> Union[str, None]:
        """
        Extracts the flag URL of the country in the specified image type.

        Args:
            country (Dict): A dictionary containing country data.
            image_type (str): The type of the flag image.

        Returns:
            Union[str, None]: The flag URL of the country, or None if not found.
        """
        return country.get('flags', {}).get(image_type)

    def get_countries(self, raw_country_data: List[Dict]) -> Union[List[List[Union[str, None]]], None]:
        """
        Transforms raw country data into a list of country details.

        Args:
            raw_country_data (List[Dict]): A list of dictionaries containing raw country data.

        Returns:
            Union[List[List[Union[str, None]]], None]: A list of lists containing country details
            (name, capital names, flag url), or None if data is invalid.
        """
        if not isinstance(raw_country_data, list):
            return None

        return [[self.get_name(country),
                 self.get_capital_names(country),
                 self.get_flag(country)]
                for country in raw_country_data]
