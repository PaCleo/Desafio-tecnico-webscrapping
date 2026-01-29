from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


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
        EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Produtos']"))
    )
    
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", produtos_btn)

    ActionChains(driver).move_to_element(produtos_btn).pause(1).perform()

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".dropdown-container"))
    )

    print("Menu Produtos aberto ✅")


def get_menu_data(driver):
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".nav-dropdown__item"))
    )

    segmentos = {}

    colunas = driver.find_elements(By.CSS_SELECTOR, ".nav-dropdown__item")

    for coluna in colunas:
        try:
            titulo_element = coluna.find_element(By.CSS_SELECTOR, "a.nav-dropdown__heading")
            segmento_nome = titulo_element.text.strip()

            produtos = []

            itens = coluna.find_elements(By.CSS_SELECTOR, "a.nav-dropdown__link")

            for item in itens:
                nome_produto = item.text.strip()
                url_produto = item.get_attribute("href")

                if nome_produto and url_produto:
                    produtos.append({
                        "nome": nome_produto,
                        "url": url_produto
                    })

            if segmento_nome:
                segmentos[segmento_nome] = produtos

        except:
            continue

    return segmentos
