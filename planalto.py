def count_planalto():
    from selenium import webdriver
    import time
    from datetime import date, datetime, timedelta
    import re

    # Define a variável month_mapping no início do script
    month_mapping = {
        '01': 'janeiro',
        '02': 'fevereiro',
        '03': 'março',
        '04': 'abril',
        '05': 'maio',
        '06': 'junho',
        '07': 'julho',
        '08': 'agosto',
        '09': 'setembro',
        '10': 'outubro',
        '11': 'novembro',
        '12': 'dezembro'
    }

    def extract_date_from_text(text):
        match = re.search(r'(\d{1,2}) de (\w+)', text)
        if match:
            day = int(match.group(1))
            month = match.group(2)
            return f"{day:02d} de {month}"
        return None

    def get_links_count_for_specific_date(target_date):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome()
        
        yesterday = datetime.now() - timedelta(days=1)
        year = yesterday.strftime('%Y')
        month = yesterday.strftime('%B').lower()

        # Usa a variável month_mapping para obter o nome do mês em português
        month = month_mapping.get(month, month)

        driver.get('http://www4.planalto.gov.br/legislacao/portal-legis/resenha-diaria/dezembro-resenha-diaria')

        time.sleep(15)

        js_path = """
        var trElements = document.querySelectorAll("#visao4 > table > tbody > tr");
        var results = [];

        trElements.forEach(function(trElement) {
            results.push(trElement.outerHTML);
        });

        return results;
        """

        results = driver.execute_script(js_path)

        pattern = r'http\S+'

        links_count_for_target_date = 0

        for result in results:
            links = re.findall(pattern, result)
            date = extract_date_from_text(result)

            if date and date == target_date:
                # Incrementa a contagem de links para a data correspondente
                links_count_for_target_date += len(links)

        # Exibe o resultado no terminal
        print(links_count_for_target_date)

        driver.quit()

        # Retorna o número de links para a data desejada
        return links_count_for_target_date

    # Comenta a variável target_date
    # target_date = "07/12/2023"

    # Adiciona uma linha para comparar a data formatada com a data atual
    data_atual = date.today()
    data_formatada = data_atual.strftime("%d de %B")
    data_formatada = data_formatada.lower().replace(data_atual.strftime("%B"), month_mapping[data_atual.strftime("%m")])

    # Passa a data formatada para a função get_links_count_for_specific_date
    get_links_count_for_specific_date(data_formatada)

# Chama a função planalto e imprime o resultado
print(count_planalto())
