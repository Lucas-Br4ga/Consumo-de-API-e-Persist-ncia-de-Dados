import sqlite3
import datetime
import requests
def create_tables():
    conecction = sqlite3.connect('bdcotacoes.db')
    cursor = conecction.cursor()

    sql ='create table coins(' \
        'requestID integer primary key autoincrement,'\
        'Date varchar(20) not null,'\
        'Dolar real,'\
        'Euro real)'

    cursor.execute(sql)
    print("Table 'Coins' table created successfully.")
    conecction.close()


def get_currency_counts():
    key = "c8c29944"
    format = "json-cors"
    url = f"https://api.hgbrasil.com/finance/quotations?format={format}&key={key}"
    request = requests.get(url)
    if not(request.status_code == requests.codes.ok):
        print(f"[ERRO] Falha na requisição - Status: {request.status_code}")
        return None

    try:
        data_json = request.json()
        print("Requisição bem-sucedida. Dados recebidos da API HG Brasil.")
        return data_json
    except ValueError:
        print("[ERRO] Falha ao converter a resposta em JSON.")
        return None




def write_database(currency_data):
    conecction = sqlite3.connect('bdcotacoes.db')
    cursor = conecction.cursor()

    cursor.execute("select name from sqlite_master where type='table' and name='coins'")
    table_exists = cursor.fetchall()
    if not table_exists:
        create_tables()

    date  = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    dolar = currency_data['results']['currencies']['USD']['buy']
    euro = currency_data['results']['currencies']['EUR']['buy']

    cursor.execute("INSERT INTO coins (Date, Dolar, Euro) VALUES (?, ?, ?)", (date, dolar, euro))
    conecction.commit()
    print(f"Registro salvo com sucesso: {date} | Dólar: R$ {dolar:.2f} | Euro: R$ {euro:.2f}")
    conecction.close()


data = get_currency_counts()
if data is None:
    print("[ERRO] Não foi possível obter dados válidos da API.")
    exit()

write_database(data)