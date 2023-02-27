def histogram(s):
    d = dict()
    for c in s:
        if c == ' ' : continue
        if c ==',': continue
        d[c] = d.get(c, 0) + 1   
    return invert_dic(d)

def invert_dic(d):
    inverse = {}
    for key in d:
        inverse.setdefault(d[key], key)
    return growing_order(inverse)

def growing_order(d):
    keys = list(d.keys())
    orderly = list()
    while len(keys) != 0:
        frequency = "{}: {}".format(max(keys), d.get(max(keys), None))
        orderly.append(frequency)
        keys.remove(max(keys))
    return orderly

Portuguese = """ Pai nosso, que estás nos céus, santificado seja o Teu nomevenha a nós o Teu reino
                Seja feita a Tua vontade, assim na terra como no céu
                O pão nosso de cada dia nos dai hoje
                E perdoa-nos as nossas dívidas, assim como nós temos perdoado aos nossos devedores
                E não nos deixes cair em tentação; mas livra-nos do mal 
                Amém"""

Spanish = """   Padre nuestro que estás en los cielos,
                santifíquese tu nombre
                venga tu reino
                hágase tu voluntad
                como en el cielo también sobre la tierra
                nuestro pan cotidiano dánoslo hoy
                Y perdónanos nuestras deudas,
                como también nosotros perdonamos a nuestros deudores.
                Y no nos induzcas a la tentación,
                sino líbranos del mal.
                Amén""" 

French = """Notre Père qui es dans les cieux
            Sanctifié soit ton Nom
            Vienne ton Règne
            Que soit faite ta volonté sur terre comme au ciel
            Notre pain quotidien, donne-le-nous aujourdhui
            Et remets-nous nos dettes, Comme nous avons remis à nos débiteurs
            Et ne nous laisse pas entrer en tentation
            Mais délivre-nous du Mauvais.
            Car cest à toi quappartiennent le règne, la puissance et la gloire pour les siècles des siècles
            Amem"""

English = """   Our Father in heaven
                hallowed be your name.
                Your kingdom come.
                Your will be done, on(in) earth as it is in heaven.
                Give us this day our daily bread. 
                And forgive us our debts, as we also have forgiven our debtors.
                And do not bring us to the time of trial, but rescue us from the evil one
                Amem"""

print(histogram(Portuguese))
print(histogram(Spanish))
print(histogram(French))
print(histogram(English))