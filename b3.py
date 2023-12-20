from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from selenium.webdriver.chrome.options import Options

def count_b3():
    yesterday = datetime.now() - timedelta(days=1)
    date = yesterday.strftime('%d/%m/%Y')

    # Configuração do WebDriver (neste exemplo, usando o Chrome)
    # Configurar as opções do Chrome para modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Instanciar o driver do Selenium com as opções configuradas
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(f"https://www.b3.com.br/pt_br/regulacao/oficios-e-comunicados/oficios-e-comunicados/?dataIni={date}&dataFim={date}")

    count = 0

    while True:
        # Verifica se há itens encontrados
        items = driver.find_elements(By.CLASS_NAME, "primary-text")
        if len(items) == 0:
            count = 0
            break

        count += len(items)

        # Verifica se há um próximo botão de página
        try:
            next_button = driver.find_element(By.XPATH, '/html/body/main/div[4]/div/div[2]/form/div[2]/ul/li[1]/a')
            if next_button.get_attribute("class") == "paginate-link":
                # Clica no botão de próxima página usando JavaScript
                driver.execute_script("arguments[0].click();", next_button)
                # Aguarda até que o novo elemento seja carregado na página seguinte
                WebDriverWait(driver, 10).until(EC.staleness_of(next_button))
            else:
                break
        except NoSuchElementException:
            count = 0
            break

    driver.quit()

    return count

result = count_b3()
print(f"Total de resultados: {result}")
