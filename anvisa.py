from selenium import webdriver
import time
from datetime import datetime
import sys

def count_anvisa(data_desejada=None):
    def get_titles_links_and_compare_dates(driver, target_date):
        js_path_titles = """
        var titles = [];
        var elements = document.querySelectorAll("#p_p_id_legislacao_WAR_etapasregulatoriasportlet_ > div > div > div > div > div > div.listagem > ul > li > h2 > a");
        elements.forEach(function(element) {
            titles.push(element.innerText);
        });
        return titles;
        """

        js_path_links = """
        var links = [];
        var elements = document.querySelectorAll("#p_p_id_legislacao_WAR_etapasregulatoriasportlet_ > div > div > div > div > div > div.listagem > ul > li > h2 > a");
        elements.forEach(function(element) {
            links.push(element.getAttribute('href'));
        });
        return links;
        """

        titles = driver.execute_script(js_path_titles)
        links = driver.execute_script(js_path_links)

        full_links = ["https://antigo.anvisa.gov.br/legislacao" + link for link in links]

        # Comparar datas
        results = []
        for title, full_link in zip(titles, full_links):
            #print("=== Verificando Título e Data ===")
            #print("Título:", title)
            #print("Link Completo:", full_link)

            # Extrair a data do título
            date_str = title.split("de")[-1].strip()
            try:
                # Converter a string de data para um objeto datetime
                date_obj = datetime.strptime(date_str, "%d/%m/%Y")
                #print("Data encontrada:", date_obj.strftime("%d/%m/%Y"))

                # Comparar com a data alvo
                if date_obj == target_date:
                    result = 1
                else:
                    result = 0
                results.append(result)
                #print("Resultado da comparação:", result)
            except ValueError:
                print("Formato de data inválido")

            #print()

        return results

    # Inicialize o driver do Selenium (certifique-se de ter o driver adequado instalado)
    driver = webdriver.Chrome()

    # Abra a URL desejada
    url = "https://antigo.anvisa.gov.br/legislacao#/"
    driver.get(url)

    # Aguarde alguns segundos para garantir que a página seja totalmente carregada
    time.sleep(10)

    # Comente a linha da "Data alvo para comparação"
    # target_date = datetime(2023, 10, 26)  # Substitua com a data desejada

    # Adicione uma nova linha para usar a data desejada como um argumento
    target_date = datetime.strptime(data_desejada, '%d-%m-%Y')

    # Inicialize uma lista para armazenar os resultados de cada página
    all_results = []

    # Loop através das páginas
    for page in range(1):
        # Obter resultados da comparação da página atual
        results = get_titles_links_and_compare_dates(driver, target_date)

        # Armazenar os resultados da página atual na lista
        all_results.extend(results)

    # Somar todos os resultados
    total_result = sum(all_results)

    # Imprimir o resultado total
    #print("=== Resultado Total ===")
    #print("Total de datas iguais em todas as páginas:", total_result)

    # Feche o navegador
    driver.quit()

    # Retornar o resultado total
    return total_result

# Chamando a função e obtendo o resultado total
resultado_total = count_anvisa(sys.argv[1])

# Agora você pode usar 'resultado_total' como desejar
print(resultado_total)
