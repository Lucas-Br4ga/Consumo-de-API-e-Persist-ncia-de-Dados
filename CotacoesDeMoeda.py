import sqlite3
import datetime
import requests
def createtables():
    conecction = sqlite3.connect('bdcotacoes.db')
    cursor = conecction.cursor()
    cursor.execute("select name from sqlite_master where type='table' and name='coins'")
    table_exists = cursor.fetchall()
    if table_exists:
        print("Table 'Coins' already exists.")
        return
    else:
        sql ='create table coins(' \
            'requestID integer primary key autoincrement,'\
            'Date varchar(20) not null,'\
            'Dolar real,'\
            'Euro real)'

        cursor.execute(sql)
        print("Table 'Coins' table created successfully.")


def getcurrencycounts():
    key = "c8c29944"
    format = "json-cors"
    url = f"https://api.hgbrasil.com/finance/quotations?format={format}&key={key}"
    request = requests.get(url)
    if request.status_code == requests.codes.ok:
        data = request.json()
        return data



def writedatabase(data):
    conecction = sqlite3.connect('bdcotacoes.db')
    cursor = conecction.cursor()
    dateobject = datetime.datetime.now()

    date  = '{}/{}/{} {}:{}:{}'.format(dateobject.day, dateobject.month,dateobject.year,dateobject.hour,dateobject.minute,dateobject.second)
    dolar = data['results']['currencies']['USD']['buy']
    euro = data['results']['currencies']['EUR']['buy']
    cursor.execute("INSERT INTO coins (Date, Dolar, Euro) VALUES (?, ?, ?)", (date, dolar, euro))
    conecction.commit()


createtables()
writedatabase(getcurrencycounts())



