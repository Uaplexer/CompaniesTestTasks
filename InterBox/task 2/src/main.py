from constants import HEADERS, COOKIES, TEST_URL
from utils import create_cookie_jar, save_data_for_json
from modules import EbayProductRetriever, MySession

if __name__ == '__main__':
    session = MySession()
    session.headers = HEADERS
    session.cookies.update(create_cookie_jar(COOKIES))

    html_content = session.get_response_text(TEST_URL)
    retriever = EbayProductRetriever(html_content)
    data = retriever.get_product_info()

    save_data_for_json(data, f'data/{data.get('title').replace('/', '-')}.json')
