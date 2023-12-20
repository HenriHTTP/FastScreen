# main.py
import pandas as pd
from openpyxl import Workbook
from selenium import webdriver
import time

# Importe seus scripts de requisição
import bacen
import bacenv3
import gabinetemcomdou
import gabinetemcomdouv3
import agu
import aguv3
import agudou
import agudouv3
import anbima
import anbimav3
import ancinedou
import ancinedouv3
import aneel
import aneelv3
import anp
import anpv3
import b3
import b3v3
import congressonacionaldou
import congnaciodouv3
import receitafederal
import receitafederalv3
import cnpsdou
import cnpsdouv3
import bacendou
import bacendouv3
import receitafederaldou
import receitafederaldouv3
import atospoderexecutivo
import atospoderexev3
import poderlegislativodou
import poderlegisdouv3
import anpddou
import anpddouv3
import bndesdou
import bndesdouv3
import cmndou
import cmndouv3
import cvm
import cvmv3
import cadedou
import cadedouv3
import coafdou
import coafdouv3
import gabinetemjsp
import gabinetemjspdouv3
import contrandou
import contrandouv3
import ccfgtsdou
import ccfgtsdouv3
import presidenciadarepublicadou
import presidenciadarepublicav3
import camexdou
import camexdouv3
import codefat
import codefatdouv3
import pgfndou
import pgfndouv3
import gabinetemdrdou
import gabinetemdrdouv3
import gabinetemctidou
import gabinetemctidouv3
import gabinetemedou
import gabinetemedouv3
import gabinetemfdou
import gabinetemfdouv3
import gabinetempsdou
import gabinetempsdouv3
import gabineteminfradou
import gabineteminfradouv3
import sedggdou
import sedggdouv3
import gabinetemtedou
import gabinetemtedouv3
import gabinetemtpdou
import gabinetemtpdouv3
import seddmdou
import seddmdouv3
import sfppdou
import sfppdouv3
import stndou
import stndouv3
import conselhoppidou
import conselhoppidouv3
import cefdou
import cefdouv3
import confazdou
import confazdouv3
import inssdou
import inssdouv3
import planalto
import planaltov3
import casacivildou
import cs_presidenciadarepublicav3
import anvisa
import anvisav3
import cs_governodoestado
import cs_governodoestadov3
import bndes
import bndesv3
import aguplanalto
import abecs
import abecsv3
import anpd
import anpdv3
import cfc
import cfcv3
import cgu
import cguv3
import siscoaf
import siscoafv3
import anateldou
import anateldouv3

# Especifique o caminho para o ChromeDriver
#path = "C:/Program Files/chromedriver/chromedriver.exe"
# Inicialize o driver do Chrome
#driver = webdriver.Chrome(executable_path=path)
driver = webdriver.Chrome()

def retry_on_failure(func, max_retries=10):
    for i in range(max_retries):
        try:
            return func()
        except Exception as e:
            print(f"Erro ao executar {func.__name__}: {e}")
            print("Tentando novamente...")
            time.sleep(5)  # Espere um pouco antes de tentar novamente
    raise Exception(f"Erro ao executar {func.__name__} após {max_retries} tentativas")

def main():
     # Defina a data desejada
    data_desejada = '13-12-2023'  # Substitua isso pela data que você deseja


    # Crie uma lista de dicionários para armazenar as informações dos scripts
    scripts = [
        {'nome': 'BACEN', 'funcao': lambda: retry_on_failure (bacen.count_bacen)},
        {'nome': 'BACEN-V3', 'funcao': bacenv3.requisicao_bacen_v3},
        {'nome': 'Gabinete-MCOM/DOU', 'funcao':lambda: retry_on_failure (gabinetemcomdouv3.mcomv3)},
        {'nome': 'Gabinete-MCOM/DOU-V3', 'funcao': gabinetemcomdou.count_gabinetemcomdou},
        {'nome': 'AGU', 'funcao': lambda: retry_on_failure (agu.count_agu)},
        {'nome': 'AGU-V3', 'funcao': aguv3.AGUV3},
        {'nome': 'AGU/DOU', 'funcao': lambda: retry_on_failure(agudou.count_agudou)},
        {'nome': 'AGU/DOU-V3', 'funcao': agudouv3.AGUDOUV3},
        {'nome': 'ANBIMA', 'funcao': lambda: retry_on_failure (anbima.anbima)},
        {'nome': 'ANBIMA-V3', 'funcao': anbimav3.anbimav3},
        {'nome': 'ANCINE/DOU', 'funcao': lambda: retry_on_failure(ancinedou.count_ancidedou)},
        {'nome': 'ANCINE/DOU-V3', 'funcao': ancinedouv3.ancinedouv3},
        {'nome': 'ANEEL', 'funcao': lambda: retry_on_failure (aneel.count_aneel)},
        {'nome': 'ANEEL-V3', 'funcao': aneelv3.aneelv3},
        {'nome': 'ANP', 'funcao': lambda: retry_on_failure (anp.count_anp)},
        {'nome': 'ANP-V3', 'funcao': anpv3.anpv3},
        {'nome': 'B3', 'funcao': lambda: retry_on_failure (b3.count_b3)},
        {'nome': 'B3-V3', 'funcao': b3v3.b3v3},
        {'nome': 'Congresso Nacional/DOU', 'funcao': lambda: retry_on_failure(congressonacionaldou.count_congressonacionaldou)},
        {'nome': 'Congresso Nacional/DOU-V3', 'funcao': congnaciodouv3.congressonacionaldouv3},
        {'nome': 'RECEITA FEDERAL', 'funcao': lambda: retry_on_failure (receitafederal.count_receitafederal)},
        {'nome': 'RECEITA FEDERAL-V3', 'funcao': receitafederalv3.receitafederalv3},
        {'nome': 'CNPS/DOU', 'funcao': lambda: retry_on_failure(cnpsdou.count_cnpsdou)},
        {'nome': 'CNPS/DOU-V3', 'funcao': cnpsdouv3.cnpsdouv3},
        {'nome': 'BACEN/DOU', 'funcao': lambda: retry_on_failure(bacendou.count_bacendou)},
        {'nome': 'BACEN/DOU-v3', 'funcao': bacendouv3.bacendouv3},
        {'nome': 'RECEITA FEDERAL/DOU', 'funcao': lambda: retry_on_failure(receitafederaldou.count_receitafederaldou)},
        {'nome': 'RECEITA FEDERAL/DOU-V3', 'funcao': receitafederaldouv3.receitafederaldouv3},
        {'nome': 'PODER EXECUTIVO/DOU', 'funcao': lambda: retry_on_failure(atospoderexecutivo.count_atospoderexecutivo)},
        {'nome': 'PODER EXECUTIVO/DOU-V3', 'funcao': atospoderexev3.atospoderexev3},
        {'nome': 'PODER LEGISLATIVO/DOU', 'funcao': lambda: retry_on_failure(poderlegislativodou.count_poderlegislativodou)},
        {'nome': 'PODER LEGISLATIVO/DOU-V3', 'funcao': poderlegisdouv3.poderlegisdouv3},
        {'nome': 'ANPD/DOU', 'funcao': lambda: retry_on_failure(anpddou.count_anpddou)},
        {'nome': 'ANPD/DOU-V3', 'funcao': anpddouv3.anpddouv3},
        {'nome': 'BNDES/DOU', 'funcao': lambda: retry_on_failure(bndesdou.count_bndesdou)},
        {'nome': 'BNDES/DOU-v3', 'funcao': bndesdouv3.bndesv3},
        {'nome': 'CMN/DOU', 'funcao': lambda: retry_on_failure(cmndou.count_cmndou)},
        {'nome': 'CMN/DOU-v3', 'funcao': cmndouv3.cmndouv3},
        {'nome': 'CVM', 'funcao': lambda: retry_on_failure (cvm.get_legislacao_cvm_result)},
        {'nome': 'CVM-V3', 'funcao': cvmv3.cvmv3},
        {'nome': 'CADE/DOU', 'funcao': lambda: retry_on_failure(cadedou.count_cadedou)},
        {'nome': 'CADE/DOU-V3', 'funcao': cadedouv3.cadedouv3},
        {'nome': 'COAF/DOU', 'funcao': lambda: retry_on_failure(coafdou.count_coafdou)},
        {'nome': 'COAF/DOU-v3', 'funcao': coafdouv3.coafdouv3},
        {'nome': 'GABINETE-MJSP/DOU', 'funcao': lambda: retry_on_failure(gabinetemjsp.count_gabinetemjsp)},
        {'nome': 'GABINETE-MJSP/DOU-V3', 'funcao': gabinetemjspdouv3.gabinetemjspv3},
        {'nome': 'CONTRAN/DOU', 'funcao': lambda: retry_on_failure(contrandou.count_contrandou)},
        {'nome': 'CONTRAN/DOU-V3', 'funcao': contrandouv3.gabinetemjspv3},
        {'nome': 'CCFGTS/DOU', 'funcao': lambda: retry_on_failure(ccfgtsdou.count_ccfgtsdou)},
        {'nome': 'CCFGTS/DOU-V3', 'funcao': ccfgtsdouv3.ccfgtsdouv3},
        {'nome': 'Casa Cívil - Presidencia da Republica/DOU', 'funcao': lambda: retry_on_failure(presidenciadarepublicadou.count_presidenciadarepublicadou)},
        {'nome': 'Casa Cívil - Presidencia da Republica/DOU-V3', 'funcao': presidenciadarepublicav3.presidenciadarepublicadouv3},
        {'nome': 'CAMEX/DOU', 'funcao': lambda: retry_on_failure(camexdou.count_camexdou)},
        {'nome': 'CAMEX/DOU-V3', 'funcao': camexdouv3.camexdouv3},
        {'nome': 'CODEFAT/DOU', 'funcao': lambda: retry_on_failure(codefat.count_codefatdou)},
        {'nome': 'CODEFAT/DOU-V3', 'funcao': codefatdouv3.codefatdouv3},
        {'nome': 'PGFN/DOU', 'funcao': lambda: retry_on_failure(pgfndou.count_pgfndou)},
        {'nome': 'PGFN/DOU-V3', 'funcao': pgfndouv3.pgfndouv3},
        {'nome': 'GABINETE-MDR/DOU', 'funcao': lambda: retry_on_failure(gabinetemdrdou.count_gabinetemdrdou)},
        {'nome': 'GABINETE-MDR/DOU-v3', 'funcao': gabinetemdrdouv3.gabinetemdrdouv3},
        {'nome': 'GABINETE-MCTI/DOU', 'funcao': lambda: retry_on_failure(gabinetemctidou.count_gabinetemctidou)},
        {'nome': 'GABINETE-MCTI/DOU-v3', 'funcao': gabinetemctidouv3.gabinetemctidouv3},
        {'nome': 'GABINETE-ME/DOU', 'funcao': lambda: retry_on_failure(gabinetemedou.count_gabinetemedou)},
        {'nome': 'GABINETE-ME/DOU-v3', 'funcao': gabinetemedouv3.gabinetemedouv3},
        {'nome': 'GABINETE-MF/DOU', 'funcao': lambda: retry_on_failure(gabinetemfdou.count_gabinetemfdou)},
        {'nome': 'GABINETE-MF/DOU-v3', 'funcao': gabinetemfdouv3.gabinetemfdouv3},
        {'nome': 'GABINETE-MPS/DOU', 'funcao': lambda: retry_on_failure(gabinetempsdou.count_gabinetempsdou)},
        {'nome': 'GABINETE-MPS/DOU-v3', 'funcao': gabinetempsdouv3.gabinetempsdouv3},
        {'nome': 'GABINETE-MINFRA/DOU', 'funcao': lambda: retry_on_failure(gabineteminfradou.count_minfradou)},
        {'nome': 'GABINETE-MINFRA/DOU-v3', 'funcao': gabineteminfradouv3.gabineteminfradouv3},
        {'nome': 'SEDGG/DOU', 'funcao': lambda: retry_on_failure(sedggdou.count_sedggdou)},
        {'nome': 'SEDGG/DOU-v3', 'funcao': sedggdouv3.sedggdouv3},
        {'nome': 'GABINETE-MTE/DOU', 'funcao': lambda: retry_on_failure(gabinetemtedou.count_gabinetemtedou)},
        {'nome': 'GABINETE-MTE/DOU-v3', 'funcao': gabinetemtedouv3.gabinetemtedouv3},
        {'nome': 'GABINETE-MTP/DOU', 'funcao': lambda: retry_on_failure(gabinetemtpdou.count_gabinetemtpdou)},
        {'nome': 'GABINETE-MTP/DOU-v3', 'funcao': gabinetemtpdouv3.gabinetemtpdouv3},
        {'nome': 'SEDDM/DOU', 'funcao': lambda: retry_on_failure(seddmdou.count_seddmdou)},
        {'nome': 'SEDDM/DOU-v3', 'funcao': seddmdouv3.seddmdouv3},
        {'nome': 'SFPP/DOU', 'funcao': lambda: retry_on_failure(sfppdou.count_sfppdou)},
        {'nome': 'SFPP/DOU-v3', 'funcao': sfppdouv3.sfppdouv3},
        {'nome': 'STN/DOU', 'funcao': lambda: retry_on_failure(stndou.count_stndou)},
        {'nome': 'STN/DOU-v3', 'funcao': stndouv3.stndouv3},
        {'nome': 'CONSELHO PPI', 'funcao': lambda: retry_on_failure (conselhoppidou.count_conselhoppidou)},
        {'nome': 'CONSELHO PPI-v3', 'funcao': conselhoppidouv3.conselhoppidouv3},
        {'nome': 'CEF/DOU', 'funcao': lambda: retry_on_failure(cefdou.count_cefdou)},
        {'nome': 'CEF/DOU-v3', 'funcao': cefdouv3.cefdouv3},
        {'nome': 'CONFAZ/DOU', 'funcao': lambda: retry_on_failure(confazdou.count_confaz)},
        {'nome': 'CONFAZ/DOU-v3', 'funcao': confazdouv3.confazdouv3},
        {'nome': 'INSS/DOU', 'funcao': lambda: retry_on_failure(inssdou.count_inssdou)},
        {'nome': 'INSS/DOU-v3', 'funcao': inssdouv3.inssdouv3},
        {'nome': 'CASA CIVIL/DOU', 'funcao': lambda: retry_on_failure(casacivildou.count_casacivildou)},
        {'nome': 'CASA CIVIL/DOU-v3', 'funcao': cs_presidenciadarepublicav3.cspresidenciarepublicav3},
        {'nome': 'ANVISA', 'funcao': lambda: retry_on_failure (anvisa.count_anvisa, data_desejada)},
        {'nome': 'ANVISA-v3', 'funcao': anvisav3.anvisav3},
        {'nome': 'Casa Cívil- Governo do Estado/DOU', 'funcao': lambda: retry_on_failure(cs_governodoestado.count_casacivilgovernodoestado)},
        {'nome': 'Casa Cívil- Governo do Estado/DOU-v3', 'funcao': cs_governodoestadov3.cs_governodoestadov3},
        {'nome': 'PLANALTO', 'funcao': lambda: retry_on_failure (planalto.count_planalto)},
        {'nome': 'PLANALTO-V3', 'funcao': planaltov3.planaltov3},
        {'nome': 'BNDES', 'funcao':  lambda: retry_on_failure(bndes.bndes)},
        {'nome': 'BNDES-V3', 'funcao': bndesv3.bndesv3},
        {'nome': 'AGU Planalto', 'funcao':  lambda: retry_on_failure(aguplanalto.aguplanalto)},
        {'nome': 'AGU Planalto-v3', 'funcao': aguv3.AGUV3},
        {'nome': 'ABECS', 'funcao':  lambda: retry_on_failure(abecs.abecs)},
        {'nome': 'ABECS-V3', 'funcao': abecsv3.abecsv3},
        {'nome': 'ANPD', 'funcao':  lambda: retry_on_failure(anpd.anpd)},
        {'nome': 'ANPD-V3', 'funcao': anpdv3.anpdv3},
        {'nome': 'CFC', 'funcao':  lambda: retry_on_failure(cfc.cfc)},
        {'nome': 'CFC-V3', 'funcao': cfcv3.cfcv3},
        {'nome': 'CGU', 'funcao':  lambda: retry_on_failure(cgu.cgu)},
        {'nome': 'CGU-V3', 'funcao': cguv3.cguv3},
        {'nome': 'SISCOAF', 'funcao': lambda: retry_on_failure(siscoaf.siscoaf)},
        {'nome': 'SISCOAF-V3', 'funcao': siscoafv3.siscoafv3},
        {'nome': 'ANATEL/DOU', 'funcao': lambda: retry_on_failure(anateldou.anateldou)},
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
            valor = funcao()
        else:
            print(f"Erro: {nome} não é uma função, é um {type(funcao)}")
            continue

        nova_linha = pd.DataFrame({'Script': [nome], 'Valor': [valor]})
        df = pd.concat([df, nova_linha], ignore_index=True)

    # Escreva o DataFrame em um arquivo Excel
    df.to_excel('dados_requisicoes.xlsx', index=False)

    driver.quit()


if __name__ == '__main__':
    main()