#DEFINIÇÃO DE DATAFRAMES
import pandas

#Revenues dataframe
receitas = pandas.DataFrame(
    {
        "nome" : [],
        "dia" : [],
        "mes": [],
        "valor" : [],
        "forma_pgto" : []
    },
)

#Expenses dataframe
despesas = pandas.DataFrame(
    {
        "nome" : [],
        "dia" : [],
        "mes" : [],
        "valor" : [],
        "forma_pgto" : []
    },
)

#Total dataframe
total = pandas.DataFrame({"valor" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]},)
#Total dataframe indexes
total.index = ["JANEIRO", "FEVEREIRO", "MARCO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"]


#Some type definitions for the dataframes
receitas["dia"] = receitas["dia"].astype(int)
despesas["dia"] = despesas["dia"].astype(int)

receitas["valor"] = receitas["valor"].astype(float)
despesas["valor"] = despesas["valor"].astype(float)

total["valor"] = total["valor"].astype(float)