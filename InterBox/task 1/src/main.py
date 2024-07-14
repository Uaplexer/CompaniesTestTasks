from prettytable import PrettyTable
from api import CountriesAPI
from constants import ALL_ENDPOINT, TABLE_COLUMN_NAMES, RETRIEVABLE_COLUMN_NAMES, API_URL
from modules import DataFetcher, CountryDataRetriever

if __name__ == '__main__':
    data_fetcher = DataFetcher(API_URL, ALL_ENDPOINT, {'fields': ','.join(RETRIEVABLE_COLUMN_NAMES)})
    data_retriever = CountryDataRetriever()
    
    api = CountriesAPI(data_fetcher, data_retriever)

    data = api.get_countries()

    sorted_data = sorted(data, key=lambda x: ~len(x[0]))
    
    countries_table = PrettyTable(field_names=TABLE_COLUMN_NAMES)
    countries_table.add_rows(sorted_data)

    print(countries_table)
