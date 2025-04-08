import sqlite3
import datetime
import requests
def CreateTables():
    conecction = sqlite3.connect('bdcotacoes.db')
    cursor = conecction.cursor()
    cursor.execute("select name from sqlite_master where type='table' and name='coins'")
    table_exists = cursor.fetchall()
    if table_exists:
        print("Table 'Coins' already exists.")
        return
    else:
        sql ='create table coins(' \
            'requestID interger primary key autoincrement,'\
            'Date varchar(20) not null,'\
            'Dolar real,'\
            'Euro real)'

        cursor.execute(sql)
        print("Table 'Coins' table created successfully.")
def GetCurrencyCounts():
    conecction = sqlite3.connect('bdcotacoes.db')
    cursor = conecction.cursor()
    key = "c8c29944"
    format = "json"
    url = f"https://api.hgbrasil.com/finance/quotations?format={format}&key={key}"
    request = requests.get(url)
    if request.status_code == requests.codes.ok:
        data = request.json()
        dateObject = datetime.datetime.now()

        date  = '{}/{}/{} {}:{}:{}'.format(dateObject.day, dateObject.month,dateObject.year,dateObject.hour,dateObject.minute,dateObject.second)
        dolar = data['results']['currencies']['USD']['buy']
        euro = data['results']['currencies']['EUR']['buy']
        cursor.execute("INSERT INTO coins (Date, Dolar, Euro) VALUES (?, ?, ?)", (date, dolar, euro))
        conecction.commit()




CreateTables()
GetCurrencyCounts()



