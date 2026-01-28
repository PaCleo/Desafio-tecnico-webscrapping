from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

BASE_URL = "https://www.sicrediconexao.com.br"


def open_homepage(driver):
    driver.get(BASE_URL)


def accept_cookies_if_present(driver):
    wait = WebDriverWait(driver, 5)

    try:
        # Botão para aceitar os cookies em caso de usuario novo
        botao = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Permitir Todos')]"))
        )
        botao.click()
        print("Cookies aceitos 🍪")
    except TimeoutException:
        print("Banner de cookies não apareceu (seguindo...)")

    try:
        wait.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".cover"))
        )
    except TimeoutException:
        pass

def open_products_menu(driver):
    wait = WebDriverWait(driver, 10)

    accept_cookies_if_present(driver)

    produtos_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Produtos']"))
    )
    produtos_btn.click()

    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav-dropdown"))
    )


