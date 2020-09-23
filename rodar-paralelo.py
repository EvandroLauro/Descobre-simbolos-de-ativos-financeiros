import threading
import os

def inicia_programa(nome_arquivo):
    os.system('py -3.7 {}'.format(nome_arquivo))
    # Ex: os.system('py -3.7 x.py')

if __name__ == "__main__":

    arquivos = ['requisitando-A.py', 'requisitando-B.py', 'requisitando-C.py', 'requisitando-D.py', 'requisitando-E.py',
                'requisitando-F.py', 'requisitando-G.py', 'requisitando-H.py', 'requisitando-I.py', 'requisitando-J.py',
                'requisitando-K.py', 'requisitando-L.py', 'requisitando-M.py', 'requisitando-N.py', 'requisitando-O.py',
                'requisitando-P.py', 'requisitando-Q.py', 'requisitando-R.py', 'requisitando-S.py', 'requisitando-T.py',
                'requisitando-U.py', 'requisitando-V.py', 'requisitando-W.py', 'requisitando-X.py', 'requisitando-Y.py',
                'requisitando-Z.py']

    processos = []
    for arquivo in arquivos:
        processos.append(threading.Thread(target=inicia_programa, args=(arquivo,)))
        # Ex: adicionar o porcesso `threading.Thread(target=inicia_programa, args=('x.py',))`

    for processo in processos:
        processo.start()