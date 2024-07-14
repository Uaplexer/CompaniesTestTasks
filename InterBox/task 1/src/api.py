from modules import DataFetcher, CountryDataRetriever


class CountriesAPI:
    """
    API interface for retrieving country data.

    Attributes:
        data_fetcher (DataFetcher): Object responsible for fetching data from the API.
        data_retriever (CountryDataRetriever): Object responsible for retrieving data from the fetched data.
    """

    def __init__(self, data_fetcher: DataFetcher, data_retriever: CountryDataRetriever):
        """
        Initialize CountriesAPI with a specified DataFetcher and DataRetriever instance.

        Args:
            data_fetcher (DataFetcher): Object responsible for fetching data from the API.
            data_retriever (CountryDataRetriever): Object responsible for retrieving data from the fetched data.
        """
        self.data_fetcher = data_fetcher
        self.data_retriever = data_retriever

    def get_countries(self):
        """
        Retrieves country data from the API endpoint with specified response fields.

        Returns:
            list or None: List of lists containing country data, or None if request fails.
        """
        raw_data = self.data_fetcher.get_response_json()
        print(raw_data)
        if raw_data:
            return self.data_retriever.get_countries(raw_data)

        return None
