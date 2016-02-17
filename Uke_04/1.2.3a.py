'''
Module med eksempler i uke 04 (informasjonsteori)
Løsninger for klasseoppgavene 25.01.2016 implementeres her
Løsningsforslag innleveres i gruppe-repositorien.
GRUPPENR: 09
STUDENTER: Sigurd Tveit Kristoffersen, Christian Fjelde Lima, Gunnhild Solsvik, Magnus Pedersen, Emil Lekang
'''
'''ascii tegn til binære tegn "banan" til binæretall, kunne også representert andre ascii tegn i tabellen under '''
ascii = {'a': '01100001', 'b' : '01100010', 'c': '01100011', 'd': '01100100',
        'n': '01101110'}
print ascii['b'],
print ascii['a'],
print ascii['n'],
print ascii['a'],
print ascii['n'],

''' En liten tabell som inneholder binæretall og hva ascii tegn disse representer, print tar i bruk noen av tallene og produserer et resultat som staver agder '''
binary = {'01100001': 'a',  '01100111': 'g', '01100100': 'd', '01100101': 'e', '01110010': 'r', '01101001': 'i', '01110000': 'p', '01111000': 'x'} 

print binary ['01100001'],
print binary ['01100111'],
print binary ['01100100'],
print binary ['01100101'],
print binary ['01110010'],