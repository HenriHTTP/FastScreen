# Importa a função bndes_normas do script filho
import bndes_normas
import bndes_programa_emergencial_de_suporte_a_empregos
import bndes_normativos_do_fgi_peac
import bndes_normativos_e_circulares

# Script Pai
def bndes():
    total = 0
    # Lista de funções dos scripts filhos
    funcoes_filhas = [
        bndes_normas.bndes_normas,
        bndes_programa_emergencial_de_suporte_a_empregos.bndes_programa_emergencial_de_suporte_a_empregos,
        bndes_normativos_do_fgi_peac.bndes_normativos_do_fgi_peac,
        bndes_normativos_e_circulares.bndes_normativos_e_circulares,
        # Adicione outras funções aqui conforme necessário
    ]
    
    for funcao in funcoes_filhas:
        resultado = funcao()  # Chama a função do script filho
        total += resultado  # Adiciona o resultado ao total
    
    return total

# Chama o script pai
print(bndes())
