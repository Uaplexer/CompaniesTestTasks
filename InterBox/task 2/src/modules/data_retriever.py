from bs4 import BeautifulSoup


class EbayProductRetriever:
    """
    A class to retrieve specific product information from HTML using BeautifulSoup.
    """

    def __init__(self, html_page: str):
        """
        Initializes the EbayProductRetriever instance with parsed HTML content.

        Args:
            html_page (str): HTML content of the product page.
        """
        self.soup = BeautifulSoup(html_page, 'lxml')

    def get_url(self):
        """
        Retrieves the canonical URL of the product.

        Returns:
            str or None: The canonical URL of the product, or None if not found.
        """
        url_element = self.soup.find('link', rel='canonical')
        return url_element.get('href') if url_element else None

    def get_title(self):
        """
        Retrieves the title of the product.

        Returns:
            str or None: The title of the product, or None if not found.
        """
        title_element = self.soup.find('h1', class_='x-item-title__mainTitle')
        return title_element.get_text(strip=True) if title_element else None

    def get_price(self):
        """
        Retrieves the price of the product.

        Returns:
            str or None: The price of the product, or None if not found.
        """
        price_element = self.soup.find('div', class_='x-bin-price__content')
        price_element_span = price_element.find('span', class_='ux-textspans')
        return price_element_span.get_text(strip=True) if price_element_span else None

    def get_delivery_price(self):
        """
        Retrieves the delivery price of the product.

        Returns:
            str or None: The delivery price of the product, or None if not found.
        """
        delivery_price_element = self.soup.find('div', class_='ux-labels-values__values-content')
        delivery_price_span = delivery_price_element.find('span', class_='ux-textspans ux-textspans--BOLD')
        return delivery_price_span.get_text(strip=True) if delivery_price_span else None

    def get_seller_name(self):
        """
        Retrieves the seller name of the product.

        Returns:
            str or None: The seller name of the product, or None if not found.
        """
        seller_card_info_element = self.soup.find('div', class_='x-sellercard-atf__info')
        seller_info_element = seller_card_info_element.find('div', class_='x-sellercard-atf__info__about-seller')
        return seller_info_element.get('title') if seller_info_element else None

    def get_image_url(self):
        """
        Retrieves the URL of the product image.

        Returns:
            str or None: The URL of the product image, or None if not found.
        """
        first_image_element = self.soup.find('link', rel='preload', fetchpriority='high')
        return first_image_element.get('href') if first_image_element else None

    def get_product_info(self):
        """
        Retrieves all available product information as a dictionary.

        Returns:
            dict: A dictionary containing the product information.
        """
        data = {
            'title': self.get_title(),
            'price': self.get_price(),
            'delivery_price': self.get_delivery_price(),
            'url': self.get_url(),
            'image_url': self.get_image_url(),
            'seller_name': self.get_seller_name(),
        }
        return data
