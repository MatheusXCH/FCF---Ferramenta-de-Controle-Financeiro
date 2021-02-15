# @Matheus Xavier
# PT-BR
# 
# FCF - Ferramenta de Controle Financeiro (Financial Control Tool)
# v.001
# 
# Descrição:
# CRUD de Receitas e Despesas ao longo dos 12 meses do ano, salvando os dados em arquivos .CSV
#
# Description:
# CRUD of Revenues and Expenses along 12 months of the year, saving data on .CSV files

import unidecode, time, sys
import pandas #Using pandas.Dataframes
import numpy as np
import matplotlib.pyplot as plt #To plot graphics
from IPython.display import clear_output #To clear the console

import lib.layout as lay #File with console messages layouts
import lib.dataframe as df #File with dataframes and their structures
import lib.functions as func #File with all the CRUD functions
import lib.save as save #File with the command to changes on .CSV files

#Setting some pandas options
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', None)
pandas.set_option('display.max_colwidth', None)

exit_flag = False #Main loop control flag

#Trying to read the files in the 'df-files' folder, creating them if not found
try:
  df.receitas = pandas.read_csv('./df-files/receitas.csv')
  df.despesas = pandas.read_csv('./df-files/despesas.csv')
except FileNotFoundError:
  df.receitas.to_csv('./df-files/receitas.csv', index = False)
  df.despesas.to_csv('./df-files/despesas.csv', index = False)
  
#Main loop of the application
while(exit_flag == False):
    print(lay.menu) #Show de "menu" layout on console
    opcao = int(input())

    #Create a new data (Revenue)
    if opcao == 1:
        clear_output()
        
        print(f'-- CADASTRO DE RECEITA --\n')
        df.receitas = func.cadastro(df.receitas) #Call de "Create Data" function with revenues as argument
        print(f'Renda cadastrada com sucesso!') #"All OK" confirm message
        
        save.save_file() #Update .CSV files
        time.sleep(3) #Wait 3 seconds

    #Create a new data (Expense)
    elif opcao == 2:
        clear_output()
        
        print(f'-- CADASTRO DE DESPESA --\n')
        df.despesas = func.cadastro(df.despesas) #Call de "Create Data" function with expenses as argument
        print(f'Despesa cadastrada com sucesso!') #"All OK" confirm message
        
        save.save_file() #Update .CSV files
        time.sleep(3) #Wait 3 seconds
    
    #Read the datas of a particular month    
    elif opcao == 3:
        clear_output()
        
        print(f'-- CONSULTAR MÊS -- \n')
        mes = input("Qual mês deseja consultar?\n").upper()
        func.consulta_mes(mes, df.receitas, df.despesas) #Call the "Read Data" function with month, revenues and expenses as arguments
        
        input("Pressione ENTER para continuar...\n") #Wait until user press ""ENTER" to proceed

    #Update a data (works deleting an old data and then registering a new one)
    elif opcao == 4:
        clear_output()
        
        print(f'-- ATUALIZAR CADASTRO --\n')
        opcao = int(input(f'O que deseja ATUALIZAR? \n1 - Receita \n2 - Despesa \n')) #User choose between revenues (1) or expenses (2)
        if opcao == 1:
            df.receitas = func.atualiza(df.receitas) #Call the "Update Data" function with revenues as argument
        elif opcao == 2:
            df.despesas = func.atualiza(df.despesas) #Call the "Update Data" function with expenses as argument
        else:
            print(f'Opção inválida! Abortando operação...')
        print("Item atualizado com sucesso!") #"All OK" confirm message
        
        save.save_file() #Update .CSV files
        time.sleep(3) #Wait 3 seconds

    #Delete a data
    elif opcao == 5:
        clear_output()
        
        print(f'-- EXCLUIR CADASTRO --\n')
        opcao = int(input(f'O que deseja EXCLUIR? \n1 - Receita \n2 - Despesa \n')) #User choose between revenues (1) or expenses (2)
        if opcao == 1:
            df.receitas = func.excluir(df.receitas) #Call the "Delete Data" function with revenues as argument
        elif opcao == 2:
            df.despesas = func.excluir(df.despesas) #Call the "Delete Data" function with expenses as argument
        else:
            print(f'Opção inválida! Abortando operação...')
        print("Item excluído com sucesso!") #"All OK" confirm message
        
        save.save_file() #Update .CSV files
        time.sleep(3) #Wait 3 seconds

    #Show all datas of all dataframes in two ways: text on console and a graphic
    elif opcao == 6:
        clear_output()
        
        print(f'-- TODOS OS DADOS SALVOS --\n')
        func.ver_tudo(df.receitas, df.despesas, df.total) #Call the "Show All" function with revenues, expenses and total as arguments
        input("Pressione ENTER para continuar... \n") #Wait until user press ""ENTER" to proceed

    #Finish the application
    elif opcao == 0:
        clear_output()
        
        save.save_file() #Update .CSV files (to prevent if there's something that has left)
        print(lay.exit) #Show the Exit layout
        
        exit_flag = True #Changing the control flag, ending the Main loop
        time.sleep(3) #Wait 3 seconds

    #DEFAULT: Invalid option if none of the above
    else:
        print("OPÇÃO INVÁLIDA!\nTente novamente") 
        time.sleep(3) #Wait 3 seconds
    
    clear_output()

#
#
#EOF