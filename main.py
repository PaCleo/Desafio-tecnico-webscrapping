from scraper.browser import start_browser
from scraper.menu import open_homepage, open_products_menu, get_menu_data
import time
import csv
import os

driver = start_browser(headless=False)

try:
    open_homepage(driver)
    time.sleep(2)

    open_products_menu(driver)
    time.sleep(2)

    segmentos = get_menu_data(driver)
    
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'segmentos.csv')

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Segmento', 'Nome do Produto', 'URL'])
        
        for segmento, produtos in segmentos.items():
            for produto in produtos:
                writer.writerow([segmento, produto.get('nome'), produto.get('url')])

    print(f"Dados exportados com sucesso para '{output_file}'")

finally:
    driver.quit()
