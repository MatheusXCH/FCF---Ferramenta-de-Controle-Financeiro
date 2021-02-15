#CONJUNTO DE FUNÇÕES 

import unidecode
import pandas
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output

#Handles string entry for month
def confere_mes(mes):
    '''
    Verifica se o mês foi inserido corretamente, tratando acentuações. Caso incorreto, solicita o mês novamente.
        Argumentos:
            mes: String (string qualquer)

        Retorna: 
            mes: String (verificada e tratada)
    '''
    
    mes = unidecode.unidecode(mes)
    
    #While mes != a valid month, keep reading "mes" from the user
    while(mes != "JANEIRO" and mes != "FEVEREIRO" and mes != "MARCO" and mes != "ABRIL" and 
        mes != "MAIO" and mes != "JUNHO" and mes != "JULHO" and mes != "AGOSTO" and 
        mes != "SETEMBRO" and mes != "OUTUBRO" and mes != "NOVEMBRO" and mes != "DEZEMBRO"):
        
        mes = input('Mês inválido! Por favor, escreva o nome do mês por extenso: ').upper() #Put it always on upper case
        mes = unidecode.unidecode(mes)

    return mes #Return the correct value
        
#Create data
def cadastro(dataframe: pandas.DataFrame):
    '''
    Cadastra novas fontes de renda no Dataframe
    '''
    
    nome = input("Nome da receita: ").upper()
    dia = int(input("Dia: "))
    mes = input("Mes [por extenso]: ").upper()
    
    mes = confere_mes(mes) #Check if this is a valid month value
    
    valor = float(input("Valor (R$): "))
    forma = input("Método: ").upper()
    
    #Append the new info. on dataframe
    dataframe = dataframe.append(
        {
            "nome": nome,
            "dia": int(dia),
            "mes": mes,
            "valor": valor,
            "forma_pgto": forma
        }, ignore_index = True
    )
    return dataframe #Return the dataframe with new info.

#Read data
def consulta_mes(mes, receitas: pandas.DataFrame, despesas: pandas.DataFrame):
    '''
    Faz a consulta das Receitas e Despesas de um determinado mês
    '''

    mes = confere_mes(mes) #Check if this is a valid month value
    
    print(f'\n\nRECEITAS DE "{mes}": ')
    receitas_aux = receitas.loc[receitas["mes"] == mes] #Get only Revenues of month "mes"
    print(receitas_aux) #Show month revenues to user
    
    print(f'\n\DESPESAS DE "{mes}": ')
    despesas_aux = despesas.loc[despesas["mes"] == mes] #Get only expenses of month "mes"
    print(despesas_aux) #Show month expenses to user
    
    total_mes = receitas_aux["valor"].sum() - despesas_aux["valor"].sum() #Sum of all revenues minus all expenses of the month
    print(f'\n\nSALDO TOTAL DE "{mes}": R$ {total_mes} \n') #Show month total to user

#Upadte data
def atualiza(dataframe: pandas.DataFrame):
    '''
    Atualiza um dado cadastrado no Dataframe "Receitas" ou "Despesas". 
    A atualização é feita excluindo uma linha do Dataframe, seguido pela inserção de uma nova linha.
    '''
    mes = input("Qual mês deseja ALTERAR?").upper()
    mes = confere_mes(mes) #Check if this is a valid month value
    
    dataframe_aux = dataframe.loc[dataframe["mes"] == mes] #Get the data of the month
    print(dataframe_aux) #Show month data to user
    ind = int(input("Indique o index (primeira coluna) do item o qual deseja alterar: ")) #Which is the index of the data to update?
    
    dataframe = dataframe.drop(dataframe.index[ind]) #Drop the line
    dataframe = dataframe.reset_index(drop = True) #Reset indexes
    dataframe = cadastro(dataframe) #Calls Create
    
    return dataframe #Return the updated dataframe 

#Delete data
def excluir(dataframe: pandas.DataFrame):
    '''
    Exclui um dado cadastrado no Dataframe "Receitas" ou "Despesas"
    '''
    
    mes = input("Qual o mês do dado que deseja EXCLUIR?").upper()
    mes = confere_mes(mes) #Check if this is a valid month value
    
    dataframe_aux = dataframe.loc[dataframe["mes"] == mes] #Get the data of the month
    print(dataframe_aux) #Show month data to user
    ind = int(input("Indique o index (primeira coluna) do item o qual deseja excluir: ")) #Which is the index of the data to delete?
    
    dataframe = dataframe.drop(dataframe.index[ind]) #Drop the line
    dataframe = dataframe.reset_index(drop = True) #Reset indexes
    
    return dataframe #Return dataframe without the deleted line

#Update the "total" dataframe values    
def saldo_anual(receitas: pandas.DataFrame, despesas: pandas.DataFrame, total: pandas.DataFrame):
    lista_meses = ["JANEIRO", "FEVEREIRO", "MARCO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"]
    
    #Iterates through all months
    for mes in lista_meses:
        receitas_aux = receitas.loc[receitas["mes"] == mes] #Get month revenues
        despesas_aux = despesas.loc[despesas["mes"] == mes] #Get month expenses
        
        #Sum of month revenues minus sum of month expenses
        total.at[mes, "valor"] = float(receitas_aux["valor"].sum() - despesas_aux["valor"].sum()) 
    
    return total #Return the "total" dataframe

#Make the graphics to plot on "Show all datas" call
def grafico(dataframe, y_):
    '''
    Configuração do gráfico de "Saldo Total" a ser plotado.
    '''
    siglas = ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"] #Month abbreviations
    
    x = siglas #Defining X as "siglas"
    y = dataframe[y_] #Defining Y as y_ parameter
    
    fig, ax = plt.subplots(figsize=(10,5)) #Plots figure
    
    verde = '#32CD32' #Green bar if positive month balance
    vermelho = '#DC143C' #Red bar if negative month balance
    
    #Setting plot
    ax.bar(x, y, color = (dataframe['valor'] > 0).map({True: verde, False: vermelho}))
    ax.set_title("SALDO ANUAL")
    ax.set_xlabel("Meses")
    ax.set_ylabel("R$")
    ax.grid(color = "grey", linestyle = "-", linewidth = 0.5)
    
    plt.show() #Show plot to user

#Show all    
def ver_tudo(receitas: pandas.DataFrame, despesas: pandas.DataFrame, total: pandas.DataFrame):
    '''
    Mostra todas as informações, sendo elas:
        - Todas as receitas cadastradas em quaisquer meses
        - Todas as despesas cadastradas em quaisquer meses
        - Saldo total anual
        - Grafico do saldo total anual
    '''
    
    print(f'\nRECEITAS: ')
    print(receitas) #Show all revenues
    
    print(f'\nDESPESAS: ')
    print(despesas) #Show all expenses
    
    total = saldo_anual(receitas, despesas, total)
    print(f'\nSALDO ANUAL: ')
    print(total) #Show monthly total

    grafico(total, "valor") #Calls the graphics maker function
    