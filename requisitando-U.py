import sqlite3
import yfinance as yf

tabelaFicçao = 'U'
tabelaTestado = 'U'
ativosExiste = 'Ativos'

con1 = sqlite3.connect('ativos-ficção.db')
cursor1 = con1.cursor()

con2 = sqlite3.connect('ativos-ficção-testado.db')
cursor2 = con2.cursor()
cursor2.execute("create table if not exists'" + str(tabelaTestado) + "' (AtivosTestados)")

con3 = sqlite3.connect('ativos-existente.db')
cursor3 = con3.cursor()
cursor3.execute("create table if not exists'" + str(ativosExiste) + "' (ListaDeAtivos)")

getFicção = []
for t in tabelaFicçao:
    cursor1.execute('SELECT AtivosFicção FROM "' + str(t) + '"')
    rows = cursor1.fetchall()
    for row in rows:
        lista = list(row)
        format1 = str(lista).strip('[]')
        format2 = format1.replace("'", '')
        format3 = format2.replace(",", '')
        format4 = format3.replace(" ", '')
        getFicção.append(format4)

getTestado = []
for t in tabelaTestado:
    cursor2.execute('SELECT AtivosTestados FROM "' + str(t) + '"')
    rows = cursor2.fetchall()
    for row in rows:
        lista = list(row)
        format1 = str(lista).strip('[]')
        format2 = format1.replace("'", '')
        format3 = format2.replace(",", '')
        format4 = format3.replace(" ", '')
        getTestado.append(format4)

ativosNaoTestado = []
for i in getFicção:
    existe = i in getTestado
    if existe == False:
        ativosNaoTestado.append(i)

contarAtivosNaoTestado = len(ativosNaoTestado)

getContarAtivosNaoTestado = []
for c in range(contarAtivosNaoTestado):
    getContarAtivosNaoTestado.append(tabelaTestado)

for a, t in zip(ativosNaoTestado, getContarAtivosNaoTestado):
    data = yf.download(a, period='1d')
    price = data[['Open']]
    result = price.values.tolist()
    if result == []:

        cursor2.execute("INSERT INTO'" + str(t) + "'(AtivosTestados) VALUES(?)", (a,))
        con2.commit()
    else:
        table = 'Ativos'
        cursor3.execute("INSERT INTO'" + str(table) + "'(ListaDeAtivos) VALUES(?)", (a,))
        con3.commit()

con1.commit()
