import pandas as pd
from dotenv import load_dotenv
import psycopg2


caminho_do_arquivo = r"/Users/valente/Desktop/scripts/01. Postgree/Origem de dados/V_OCORRENCIA_AMPLA.json"
df = pd.read_json(caminho_do_arquivo, encoding='utf-8-sig')


colunas = ['Numero_da_Ocorrencia', 'Classificacao_da_Ocorrência', 'Data_da_Ocorrencia', 'Municipio', 'UF', 'Regiao', 'Nome_do_Fabricante']
df = df[colunas]
df = df.rename(columns={'Classificacao_da_Ocorrência': 'Classificacao_da_Ocorrencia'})


dbname = 'python'
user = 'postgres'
password = 'senha123'
host = 'localhost'
port = '5432'

conexao = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cursor = conexao.cursor() 

cursor.execute('delete from public.Anac')

for indice,coluna_df in df.iterrows():
    cursor.execute(""" insert into Anac (     
                Numero_da_Ocorrencia, 
                Classificacao_da_Ocorrencia, 
                Data_da_Ocorrencia, 
                Municipio, 
                UF, 
                Regiao, 
                Nome_do_Fabricante
            ) VALUES (%s,%s,%s,%s,%s,%s,%s)
            """ , (
                coluna_df["Numero_da_Ocorrencia"],
                coluna_df["Classificacao_da_Ocorrencia"],
                coluna_df["Data_da_Ocorrencia"],
                coluna_df["Municipio"],
                coluna_df["UF"],
                coluna_df["Regiao"],
                coluna_df["Nome_do_Fabricante"],
            )

                   )

conexao.commit()
cursor.close()
conexao.close()


