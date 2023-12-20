from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def bndes_normativos_do_fgi_peac():
    # Configurando o driver do Selenium (substitua 'caminho_do_seu_driver' pelo caminho do seu driver)
    # Configurar as opções do Chrome para modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Instanciar o driver do Selenium com as opções configuradas
    driver = webdriver.Chrome(options=chrome_options)
    # URL alvo
    url = "https://www.bndes.gov.br/wps/portal/site/home/financiamento/garantias/peac/normativos-peac"

    # Abrindo a página
    driver.get(url)

    # Aguarde o carregamento completo da página (você pode ajustar o tempo conforme necessário)
    driver.implicitly_wait(10)

    # Obtendo os elementos usando find_elements com By.XPATH
    elements = driver.find_elements(By.XPATH, '//*[(@id = "main")]//a')

    titulos_desejados = [
         #Regulamento 2
    "Circular SUP/ADIG nº 66/2023",
    "FORMULÁRIO DE SOLICITAÇÃO DE ADESÃO AO PROGRAMA + TERMO DE ADESÃO (para novas habilitações)",
        #Taxas de Equivalência 8
    "Aviso SUP/ADIG nº 08/2023",
    "Circular SUP/ADIG n° 04/2023",
    "Circular SUP/ADIG n° 02/2023",
    "Circular SUP/ADIG n° 61/2022",
    "Circular SUP/ADIG n° 56/2022",
    "Circular SUP/ADIG n° 52/2022",
    "Circular SUP/ADIG n° 48/2022",
    "Circular SUP/ADIG n° 44/2022",

        #Outros Normativos 23

    "Aviso SUP/ADIG nº 16/2023",
    "Circular SUP/ADIG nº 70/2023",
    "Circular SUP/ADIG nº 65/2023",
    "Circular SUP/ADIG n° 52/2023",
    "Circular SUP/ADIG nº 42/2023-BNDES, de 07.08.2023",
    "Circular SUP/ADIG nº 19/2023",
    "Circular SUP/ADIG nº 18/2023",
    "Circular SUP/ADIG nº 17/2023",
    "Circular SUP/ADIG nº 14/2023",
    "Aviso SUP/ADIG nº 06/2023",
    "Circular SUP/ADIG nº 05/2023",
    "Aviso SUP/ADIG nº 01/2023",
    "Circular SUP/ADIG n° 70/2022",
    "Circular SUP/ADIG nº 58/2022",
    "Circular SUP/ADIG nº 54/2022",
    "Circular SUP/ADIG nº 51/2022",
    "Circular SUP/ADIG nº 50/2022",
    "Circular SUP/ADIG nº 45/2022",
    "Circular DIR4 nº 01/2022-BNDES",
    "Circular SUP/ADIG nº 40/2022",
    "Circular SUP/ADIG nº 18/2022",
    "Aviso nº 22/2021",
    ","
        ]

    titulos_nao_correspondentes = 0


    # Filtrando elementos vazios ou com texto igual a ',' e obtendo os títulos
    titles = [element.text.strip() for element in elements if element.text.strip() and element.text.strip() != ',']

    # Extraindo e imprimindo os títulos
    for element in elements:
        element_text = element.text.strip()  # Remover espaços em branco no início e no final

        # Verificar se o texto não está vazio após remover espaços em branco
        if element_text and element_text not in titulos_desejados:
                print(f"Título não correspondente: {element_text}")
                titulos_nao_correspondentes += 1

    # Fechando o navegador
    driver.quit()

    return titulos_nao_correspondentes

result = bndes_normativos_do_fgi_peac()
print(result)
