# Projeto ANAC - Análise de Ocorrências Aeronáuticas

Este projeto realiza a extração, transformação e carregamento (ETL) de dados de ocorrências aeronáuticas disponibilizados pela Agência Nacional de Aviação Civil (ANAC) para um banco de dados PostgreSQL.

## 📋 Objetivo

Processar dados de ocorrências aeronáuticas para análise, mantendo um banco de dados atualizado com as informações mais recentes.

## 🛠 Tecnologias Utilizadas

- Python 3
- Pandas (para manipulação de dados)
- Psycopg2 (para conexão com PostgreSQL)
- Python-dotenv (para gerenciamento de credenciais)
- Docker (para container do PostgreSQL)

## 📊 Dados Processados

O projeto trabalha com as seguintes colunas do dataset original:

- Número da Ocorrência
- Classificação da Ocorrência
- Data da Ocorrência
- Município
- UF
- Região
- Nome do Fabricante

## ⚙️ Configuração

### Pré-requisitos

- Docker instalado
- Python 3.8+
- Pacotes Python listados em `requirements.txt`

### Setup do Ambiente

1. **Banco de dados PostgreSQL via Docker**:

   ```bash
   docker run --name seu_banco -e POSTGRES_PASSWORD=suasenha -e POSTGRES_USER=postgres -e POSTGRES_DB=python -p 5432:5432 -d postgres:alpine
   ```

2. **Configuração das variáveis de ambiente**:
   Crie um arquivo `.env` na raiz do projeto com:

   ```env
   DB_NAME=
   DB_USER=
   DB_PASSWORD=
   DB_HOST=
   DB_PORT=
   ```

3. **Instalação de dependências**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Execução

1. Coloque o arquivo `V_OCORRENCIA_AMPLA.json` no diretório `/Origem de dados/`
2. Execute o Jupyter Notebook `dados_anac.ipynb`

## 🔄 Fluxo de Processamento

1. Importa dados do arquivo JSON
2. Filtra colunas relevantes
3. Padroniza nomes de colunas
4. Conecta ao banco PostgreSQL
5. Limpa a tabela existente
6. Insere os novos dados processados

## 📝 Notas

- O projeto inclui um mecanismo de limpeza da tabela antes da inserção para garantir que apenas os dados mais recentes sejam mantidos.
- As credenciais do banco de dados são gerenciadas através de variáveis de ambiente para maior segurança.

## 📂 Estrutura de Arquivos

```
/projeto-anac
│   dados_anac.ipynb        # Notebook principal de processamento
│   .env.example            # Modelo de arquivo de configuração
│   requirements.txt        # Dependências do projeto
│   README.md               # Este arquivo
│
└───/Origem de dados       # Diretório para os arquivos JSON de origem
        V_OCORRENCIA_AMPLA.json
```
