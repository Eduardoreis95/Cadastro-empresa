#i Importação das Bibliotecas

import tkinter as tk
from tkinter import ttk
import datetime as dt

# Declaração das Variaveis

regime_tributario = ['Simples Nacional', 'Lucro Presumido', 'Lucro Real']
natureza_juridica = ['Sociedade Unipessoal', 'Sociedade Limitada', 'Eireli', 'Empresa Individual']
lista_codigos = []

janela = tk.Tk()

# Criação da Função

def inserir_codigo():
    natureza = combobox_selecionar_natureza.get()
    regime = combobox_selecionar_regime.get()
    codigo = len(lista_codigos) + 1
    codigo_str = 'COD-{}'.format(codigo)
    lista_codigos.append((natureza, regime, codigo_str))



# Titulo da Janela

janela.title('Ferramenta de Dados de Empresa')

# Corpo da Janela

label_selecionar_natureza = tk.Label(text='Selecione a Natureza Jurídica')
label_selecionar_natureza.grid(row=1, column=1, padx = 10, pady = 10, sticky='nswe', columnspan = 1)

combobox_selecionar_natureza = ttk.Combobox(values=natureza_juridica)
combobox_selecionar_natureza.grid(row=1, column=2, padx = 10, pady = 10, sticky='nswe', columnspan = 1)

label_nome_empresa = tk.Label(text='Nome Empresarial')
label_nome_empresa.grid(row=2, column=1, padx = 10, pady=10, sticky='nswe', columnspan = 1)

entry_nome_empresa = tk.Entry()
entry_nome_empresa.grid(row=3, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

label_selecionar_regime = tk.Label(text='Selecione o Regime Tributário')
label_selecionar_regime.grid(row=4, column=1, padx = 10, pady = 10, sticky='nswe', columnspan = 1)

combobox_selecionar_regime = ttk.Combobox(values=regime_tributario)
combobox_selecionar_regime.grid(row=4, column=2, padx = 10, pady = 10, sticky='nswe', columnspan = 1)

label_capital_social = tk.Label(text='Valor do Capital Social')
label_capital_social.grid(row=5, column=1, padx = 10, pady = 10, sticky='nswe', columnspan = 1)

entry_capital_social = tk.Entry()
entry_capital_social.grid(row=6, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

label_faturamento = tk.Label(text='Qual previsão de faturamento?')
label_faturamento.grid(row=7, column=1, padx = 10, pady = 10, sticky='nswe', columnspan = 1)

entry_faturamento = tk.Entry()
entry_faturamento.grid(row=8, column=1, padx=10, pady=10, sticky='nswe', columnspan=1)

label_numero_socios = tk.Label(text='Digite o numero de soocios (se houver)')
label_numero_socios.grid(row=9, column=1, padx = 10, pady = 10, sticky='nswe', columnspan = 1)

entry_numero_socios = tk.Entry()
entry_numero_socios.grid(row=10, column=1, padx=10, pady=10, sticky='nswe', columnspan =1)

botao_criar_codigo = tk.Button(text='Enviar Formulário', command=inserir_codigo())
botao_criar_codigo.grid(row=11, column=0, padx = 10, pady=10, sticky='nswe', columnspan = 2)

# Inserido as informações como nome, regime tributario, tipo juridico e faturamento

# Falta inserir mais informações

janela.mainloop()

print(lista_codigos)