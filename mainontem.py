import subprocess
import pandas as pd
from openpyxl import Workbook
#import time

# Importe seus scripts de requisição

import anvisav3
import bacenv3
import agudouv3
import gabinetemcomdouv3
import aguv3
import anbimav3
import ancinedouv3
import aneelv3
import anpv3
import b3v3
import congnaciodouv3
import receitafederalv3
import cnpsdouv3
import bacendouv3
import receitafederaldouv3
import atospoderexev3
import poderlegisdouv3
import anpddouv3
import bndesdouv3
import cmndouv3
import cvmv3
import cadedouv3
import coafdouv3
import gabinetemjspdouv3
import contrandouv3
import ccfgtsdouv3
import presidenciadarepublicav3
import camexdouv3
import codefatdouv3
import pgfndouv3
import gabinetemdrdouv3
import gabinetemctidouv3
import gabinetemedouv3
import gabinetemfdouv3
import gabinetempsdouv3
import gabineteminfradouv3
import sedggdouv3
import gabinetemtedouv3
import gabinetemtpdouv3
import seddmdouv3
import sfppdouv3
import stndouv3
import conselhoppidouv3
import cefdouv3
import confazdouv3
import inssdouv3
import planaltov3
import cs_presidenciadarepublicav3
import cs_governodoestadov3
import bndesv3
import abecsv3
import anpdv3
import cfcv3
import cguv3
import siscoafv3
import anateldouv3



# Especifique o caminho para o ChromeDriver
#path = "C:/Program Files/chromedriver/chromedriver.exe"
# Inicialize o driver do Chrome
#driver = webdriver.Chrome(executable_path=path)
#driver = webdriver.Chrome()

def retry_on_failure(func, max_retries=10):
    for i in range(max_retries):
        try:
            return func()
        except Exception as e:
            print(f"Erro ao executar {func.__name__}: {e}")
            print("Tentando novamente...")
            # time.sleep(5)  # Espere um pouco antes de tentar novamente
    raise Exception(f"Erro ao executar {func.__name__} após {max_retries} tentativas")

def main():
     # Defina a data desejada
    data_desejada = '28-11-2023'  # Substitua isso pela data que você deseja


    # Crie uma lista de dicionários para armazenar as informações dos scripts
    scripts = [

        {'nome': 'ANVISA', 'funcao': lambda: subprocess.run(['python', 'anvisa.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'BACEN', 'funcao': lambda: subprocess.run(['python', 'bacen.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'Gabinete-MCOM/DOU', 'funcao': lambda: subprocess.run(['python', 'gabinetemcomdouv3.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'AGU', 'funcao': lambda: subprocess.run(['python', 'agu.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'AGU/DOU', 'funcao': lambda: subprocess.run(['python', 'agudou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'ANBIMA', 'funcao': lambda: subprocess.run(['python', 'anbima.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'ANCINE/DOU', 'funcao': lambda: subprocess.run(['python', 'ancinedou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'ANEEL', 'funcao': lambda: subprocess.run(['python', 'aneel.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'ANP', 'funcao': lambda: subprocess.run(['python', 'anp.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'B3', 'funcao': lambda: subprocess.run(['python', 'b3.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'Congresso Nacional/DOU', 'funcao': lambda: subprocess.run(['python', 'congressonacionaldou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'RECEITA FEDERAL', 'funcao': lambda: subprocess.run(['python', 'receitafederal.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'CNPS/DOU', 'funcao': lambda: subprocess.run(['python', 'cnpsdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'BACEN/DOU', 'funcao': lambda: subprocess.run(['python', 'bacendou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'RECEITA FEDERAL/DOU', 'funcao': lambda: subprocess.run(['python', 'receitafederaldou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'PODER EXECUTIVO/DOU', 'funcao': lambda: subprocess.run(['python', 'atospoderexecutivo.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'PODER LEGISLATIVO/DOU', 'funcao': lambda: subprocess.run(['python', 'poderlegislativodou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'ANPD/DOU', 'funcao': lambda: subprocess.run(['python', 'anpddou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'BNDES/DOU', 'funcao': lambda: subprocess.run(['python', 'bndesdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'CMN/DOU', 'funcao': lambda: subprocess.run(['python', 'cmndou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'CVM', 'funcao': lambda: subprocess.run(['python', 'cvm.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'CADE/DOU', 'funcao': lambda: subprocess.run(['python', 'cadedou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'COAF/DOU', 'funcao': lambda: subprocess.run(['python', 'coafdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'GABINETE-MJSP/DOU', 'funcao': lambda: subprocess.run(['python', 'gabinetemjsp.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'CONTRAN/DOU', 'funcao': lambda: subprocess.run(['python', 'contrandou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'CCFGTS/DOU', 'funcao': lambda: subprocess.run(['python', 'ccfgtsdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'Casa Cívil - Presidencia da Republica/DOU', 'funcao': lambda: subprocess.run(['python', 'presidenciadarepublicadou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'CAMEX/DOU', 'funcao': lambda: subprocess.run(['python', 'camexdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'CODEFAT/DOU', 'funcao': lambda: subprocess.run(['python', 'codefatdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'PGFN/DOU', 'funcao': lambda: subprocess.run(['python', 'pgfndou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'GABINETE-MDR/DOU', 'funcao': lambda: subprocess.run(['python', 'gabinetemdrdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'GABINETE-MCTI/DOU', 'funcao': lambda: subprocess.run(['python', 'gabinetemctidou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'GABINETE-ME/DOU', 'funcao': lambda: subprocess.run(['python', 'gabinetemedou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'GABINETE-MF/DOU', 'funcao': lambda: subprocess.run(['python', 'gabinetemfdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'GABINETE-MPS/DOU', 'funcao': lambda: subprocess.run(['python', 'gabinetempsdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'GABINETE-MINFRA/DOU', 'funcao': lambda: subprocess.run(['python', 'gabineteminfradou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'SEDGG/DOU', 'funcao': lambda: subprocess.run(['python', 'sedggdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'GABINETE-MTE/DOU', 'funcao': lambda: subprocess.run(['python', 'gabinetemtedou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'GABINETE-MTP/DOU', 'funcao': lambda: subprocess.run(['python', 'gabinetemtpdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'SEDDM/DOU', 'funcao': lambda: subprocess.run(['python', 'seddmdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'SFPP/DOU', 'funcao': lambda: subprocess.run(['python', 'sfppdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'STN/DOU', 'funcao': lambda: subprocess.run(['python', 'stndou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'CONSELHO PPI', 'funcao': lambda: subprocess.run(['python', 'conselhoppidou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'CEF/DOU', 'funcao': lambda: subprocess.run(['python', 'cefdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'CONFAZ/DOU', 'funcao': lambda: subprocess.run(['python', 'confazdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'INSS/DOU', 'funcao': lambda: subprocess.run(['python', 'inssdou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'CASA CIVIL/DOU', 'funcao': lambda: subprocess.run(['python', 'casacivildou.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'Casa Cívil- Governo do Estado/DOU', 'funcao': lambda: subprocess.run(['python', 'cs_governodoestado.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'PLANALTO', 'funcao': lambda: subprocess.run(['python', 'planalto.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'BNDES', 'funcao': lambda: subprocess.run(['python', 'bndes.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'AGU Planalto', 'funcao': lambda: subprocess.run(['python', 'aguplanalto.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'ABECS', 'funcao': lambda: subprocess.run(['python', 'abecs.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'ANPD', 'funcao': lambda: subprocess.run(['python', 'anpd.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'CFC', 'funcao': lambda: subprocess.run(['python', 'cfc.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'CGU', 'funcao': lambda: subprocess.run(['python', 'cgu.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'SISCOAF', 'funcao': lambda: subprocess.run(['python', 'siscoaf.py', data_desejada], capture_output=True, text=True).stdout.strip()},
        {'nome': 'ANATEL/DOU', 'funcao': lambda: subprocess.run(['python', 'anateldou.py', data_desejada], capture_output=True, text=True).stdout.strip()},

        #Aqui segue requisição v3
        {'nome': 'BACEN-V3', 'funcao': bacenv3.requisicao_bacen_v3},
        {'nome': 'Gabinete-MCOM/DOU-V3', 'funcao': gabinetemcomdouv3.mcomv3},
        {'nome': 'AGU-V3', 'funcao': aguv3.AGUV3},
        {'nome': 'AGU/DOU-V3', 'funcao': agudouv3.AGUDOUV3},
        {'nome': 'ANBIMA-V3', 'funcao': anbimav3.anbimav3},
        {'nome': 'ANCINE/DOU-V3', 'funcao': ancinedouv3.ancinedouv3},
        {'nome': 'ANEEL-V3', 'funcao': aneelv3.aneelv3},
        {'nome': 'ANP-V3', 'funcao': anpv3.anpv3},
        {'nome': 'B3-V3', 'funcao': b3v3.b3v3},
        {'nome': 'Congresso Nacional/DOU-V3', 'funcao': congnaciodouv3.congressonacionaldouv3},
        {'nome': 'RECEITA FEDERAL-V3', 'funcao': receitafederalv3.receitafederalv3},
        {'nome': 'CNPS/DOU-V3', 'funcao': cnpsdouv3.cnpsdouv3},
        {'nome': 'BACEN/DOU-v3', 'funcao': bacendouv3.bacendouv3},
        {'nome': 'RECEITA FEDERAL/DOU-V3', 'funcao': receitafederaldouv3.receitafederaldouv3},
        {'nome': 'PODER EXECUTIVO/DOU-V3', 'funcao': atospoderexev3.atospoderexev3},
        {'nome': 'PODER LEGISLATIVO/DOU-V3', 'funcao': poderlegisdouv3.poderlegisdouv3},
        {'nome': 'ANPD/DOU-V3', 'funcao': anpddouv3.anpddouv3},
        {'nome': 'BNDES/DOU-v3', 'funcao': bndesdouv3.bndesv3},
        {'nome': 'CMN/DOU-v3', 'funcao': cmndouv3.cmndouv3},
        {'nome': 'CVM-V3', 'funcao': cvmv3.cvmv3},
        {'nome': 'CADE/DOU-V3', 'funcao': cadedouv3.cadedouv3},
        {'nome': 'COAF/DOU-v3', 'funcao': coafdouv3.coafdouv3},
        {'nome': 'GABINETE-MJSP/DOU-V3', 'funcao': gabinetemjspdouv3.gabinetemjspv3},
        {'nome': 'CONTRAN/DOU-V3', 'funcao': contrandouv3.gabinetemjspv3},
        {'nome': 'CCFGTS/DOU-V3', 'funcao': ccfgtsdouv3.ccfgtsdouv3},
        {'nome': 'Casa Cívil - Presidencia da Republica/DOU-V3', 'funcao': presidenciadarepublicav3.presidenciadarepublicadouv3},
        {'nome': 'CAMEX/DOU-V3', 'funcao': camexdouv3.camexdouv3},
        {'nome': 'CODEFAT/DOU-V3', 'funcao': codefatdouv3.codefatdouv3},
        {'nome': 'PGFN/DOU-V3', 'funcao': pgfndouv3.pgfndouv3},
        {'nome': 'GABINETE-MDR/DOU-v3', 'funcao': gabinetemdrdouv3.gabinetemdrdouv3},
        {'nome': 'GABINETE-MCTI/DOU-v3', 'funcao': gabinetemctidouv3.gabinetemctidouv3},
        {'nome': 'GABINETE-ME/DOU-v3', 'funcao': gabinetemedouv3.gabinetemedouv3},
        {'nome': 'GABINETE-MF/DOU-v3', 'funcao': gabinetemfdouv3.gabinetemfdouv3},
        {'nome': 'GABINETE-MPS/DOU-v3', 'funcao': gabinetempsdouv3.gabinetempsdouv3},
        {'nome': 'GABINETE-MINFRA/DOU-v3', 'funcao': gabineteminfradouv3.gabineteminfradouv3},
        {'nome': 'SEDGG/DOU-v3', 'funcao': sedggdouv3.sedggdouv3},
        {'nome': 'GABINETE-MTE/DOU-v3', 'funcao': gabinetemtedouv3.gabinetemtedouv3},
        {'nome': 'GABINETE-MTP/DOU-v3', 'funcao': gabinetemtpdouv3.gabinetemtpdouv3},
        {'nome': 'SEDDM/DOU-v3', 'funcao': seddmdouv3.seddmdouv3},
        {'nome': 'SFPP/DOU-v3', 'funcao': sfppdouv3.sfppdouv3},
        {'nome': 'STN/DOU-v3', 'funcao': stndouv3.stndouv3},
        {'nome': 'CONSELHO PPI-v3', 'funcao': conselhoppidouv3.conselhoppidouv3},
        {'nome': 'CEF/DOU-v3', 'funcao': cefdouv3.cefdouv3},
        {'nome': 'CONFAZ/DOU-v3', 'funcao': confazdouv3.confazdouv3},
        {'nome': 'INSS/DOU-v3', 'funcao': inssdouv3.inssdouv3},
        {'nome': 'CASA CIVIL/DOU-v3', 'funcao': cs_presidenciadarepublicav3.cspresidenciarepublicav3},
        {'nome': 'ANVISA-v3', 'funcao': anvisav3.anvisav3},
        {'nome': 'Casa Cívil- Governo do Estado/DOU-v3', 'funcao': cs_governodoestadov3.cs_governodoestadov3},
        {'nome': 'PLANALTO-V3', 'funcao': planaltov3.planaltov3},
        {'nome': 'BNDES-V3', 'funcao': bndesv3.bndesv3},
        {'nome': 'AGU Planalto-v3', 'funcao': aguv3.AGUV3},
        {'nome': 'ABECS-V3', 'funcao': abecsv3.abecsv3},
        {'nome': 'ANPD-V3', 'funcao': anpdv3.anpdv3},
        {'nome': 'CFC-V3', 'funcao': cfcv3.cfcv3},
        {'nome': 'CGU-V3', 'funcao': cguv3.cguv3},
        {'nome': 'SISCOAF-V3', 'funcao': siscoafv3.siscoafv3},
        {'nome': 'ANATEL/DOU-V3', 'funcao': anateldouv3.anateldouv3},


    ]

    # Crie um DataFrame vazio
    df = pd.DataFrame(columns=['Script', 'Valor'])

    # Use um loop para adicionar cada script ao DataFrame
    for script in scripts:
        nome = script['nome']
        funcao = script['funcao']
        
        # Verifique se a função é realmente uma função antes de chamá-la
        if callable(funcao):
            valor = retry_on_failure(funcao)
        else:
            print(f"Erro: {nome} não é uma função, é um {type(funcao)}")
            continue

        nova_linha = pd.DataFrame({'Script': [nome], 'Valor': [str(valor)]})
        df = pd.concat([df, nova_linha], ignore_index=True)

    # Escreva o DataFrame em um arquivo Excel
    df.to_excel('dados_requisicoes_ontem.xlsx', index=False)

    # driver.quit()

if __name__ == '__main__':
    main()
