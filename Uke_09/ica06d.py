#!/usr/bin/env python
# -*- coding: utf-8 -*-

#source/veiledning: http://codepad.org/cywKyxXO

from PIL import Image

print """
En mann har vaert paa markedet a handlet, og han har behov for aa krysse elva med en kylling, en pose med korn, 
og en rev. Det er kun plass til 2 ting i baaten saa han kan kunne bring en av tinga om gangen.
Dersom reven blir etterlatt med kyllingen alene, saa vil den spise kyllling, og kyllingen alene med korn
fører til at kyllingen vil spise kornposen så game over. Mannen maa tenke seg fram for aa ikke tape en 
eneste ting. æææ


"""

# Løsning fra internett:
#
# Mannen  tar med seg kylling først til høyre siden av elva, og reiser tilbake alene.
# Han tar da kornposen til høyre siden og tar med seg kyllingen tilbake til venstre siden
# Saa tar han med seg reven til høyre siden og kommer tilbake alene og saa endelig kan han
# ta med seg kyllingen over elva igjen(høyre siden).


# En konfigurasjon er en nested tuple: ((left,right),desc)
# left and right are sets representer "ting" på hver side av elva
# og 'desc' beskriver hvordan denne konfigurasjonen kom til 

mann,kylling,korn,rev=("mann","kylling","korn","rev")
flyttbareObjekter=(kylling,korn,rev,None)

# Ikke tillatte tilstander, game over om det skjer(skjer ikke i koden)
forbudt=(set((kylling,korn)), set((rev,kylling)))

# returnerer hvis en uspesifert aksjon skjer
# TODO: Can omskrive dette med any() og all() og listcomps
def mayhem(cfg):
    for shore in cfg[0]:
        if mann not in shore:
            for forbidden in forbudt:
                if shore.issuperset(forbidden):
                    return True
    return False

# return True når er tilstand er naad (naar alle enhetene er paa hoyre side)
def done(cfg):
    left,right=cfg[0]
    return left==set()
    
# Mannen reiser over elven, og tar en ting med seg.
# 'ting" kan bli ""None"" naar mannen ikke tar noe med seg
# Return den nye konfigurasjonen, eller None hvis kryssningen ikke kan bli gjort
# fordi tingen ikke er på samme side som mammen
def boat(cfg,item):
    left,right=[set(x) for x in cfg[0]] # lage kopier, fordi 'left' og 'right' vil bli mutert
    # finne ut hvilken side mannen er på, og til hvilken side han vil kjore baaten
    if mann in left:
        src,dst=left,right
    else:
        src,dst=right,left
    # gjore det klart om man skal kjore en ting, at det er paa samme side som mammen
    if item and not item in src:
        return None
    # krysse elven med muligvis en ting
    desc="Mannen reiser over elva  -->" if mann in left else "Mannen reiser tilbake <--"
    src.remove(mann)
    dst.add(mann)
    if item:
        src.remove(item)
        dst.add(item)
        desc+=" med "+item
    else:
        desc+=" alene"
    return ((left,right),desc) # return konfigurasjonen

# printe ut en konfigurasjon
def printcfg(cfg,level=0):
    left,right=cfg[0]
    verdict="(Not allowed)" if mayhem(cfg) else "(Ok)"
    print "    "*level,", ".join(left),"  ~~~  ",", ".join(right),cfg[1],verdict

# gi en spesiell konfiguarsjon, lage en konfigurasjon som kan komme ut av det
def onegeneration(cfg):
    followups=[]
    for item in flyttbareObjekter:
        followup=boat(cfg,item)
        if not followup: continue
        followups.append(followup)
    return followups

# rekursivt generere en set konfigurasjon
def generate(cfg,level=0):
    solutionstack.extend([None]*(level-len(solutionstack)+1))
    solutionstack[level]=cfg[1]
    printcfg(cfg,level)
    childs=onegeneration(cfg)
    for child in childs:
        if mayhem(child): # hoppe over konfigurasjoner som ikke er lov
            continue
        if child[0] in previouscfgs: # hoppe over konfigurasjoner som er blitt brukt før
            continue
        previouscfgs.append(child[0])
        generate(child,level+1)
        
 #litt rotete løsning, men bilde som åpnes henviser til de forskjellige tilstandene 
 #etter visse commands
img = Image.open('goose.jpg')
img.show()

# begynn konfigurasjon
cfg=((set((mann,kylling,korn,rev)), set()),"")

# dette lagrer tidligere konfigurasjoner som er blir brukt
previouscfgs=[cfg[0]]

# lagre en løsning for senere printing
solutionstack=[]

# kjør
print "Fremgangsmaate for aa loese problemet:"
generate(cfg)

print "Endelig losning:"
for step in solutionstack:
    if step:
        print "  ",step
        
        