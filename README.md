# 🌎 Currency Tracker 

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-blue.svg?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Version](https://img.shields.io/badge/Version-1.0.0-informational)
![API](https://img.shields.io/badge/API-HG%20Brasil-orange)

Uma aplicação Python elegante para rastrear e armazenar cotações de moedas (Dólar e Euro) em tempo real utilizando a API HG Brasil Finance.

## 📋 Sumário

- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Instalação e Uso](#-instalação-e-uso)
- [Como Funciona](#-como-funciona)
- [Banco de Dados](#-banco-de-dados)
- [API](#-api)
- [Contribuições](#-contribuições)
- [Licença](#-licença)

## 🔭 Visão Geral

O **Currency Tracker** é uma ferramenta desenvolvida em Python para obter, processar e armazenar cotações atuais de moedas estrangeiras (Dólar e Euro) em relação ao Real brasileiro. O sistema utiliza a API Finance da HG Brasil para obter dados em tempo real e armazena essas informações em um banco de dados SQLite para consultas futuras e análises históricas.

## ✨ Funcionalidades

- ✅ **Consulta em Tempo Real**: Obtém cotações atualizadas de Dólar e Euro
- 📊 **Armazenamento Persistente**: Salva os dados em banco SQLite com data e hora da consulta
- 🔄 **Criação Automática de Banco**: Sistema cria o banco de dados e tabelas quando necessário
- 🛡️ **Tratamento de Erros**: Gerenciamento robusto de falhas na API ou na conexão
- 📅 **Registro Temporal**: Cada consulta é registrada com timestamp para análise histórica

## 🛠️ Tecnologias

- **Python**: Base do desenvolvimento
- **SQLite**: Banco de dados leve e portátil
- **Requests**: Biblioteca para requisições HTTP
- **Datetime**: Manipulação de datas e horas
- **HG Brasil Finance API**: Fonte de dados para cotações

## 📁 Estrutura do Projeto

```
currency-tracker/
│
├── CotacoesDeMoeda.py   # Script principal para consulta e armazenamento
├── bdcotacoes.db        # Banco de dados SQLite (gerado automaticamente)
├── .gitignore           # Configurações do Git para ignorar arquivos
└── README.md            # Documentação do projeto
```

## 🚀 Instalação e Uso

1. **Clone o repositório**:
   ```bash
   git clone https://seu-repositorio/currency-tracker.git
   cd currency-tracker
   ```

2. **Instale as dependências**:
   ```bash
   pip install requests
   ```

3. **Configure sua chave API**:
   Edite o arquivo `CotacoesDeMoeda.py` e substitua `"c8c29944"` pela sua chave API HG Brasil.

4. **Execute o script**:
   ```bash
   python CotacoesDeMoeda.py
   ```

## 🔍 Como Funciona

O script `CotacoesDeMoeda.py` executa as seguintes operações:

1. **Verifica/Cria o banco de dados**: Através da função `create_tables()`, o sistema verifica se o banco de dados existe e, caso necessário, cria a tabela `coins`.

2. **Consulta a API**: A função `get_currency_counts()` faz uma requisição à API HG Brasil Finance para obter as cotações atuais.

3. **Processa os dados**: O sistema extrai as informações de compra do Dólar e Euro.

4. **Armazena os resultados**: A função `write_database()` registra os dados recebidos no banco SQLite, incluindo data e hora da consulta.

## 💾 Banco de Dados

O sistema utiliza um banco de dados SQLite com a seguinte estrutura:

```sql
CREATE TABLE coins(
    requestID INTEGER PRIMARY KEY AUTOINCREMENT,
    Date VARCHAR(20) NOT NULL,
    Dolar REAL,
    Euro REAL
);
```

- **requestID**: Identificador único da consulta
- **Date**: Data e hora da consulta no formato DD/MM/AAAA HH:MM:SS
- **Dolar**: Valor do Dólar em Reais
- **Euro**: Valor do Euro em Reais

## 🔌 API

O projeto utiliza a API [HG Brasil Finance](https://hgbrasil.com/status/finance) para obter dados atualizados de cotações. É necessário ter uma chave API válida para o funcionamento adequado do sistema.

Formato da requisição:
```
https://api.hgbrasil.com/finance/quotations?format=json-cors&key=SUA_CHAVE
```

## 👥 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir novos recursos
- Enviar pull requests

---

<div align="center">
  <sub>Desenvolvido com ❤️ para monitoramento financeiro eficiente</sub>
</div>
