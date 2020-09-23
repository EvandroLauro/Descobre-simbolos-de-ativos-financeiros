import itertools
import sqlite3

con = sqlite3.connect('ativos-ficção.db')
cursor = con.cursor()
caracteres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']

get = []

for l in range(4):
    for subset in itertools.product(caracteres, repeat=4):
        get.append(subset)


numeros = ['3','4','11']
listaAtivos = []
tabela = []
for g in get:
    lista = list(g)
    format1 = str(lista).strip('[]')
    format2 = format1.replace("'", '')
    format3 = format2.replace(",", '')
    format4 = format3.replace(" ", '')
    if format4 == 'ZZZZ':
        break
    for n in numeros:
        simbolos = format4 + n + '.SA'

        for l in caracteres:
            i = simbolos[0]
            if i == l:
                listaAtivos.append(simbolos)
                tabela.append(l)

for l, t in zip(listaAtivos, tabela):
    print(l, t)
    cursor.execute("create table if not exists'" + str(t) + "' (AtivosFicção)")
    cursor.execute("INSERT INTO'" + str(t) + "'(AtivosFicção) VALUES(?)", (l,))
con.commit()

