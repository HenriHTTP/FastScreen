from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

# Configurando o caminho do seu driver do Chrome
# path = "C:/Caminho/para/o/chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
driver = webdriver.Chrome()

# Abrindo a página
driver.get("http://diario.ac.gov.br/")

# Definindo um tempo limite de espera para aguardar até 10 segundos até que um elemento com id="calendarioBusca" esteja presente
wait = WebDriverWait(driver, 10)
elemento_calendario = wait.until(EC.presence_of_element_located((By.ID, "calendarioBusca")))

# Aguardando um pouco mais para garantir que a página tenha carregado completamente
driver.implicitly_wait(10)

# Obtendo o dia atual
dia_atual = datetime.datetime.now().day

# Encontrando todas as células do calendário
celulas_calendario = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[2]/div/div/table//td/a")

# Iterando sobre as células e clicando no número correspondente ao dia atual
for celula in celulas_calendario:
    numero = celula.text.strip()
    if numero == str(dia_atual):
        celula.click()
        break

# Fechando o navegador
driver.quit()
