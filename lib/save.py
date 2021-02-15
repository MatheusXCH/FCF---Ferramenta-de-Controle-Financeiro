import pandas
import lib.dataframe as df

#Function that uptades the .CSV files
def save_file():
    df.receitas.to_csv('./df-files/receitas.csv', index = False)
    df.despesas.to_csv('./df-files/despesas.csv', index = False)
    df.total.to_csv('./df-files/saldo_total.csv', index = True)