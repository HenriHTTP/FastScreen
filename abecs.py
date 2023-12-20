from selenium import webdriver

def abecs():
    # Configuração do WebDriver (certifique-se de ter o WebDriver apropriado para seu navegador instalado)
    driver = webdriver.Chrome()

    # URL alvo
    url = "https://www.abecs.org.br/normas"

    # Acessa a URL
    driver.get(url)

    # Espera até que a página esteja completamente carregada (você pode ajustar o tempo conforme necessário)
    driver.implicitly_wait(10)

    # Utiliza execute_script para obter uma lista de elementos com base no JS Path
    js_path = "#__next > main > section > div > div > div > div.file-list > div > div > a"
    elements = driver.execute_script(f'return document.querySelectorAll("{js_path}")')

    # Lista de títulos desejados
    titulos_desejados = [
        "Normativo 028 - Dispõe sobre a criação do Cadastro Unificado de MCCs, e dá outras providências.",
        "Normativo 027 - Dispõe sobre a certificação dos terminais POSTEF, e dá outras providências.",
        "Normativo 026 - Dispõe sobre os procedimentos a serem adotados sobre o canal de relatos de uso não convencional de contas de pagamento da Abecs, e dá outras providências.",
        "Normativo 025 - Dispõe sobre as especificidades dos negócios envolvendo saque/compra com troco em estabelecimentos comerciais e dá outras providências.",
        "Normativo 024 - Dispõe sobre o pagamento de tributos com cartão de crédito, débito e pré-pago, e dá outras providências.",
        "Normativo 023 - Dispõe sobre a certificação dos terminais PINPAD, e dá outras providências.",
        "Normativo 022 - Dispõe sobre informações mínimas que deverão compor as faturas/demonstrativos de despesas enviados aos Consumidores portadores de cartão de crédito.",
        "Normativo 21 - Dispõe sobre a equalização dos códigos de mensagens que serão disponibilizadas aos estabelecimentos comerciais em transações de pagamento negadas, e dá outras providências.",
        "Normativo 020 - Dispõe sobre o envio gratuito de mensagens de transações realizadas para pessoas com deficiência visual e dá outras providências.",
        "Normativo 019 - Implementação de pagamento por aproximação aditamento ref desabilitação.",
        "Normativo 018 - Dispõe sobre a acessibilidade dos terminais de POS aos deficientes visuais, e dá outras providências",
        "Normativo 017 - Dispõe sobre o fomento da viabilização de compras de alto valor realizadas com a utilização de instrumento de pagamento de débito e dá outras providências.",
        "Normativo 016 - Dispõe sobre as especificidades dos negócios envolvendo conta de pagamento pré-paga de uso geral para pessoa jurídica destinada ao uso do Titular e dá outras providências.",
        "Normativo 015 - Dispõe sobre os procedimentos a serem adotados pelo Emissor na cobrança e renegociação de dívidas com os Consumidores e dá outras providências.",
        "Normativo 014 - Dispõe sobre a oferta de alternativas menos onerosas do que aquelas praticadas no Crédito Rotativo, incluindo o parcelamento do saldo devedor da conta de pagamento pós-paga com taxas de juros menos onerosas do que aquelas praticadas no Crédito Rotativo pelas empresas associadas da Associação Brasileira das Empresas de Cartões de Crédito e Serviços – Abecs e dá outras providências.",
        "Normativo 013 - Dispõe sobre as especificidades envolvendo a emissão de cartões para movimentação de contas de pagamento para pessoas com deficiência ou com mobilidade reduzida.",
        "Normativo 012 - Dispõe sobre a concessão de crédito responsável pelas empresas associadas da Associação Brasileira das Empresas de Cartões de Crédito e Serviços – Abecs e dá outras providências.",
        "Normativo 011 - Dispõe sobre requisitos mínimos para os contratos de credenciamento entre Credenciadora e Facilitadora e dá outras providências",
        "Normativo 010 - Dispõe sobre os procedimentos e processos necessários à contestação de despesas por desacordo comercial e dá outras providências.",
        "Normativo 009 - Dispõe sobre o procedimento preliminar e processo disciplinar instaurados para apurar os indícios e/ou infrações disciplinares praticadas por qualquer Associada da abecs e dá outras providências",
        "Normativo 008 - Dispõe sobre as especificidades dos negócios envolvendo conta de pagamento pré-paga de uso geral para pessoa física destinada ao uso do Consumidor Portador e dá outras providências.",
        "Normativo 007 - Dispõe sobre as informações de pagamento mínimo da fatura de cartão de crédito, e dá outras providências",
        "Normativo 006 - Dispõe sobre o envio de cartão de crédito ao consumidor, e dá outras providências",
        "Normativo 005 - Dispõe sobre a (i) entrega de prospecto de informações essenciais, (ii) entrega de cópia do contrato de adesão aos serviços relativos às contas de pagamento pós-pagas destinadas ao uso do Portador e (iii) a adesão aos serviços relativos às contas de pagamento pós-pagas destinadas ao uso do Portador e dá outras providências.",
        "Normativo 004 - Dispõe sobre a utilização das ferramentas de meios eletrônicos de pagamentos em operações que envolvam transferências de recursos via cartões, e dá outras providências.",
        "Normativo 003 - Dispõe sobre o fomento e aprimoramento do comércio eletrônico com pagamento realizado por meio do sistema de cartão, e dá outras providências",
        "Normativo 002 - Dispõe sobre registro de ocorrências realizado pelos consumidores portadores de cartões, e dá outras providências",
        "Normativo 001 - Dispõe sobre as normas e as condições aplicáveis ao processo de Certificação de aderência dos processos das Associadas ao disposto na Autorregulação da Abecs e dá outras providências.",
        "Circular 1 - Anexo ao Normativo 001",
        "Circular 2 - Anexo ao Normativo 001",
        "Circular 3 - Anexo ao Normativo 001",
        "Código de Ética e Autorregulação",
        "Anexo II - Anexo ao Código de Ética e Autorregulação",
    ]

    # Variável para contabilizar títulos não correspondentes
    titulos_nao_correspondentes = 0

    # Itera sobre os elementos encontrados
    for element in elements:
        element_text = element.text

        # Verifica se o título não está na lista de títulos desejados
        if element_text not in titulos_desejados:
            print(f"Título não correspondente: {element_text}")
            titulos_nao_correspondentes += 1

    # Fecha o navegador
    driver.quit()

    # Retorna o número de títulos não correspondentes como um número inteiro
    return titulos_nao_correspondentes

# Exemplo de chamada da função
result = abecs()
print(result)
