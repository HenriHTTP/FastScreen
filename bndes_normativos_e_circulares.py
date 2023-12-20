from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def bndes_normativos_e_circulares():
    # Configurando o WebDriver (neste exemplo, estou usando o Chrome)
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Instanciar o driver do Selenium com as opções configuradas
    driver = webdriver.Chrome(options=chrome_options)
    # Abrindo a URL desejada
    url = "https://www.bndes.gov.br/wps/portal/site/home/financiamento/garantias/bndes-fgi/normativos-circulares-bndes-fgi"
    driver.get(url)

    # Esperando a página carregar completamente (você pode ajustar o tempo conforme necessário)
    driver.implicitly_wait(10)

    # Obtendo os elementos usando XPath
    elements = driver.find_elements("xpath", '//*[(@id = "main")]//a')

    titulos_desejados = [
        #Estatuto do BNDES FGI
        "Circular SUP/ADIG nº 65/2023",

        #Regulamentos de Garantia
        "Circular SUP/ADIG nº 50/2023",
        "Circular SUP/ADIG nº 51/2023",

        #Procedimentos operacionais
        "Circular SUP/ADIG nº 09/2023",

        #Procedimentos de habilitação perante o BNDES FGI
        "Circular SUP/ADIG nº 71/2023",
        "Formulário de Recuperação de Crédito - FRC",
        "Formulário de subscrição de cotas para o BNDES FGI - FSC",
        "Formulário de Solicitação de Habilitação Alternativa ao FGI - FALT",
        "Anexo A - Auditoria externa",

        #Lista de produtos, linhas e programas passíveis de garantia do BNDES FGI
        "Circular SUP/ADIG 69/2023",

        #Fator K para cálculo do encargo por concessão de garantia - ECG
        "Circular nº 69/2021",

        #Avisos
        "Aviso nº 15/2023",
        "Aviso nº 01/2020",
        "Aviso nº 01/2019",
        "Aviso nº 01/2018",
        
    ]

    titulos_nao_correspondentes = 0

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

result = bndes_normativos_e_circulares()
print(result)
