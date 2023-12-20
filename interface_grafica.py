import tkinter as tk
from tkinter import ttk
import pandas as pd

class ComparadorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Comparador de Dados")

        # Carrega os dados do Excel
        self.dados = pd.read_excel("dados_requisicoes_teste.xlsx")

        # Cria uma tabela na interface gráfica
        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ("Script", "Valor", "Comparação")
        self.tree.heading("Script", text="Script")
        self.tree.heading("Valor", text="Valor")
        self.tree.heading("Comparação", text="Comparação")
        
        # Remove a coluna vazia
        self.tree["show"] = "headings"
        
        # Preenche a tabela com os dados do Excel
        for i in range(0, len(self.dados), 2):  # Passa por cada par de linhas
            script_atual = self.dados.at[i, "Script"]
            valor_atual = self.dados.at[i, "Valor"]
            
            script_proximo = self.dados.at[i+1, "Script"]
            valor_proximo = self.dados.at[i+1, "Valor"]

            comparacao = "✅" if valor_atual == valor_proximo else "❌"  # Emoji de check se igual, cross se diferente

            self.tree.insert("", i, text="", values=(script_atual, valor_atual, comparacao))
            self.tree.insert("", i+1, text="", values=(script_proximo, valor_proximo, comparacao))

        # Adiciona a tabela à interface gráfica
        self.tree.pack(expand=True, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = ComparadorApp(root)
    root.mainloop()
