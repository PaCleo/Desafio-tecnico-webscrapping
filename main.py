from scraper.browser import start_browser
from scraper.menu import open_homepage, open_products_menu, get_segment_links
import time

driver = start_browser(headless=False)

try:
    open_homepage(driver)
    time.sleep(2)

    open_products_menu(driver)
    

finally:
    driver.quit()
