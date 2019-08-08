miasto1 = {'miasto' : 'lisbona',
        'panstwo': 'hiszpania',
        'liczba' : 10}

miasto2 = {'miasto' : 'warszawa',
        'panstwo': 'polska',
        'liczba' : 15}

miasto3 = {'miasto' : 'praga',
        'panstwo': 'czechy',
        'liczba' : 15}

miasto = [miasto1, miasto2,miasto3]


def dodajmiasto(miejsce,miasto):
    if miejsce in miasto:
        print("Klient juz istnieje")
    else:
        miasto.append(miejsce)

def znajdzKlient(miejsce,miasto):
    if miejsce in miasto:
        print('miasto ' + miejsce['miasto'] + ' istnieje w bazie')
    else:
        print('Nie ma takiego miasta')

def usunKlienta(miejsce,miasto):
    if miejsce in miasto:
        miasto.remove(miejsce)
        print('miasto ' + miejsce['miasto'] + ' nie istnieje juz w bazie')
    else:
        print('Nie usunięto, nie ma takiego miasta')

def zmienKlienta(noweMiejsce, miejsce,miasto):
    if miejsce not in miasto:
        print('Nie ma takiego miasta')
    else:
        index=miasto.index(miejsce)
        miasto[index]['panstwo']=  noweMiejsce['panstwo']
        miasto[index]['miasto']= noweMiejsce['miasto']
        miasto[index]['liczba'] = noweMiejsce['liczba']

def znajdzMiasto(miastoNowe ,panstwoNowe ,miasto ):
    miasta = ''
    for miasta in miasto:
        if (miasta['miasto'] == miastoNowe and miasta['panstwo'] == panstwoNowe):
                print('jest takie miasto ' + miastoNowe + ' w panstwie ' +  panstwoNowe )
        else:
                print('miasto' + miastoNowe + 'nie istnieje w danym panstwie ' + panstwoNowe)

def znajdzNajwieksze(miasto):
    miastoNajw = 0
    for miasta in miasto:
        if (miasta['liczba'] > miastoNajw):
            miastoNajw = miasta['liczba']
            print('Najwiekszym miastem jest ' + miasta['miasto'])

def znajdzNajmniejsze(miasto):
    miastoNajm = 999
    for miasta in miasto:
        if (miasta['liczba'] < miastoNajm):
            miastoNajm = miasta['liczba']
            print('Najmniejszym miastem jest ' + miasta['miasto'])

dodajmiasto({'miasto':'lublin','panstwo':'polska','liczba':30},miasto)
print(miasto)
znajdzKlient({'miasto':'lublin','panstwo':'polska','liczba':30},miasto)
usunKlienta({'miasto':'lublin','panstwo':'polska','liczba':30},miasto)
zmienKlienta({'miasto':'zabrze','panstwo':'polska','liczba':60},{'miasto' : 'praga','panstwo': 'czechy', 'liczba' : 15},miasto)
print(miasto)
znajdzMiasto('zabrze','polska',miasto)
znajdzNajwieksze(miasto)
znajdzNajmniejsze(miasto)