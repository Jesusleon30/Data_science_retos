import requests
from bs4 import BeautifulSoup
from prefect import task

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

@task(name="Extraer productos de Amazon")
def task_extract_products(query):
    products = []
    url = f"https://www.amazon.it/s?k={query}"
    
    # Realizar la solicitud a la página de Amazon
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html = BeautifulSoup(response.content, "html.parser")
        product_elements = html.find_all("div", {"data-component-type": "s-search-result"})
        
        for product_element in product_elements:
            title_element = product_element.find("span", class_="a-size-base-plus a-color-base a-text-normal")
            price_element = product_element.find("span", class_="a-price-whole")
            
            product_title = title_element.get_text(strip=True) if title_element else "N/A"
            product_price = price_element.get_text(strip=True) if price_element else "N/A"

            products.append((product_title, product_price))
    return products